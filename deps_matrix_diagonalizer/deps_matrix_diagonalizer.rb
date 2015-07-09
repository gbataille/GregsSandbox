#!/usr/bin/env ruby
require 'CSV'

class DepsMatrixDiagonalizer
  attr_accessor :csv_lines, :column_index, :line_index

  def initialize
    @column_index = {}
    @line_index = {}
    @csv_lines = []
  end

  def display_matrix
    @csv_lines.each do |line|
      p line
    end

    puts "\n"
  end

  def diagonalize(path, separator)
    self.parse(path, separator)
    self.add_missing_columns
    self.add_missing_lines
    self.order_lines_based_on_columns
    self.add_diag_value
    self.move_columns
    self.display_matrix
  end

  def move_columns
    (0..@csv_lines.count - 1).each do |i|
      # Start after the diagonal
      j = i + 1
      while j < @csv_lines.count
        if (i != j) and (@csv_lines[i][j] != 0)
          # Move it around
          move_column_from_to(j, i)
          move_line_from_to(j, i)
        end
        # Go to the next column
        j += 1
      end
    end
  end

  def move_column_from_to(a, b)
    # Moves the columns for each line
    @csv_lines.each_index do |i|
      line = @csv_lines[i]
      elem_to_move = line.delete_at(a)
      line.insert(b, elem_to_move)
      @csv_lines[i] = line
    end

    # Change the index
    @line_index.each_key do |key|
      index = @line_index[key]
      if index == a
        @line_index[key] = b
      elsif index >= b and index < a
        @line_index[key] = index + 1
      end
    end
  end

  def move_line_from_to(a, b)
    # Move the line around
    line = @csv_lines.delete_at(a)
    @csv_lines.insert(b, line)

    # Change the index
    @column_index.each_key do |key|
      index = @column_index[key]
      if index == a
        @column_index[key] = b
      elsif index >= b and index < a
        @column_index[key] = index + 1
      end
    end
  end

  def add_diag_value
    (0..@csv_lines.count - 1).each do |i|
      line = @csv_lines[i]
      line[i] = 1
      @csv_lines[i] = line
    end
  end

  def order_lines_based_on_columns
    new_lines = []
    @column_index.each_pair do |key, value|
      new_lines[value - 1] = @csv_lines[@line_index[key] - 1]
    end
    @csv_lines = new_lines

    # Lines and columns are now ordered the same way
    @line_index = @column_index
  end

  def add_missing_columns
    # Add columns
    # For each line that does not have a corresponding column
    new_column_count = 0
    @line_index.each_key do |key|
      if not @column_index.has_key?(key)
        @column_index[key] = @column_index.keys.count + 1
        new_column_count += 1
      end
    end
    # For each new column, add 0 at the end of the lines
    @csv_lines.each_index do |i|
      @csv_lines[i] += [0] * new_column_count
    end
  end

  def add_missing_lines
    # Add lines
    # For each column that does not have a corresponding line
    new_line_count = 0
    @column_index.each_key do |key|
      if not @line_index.has_key?(key)
        @line_index[key] = line_index.keys.count + 1
        new_line_count += 1
      end
    end
    # For each new line, add a line of 0s
    new_line_count.times {
      @csv_lines << [0] * @column_index.count
    }
  end

  def parse(path, separator)
    # Parse CSV
    line_number = 1
    csv_headers = nil
    CSV.foreach(path, {col_sep: ","}) do |line|
      if not csv_headers
        csv_headers = line[1, line.length]
        csv_headers.each_index do |i|
          @column_index[csv_headers[i]] = i + 1
        end
      else
        l = line[1, line.length]
        l.map! { |v| v.to_i}
        l.map! { |v| v == nil ? 0 : v }
        @csv_lines << l
        @line_index[line[0]] = line_number
        line_number += 1
      end
    end
  end

  def output(path, separator)
    CSV.open(path, 'wb', {col_sep: separator}) do |csv|
      cols = []
      @column_index.each_pair do |key, value|
        cols[value - 1] = key
      end
      lns = []
      @line_index.each_pair do |key, value|
        lns[value - 1] = key
      end

      csv << [" "] + cols
      p lns
      @csv_lines.each_index do |i|
        csv << [lns[i]] + @csv_lines[i].map! { |v| v == 0 ? nil : v }
      end
    end
  end
end

dmd = DepsMatrixDiagonalizer.new
dmd.diagonalize("matrix.csv", ",")
dmd.output("matrix_out.csv", ",")
