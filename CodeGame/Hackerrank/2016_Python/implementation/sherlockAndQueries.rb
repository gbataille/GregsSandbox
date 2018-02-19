#!/usr/bin/env ruby
DEBUG = false

as = ""
bs = ""
cs = ""
ARGF.each_with_index do |line, idx|
  if idx == 1
    as = line
  elsif idx == 2 
    bs = line
  elsif idx == 3
    cs = line
  end

end

a = as.split(' ').map { |x| x.to_i }
b = bs.split(' ').map { |x| x.to_i }
c = cs.split(' ').map { |x| x.to_i }

cees = {}
b.each_with_index do |bi, i|
  cees.merge!({bi => c[i]}) { |key, oldval, newval| (oldval*newval) % (10**9 + 7) }
end


cees.each do |bj, cj|
  puts "Doing bj #{bj}, with value cj #{cj}" if DEBUG
  (bj-1..(a.length - 1)).each do |i|
    puts "Checking index #{i} with value #{a[i]}" if DEBUG
    if (i + 1) % bj == 0
      a[i] = (a[i] * cj) % (10**9 + 7)
      puts "a[i] is now #{a[i]}" if DEBUG
    end
  end
end

puts a.join(' ')
