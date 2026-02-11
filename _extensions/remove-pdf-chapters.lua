-- Remove specific chapters from PDF output.
-- The copyright page is injected via include-before-body instead,
-- and the purchase page should not appear in the PDF at all.

local chapters_to_remove = {
  ["copyright"] = true,
  ["purchase-print-edition"] = true,
}

-- Handle section-divs case (sections wrapped in Div elements)
function Div(el)
  if quarto.doc.is_format("latex") and chapters_to_remove[el.identifier] then
    return {}
  end
end

-- Handle flat-blocks case (headers at top level)
function Pandoc(doc)
  if not quarto.doc.is_format("latex") then
    return doc
  end

  local new_blocks = pandoc.List()
  local removing = false
  local remove_level = 0

  for _, block in ipairs(doc.blocks) do
    if block.t == "Header" then
      if chapters_to_remove[block.identifier] then
        removing = true
        remove_level = block.level
      elseif removing and block.level <= remove_level then
        removing = false
      end
    end

    if not removing then
      new_blocks:insert(block)
    end
  end

  doc.blocks = new_blocks
  return doc
end
