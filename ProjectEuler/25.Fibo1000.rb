#!/usr/bin/env ruby

fibo = 1
fiboM = 1

i = 2
while fibo.to_s.size < 1000 do
  temp = fibo
  fibo += fiboM
  fiboM = temp
  i+=1
end

puts i
puts fibo


