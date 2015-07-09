#!/usr/bin/env ruby
require 'CSV'

csv_headers = nil
csv_lines = []
csv_line_headers = []

# Parse CSV
CSV.foreach("matrix.csv") do |line|
  if not csv_headers
    csv_headers = line[1, line.length]
  else
    csv_lines << { header: line[0], data: line[1, line.length].map!{ |v| v == nil ? 0 : v } }
    csv_line_headers << line[0]
  end
end

p csv_headers
p csv_lines

# Add columns to the end
new_columns_count = 0
csv_line_headers.each do |header|
  if not csv_headers.find_index(header)
    csv_headers << header
    new_columns_count += 1
  end
end

add_columns = []
new_columns_count.times { add_columns << 0 }

csv_lines.each do |line|
  line[:data] += add_columns
end

p csv_headers
p csv_lines

# Add lines
add_line = []
csv_headers.length.times { add_line << 0 }
csv_headers.each do |header|
  if not csv_line_headers.find_index(header)
    csv_lines << { header: header, data: add_line }
  end
end

p csv_headers
p csv_lines

