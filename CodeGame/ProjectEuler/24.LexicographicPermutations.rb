#!/usr/bin/env ruby

listSize = 10
nth = 1000000

def fact(number)
  if number == 1
    return number
  end
  return number * fact(number-1)
end

nthElem = []
array = []
for i in 0..listSize - 1
  array.push i
end

loopcount = array.length - 1
loopcount.downto(1) do |j|
  if nth == 1
    nthElem.concat array
    break
  end

  permutation = fact(j)
  nextNumIndex = nth / permutation
  if (nth % permutation == 0)
    nthElem.push(array[nextNumIndex - 1])
    array.delete_at(nextNumIndex - 1)
    nthElem.concat array.reverse
    break
  else
    nthElem.push(array[nextNumIndex])
    array.delete_at(nextNumIndex)
  end

  nth = nth % permutation
end

puts nthElem
