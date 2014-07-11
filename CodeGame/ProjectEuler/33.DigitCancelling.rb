#!/usr/bin/env ruby

def simpl (a, b)
  aa = a.to_s.chars
  ab = b.to_s.chars
  sol = []

  aa.each_index do |aaInd|
    abInd = ab.index(aa[aaInd])
    if abInd != nil
      aa.delete_at(aaInd)
      ab.delete_at(abInd)

      frac = a.to_f / b
      sfrac = aa.join.to_f / ab.join.to_f

      if (frac - sfrac).abs < 0.0001
        sol.push(a)
        sol.push(b)
      end
    end
    if abInd == 0 and ab[1] == aa[aaInd]
      aa.deleteAt(aaInd)
      ab.deleteAt(abInd)

      frac = a.to_f / b.to_f
      sfrac = aa.join.to_f / ab.join.to_f

      if (frac - sfrac).abs < 0.000001
        sol.push([a, b])
      end
    end
  end

  return sol
end

soluce = []

for i in (11..99)
  if i % 10 == 0
    next
  end

  digit = i.to_s.chars[0].to_i
  2.times {
    for j in (1..9)
      denom = 10.0*j + digit
      denom2 = 10.0*digit + j

      if i < denom
        sol = simpl(i, denom)
        if not sol.empty?
          soluce.push sol
        end
      end
      if i < denom2
        sol = simpl(i, denom2)
        if not sol.empty?
          soluce.push sol
        end
      end
    end
    digit = i.to_s.chars[1].to_i
  }
end

num = 1
denum = 1

soluce.each do |pair|
  num *= pair[0]
  denum *= pair[1]
end

p soluce
p num
p denum
