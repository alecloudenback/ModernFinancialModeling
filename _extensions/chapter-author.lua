-- Display chapter-level author in PDF output
-- For book projects, reads author from source files based on chapter structure

local function get_author_and_id_from_file(filepath)
  local file = io.open(filepath, "r")
  if not file then
    return nil, nil
  end

  local content = file:read("*all")
  file:close()

  -- Normalize line endings (handle Windows \r\n)
  content = content:gsub("\r\n", "\n"):gsub("\r", "\n")

  -- Extract YAML frontmatter
  local yaml_start, yaml_end = content:find("^%-%-%-\n")
  if not yaml_start then
    return nil, nil
  end

  local _, yaml_close = content:find("\n%-%-%-", yaml_end)
  if not yaml_close then
    return nil, nil
  end

  local yaml_content = content:sub(yaml_end + 1, yaml_close - 4)
  local after_yaml = content:sub(yaml_close + 1)

  -- Extract H1 header ID from content after YAML
  -- Matches: # Title {#some-id} or # Title
  local h1_id = after_yaml:match("\n#%s+[^\n]+%s*{#([^}]+)}")
  if not h1_id then
    -- No custom ID, try to derive from title (Quarto auto-generates IDs)
    local h1_title = after_yaml:match("\n#%s+([^\n{]+)")
    if h1_title then
      -- Convert title to ID: lowercase, replace spaces with hyphens
      h1_id = h1_title:lower():gsub("%s+", "-"):gsub("[^%w%-]", ""):gsub("%-+", "-"):gsub("^%-", ""):gsub("%-$", "")
    end
  end

  -- Parse authors from YAML
  local authors = {}

  -- Handle "author: Name" format (single line)
  local single_author = yaml_content:match("author:%s*([^\n]+)")
  if single_author and not single_author:match("^%s*$") and not single_author:match("^%s*%-") then
    single_author = single_author:match("^%s*(.-)%s*$")
    table.insert(authors, single_author)
  else
    -- Handle "author:\n  - name: Name" format (can have multiple)
    for name in yaml_content:gmatch("%-%s*name:%s*([^\n]+)") do
      name = name:match("^%s*(.-)%s*$")
      if name and name ~= "" then
        table.insert(authors, name)
      end
    end
  end

  if #authors == 0 then
    return nil, h1_id
  end

  return table.concat(authors, ", "), h1_id
end

local function build_chapter_author_map(meta)
  local chapter_authors = {}

  -- Get project directory
  local project_dir = nil
  if quarto and quarto.project and quarto.project.directory then
    project_dir = quarto.project.directory
    if not project_dir:match("/$") then
      project_dir = project_dir .. "/"
    end
  elseif quarto and quarto.doc and quarto.doc.input_file then
    project_dir = quarto.doc.input_file:match("(.*/)")
  end

  if not project_dir then
    return chapter_authors
  end

  -- Read _quarto.yml to get chapter list
  local quarto_yml = io.open(project_dir .. "_quarto.yml", "r")
  if not quarto_yml then
    return chapter_authors
  end

  local yml_content = quarto_yml:read("*all")
  quarto_yml:close()

  -- Find all .qmd files mentioned in the yml
  for qmd_file in yml_content:gmatch("([%w%-_]+%.qmd)") do
    local filepath = project_dir .. qmd_file
    local authors, h1_id = get_author_and_id_from_file(filepath)
    if authors and h1_id then
      chapter_authors[h1_id] = authors
    end
  end

  return chapter_authors
end

function Pandoc(doc)
  local chapter_authors = build_chapter_author_map(doc.meta)

  local new_blocks = {}

  for _, block in ipairs(doc.blocks) do
    table.insert(new_blocks, block)

    if block.t == "Header" and block.level == 1 and block.identifier then
      local author = chapter_authors[block.identifier]
      if author then
        local author_para = pandoc.Para({
          pandoc.RawInline("latex", "\\textcolor{gray}{\\textsc{Chapter Authored by: " .. author .. "}}")
        })
        table.insert(new_blocks, author_para)
      end
    end
  end

  doc.blocks = new_blocks
  return doc
end
