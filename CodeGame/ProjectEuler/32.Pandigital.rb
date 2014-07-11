#!/usr/bin/env ruby

def pandigital(a,b,c)
  s = a.to_s + b.to_s + c.to_s
  pandigital = true
  if s.length == 9
    for i in (1..9)
      if s.index(i.to_s) == nil
        pandigital = false
      end
    end
  else
    pandigital = false
  end

  return pandigital
end

h = {}
for a in (1..9)
  for b1 in (1..9)
    if b1 == a
      next
    end
    for b2 in (1..9)
      if b2 == b1 || b2 == a
        next
      end
      for b3 in (1..9)
        if b3 == b2 || b3 == b1 || b3 == a
          next
        end
        for b4 in (1..9)
          if b4 == b3 || b4 == b2 || b4 == b1 || b4 == a
            next
          end

          #1 digit number times 4 digits number
          b = 1000*b1 + 100*b2 + 10*b3 + b4
          c = a * b
          if pandigital(a, b, c)
            h.store(c, true)
          end

          #2 digit number times 3 digit number
          d = 10*a + b1
          e = 100*b2 + 10*b3 + b4
          f = d * e
          if pandigital(d,e,f)
            h.store(f, true)
          end
        end
      end
    end
  end
end

p h
sum = 0
h.keys.each do |k|
  sum += k
end

p sum
