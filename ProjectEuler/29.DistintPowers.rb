#!/usr/bin/env ruby

h = {}

2.upto(100) do |a|
  2.upto(100) do |b|
    h.store(a**b, true)
  end
end

p h.keys.count
