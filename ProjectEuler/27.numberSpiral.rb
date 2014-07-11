#!/usr/bin/env ruby

diagonals = [1]
increment = 2
while increment < 1001
  4.times { diagonals.push(diagonals.last + increment) }
  increment += 2
end

sum = 0
diagonals.each do |d|
  sum += d
end

p sum
