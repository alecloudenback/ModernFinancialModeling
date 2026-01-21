-- Truncate cell output to a maximum number of lines
-- Usage: #| max-lines: 20

local function truncate_text(text, max_lines)
  local lines = {}
  for line in text:gmatch("([^\n]*)\n?") do
    table.insert(lines, line)
  end
  -- Remove trailing empty line from gmatch
  if lines[#lines] == "" then
    table.remove(lines)
  end

  if #lines > max_lines then
    local truncated = {}
    for i = 1, max_lines do
      table.insert(truncated, lines[i])
    end
    table.insert(truncated, "")
    table.insert(truncated, "... (" .. (#lines - max_lines) .. " more lines omitted)")
    return table.concat(truncated, "\n")
  end
  return text
end

local function process_output(el, max_lines)
  if el.t == "CodeBlock" then
    el.text = truncate_text(el.text, max_lines)
    return el
  elseif el.t == "RawBlock" then
    el.text = truncate_text(el.text, max_lines)
    return el
  elseif el.content then
    for i, child in ipairs(el.content) do
      el.content[i] = process_output(child, max_lines)
    end
  end
  return el
end

function Div(div)
  -- Check if this is a cell div with max-lines attribute
  local max_lines = div.attributes["max-lines"]

  if max_lines and div.classes:includes("cell") then
    max_lines = tonumber(max_lines)

    -- Process all output divs within this cell
    for i, el in ipairs(div.content) do
      if el.t == "Div" and (
        el.classes:includes("cell-output") or
        el.classes:includes("cell-output-stdout") or
        el.classes:includes("cell-output-stderr") or
        el.classes:includes("cell-output-error")
      ) then
        div.content[i] = process_output(el, max_lines)
      end
    end

    -- Remove the attribute so it doesn't appear in output
    div.attributes["max-lines"] = nil
  end

  return div
end
