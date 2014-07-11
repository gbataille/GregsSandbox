#!/usr/bin/env ruby

# factorielle 1 is 1
# factorielle 2 is 2
# factorielle 3 is 6
# factorielle 4 is 24
# factorielle 5 is 120
# factorielle 6 is 720
# factorielle 7 is 5040
# factorielle 8 is 40320
# factorielle 9 is 362880

# def fact(num)
#   f = 1
#   num.downto(2) { |n| f*=n }
#   return f
# end

h = {}
h[0] = 1
h[1] = 1
h[2] = 2
h[3] = 6
h[4] = 24
h[5] = 120
h[6] = 720
h[7] = 5040
h[8] = 40320
h[9] = 362880


# (1..9).each { |i| puts "factorielle #{i} is #{fact(i)}" }

soluce = []

10.upto(1000000) do |i|
  sum = 0
  i.to_s.chars.each do |c|
    sum += h[ c.to_i ]
  end
  if sum == i
    soluce.push sum
  end
end

p soluce
