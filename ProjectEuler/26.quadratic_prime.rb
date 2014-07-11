#!/usr/bin/env ruby

require 'prime'

def quadratic(a, b, n)
  return n*n + a*n + b
end

prime = Prime.instance.take_while { |p| p < 1000 }
prime = [1].concat(prime)
invPrime = prime.map { |x| x * -1 }
prime = invPrime.concat(prime)

# a = 1
# b = 41
# 0.upto(40) do |i|
#   p quadratic(a, b, i)
#   p Prime.prime?(quadratic(a,b,i))
# end
# exit
aMax = 0
bMax = 0
nMax = 0

#Try all the primes for b
prime.each do |p|
  b = p
  prime.each do |p2|
    a = p2 - b - 1
    if Prime.prime?(a)
      n = 2
      while Prime.prime?(quadratic(a, b, n)) do
        n += 1
      end
      if n > nMax
        nMax = n
        aMax = a
        bMax = b
      end
    end
  end
end

p nMax
p aMax
p bMax
p ""
p aMax * bMax
