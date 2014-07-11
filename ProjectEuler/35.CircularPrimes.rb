#!/usr/bin/env ruby

require 'prime'

prime = Prime.take_while { |i| i <= 1000000 }

count = 0

prime.each do |p|
  circular = true
  #permutations
  ps = p.to_s
  pa = ps.chars
  if (pa.take_while{|i| i == pa[0]}).length != pa.length
    (ps.length - 1).times {
      permP = pa.push(pa.shift).join.to_i
      ind = prime.index(permP)
      if ind == nil
        circular = false
        break
      else
        prime.delete_at ind
      end
    }
  end
  if circular
    if (pa.take_while{|i| i == pa[0]}).length == pa.length
      count += 1
    else
      count += ps.length
    end
  end
end
