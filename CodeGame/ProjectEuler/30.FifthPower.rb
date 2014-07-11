#!/usr/bin/env ruby

fifth = {}
soluce = []

0.upto(9) do |i|
  fifth[i] = i**5
end

1000.upto(600000) do |num|
  sum = 0
  num.to_s.chars.each do |digit|
    sum += fifth[digit.to_i]
  end

  if sum == num
    soluce.push num
  end
end

sum = 0
soluce.each { |i| sum += i }
p sum
