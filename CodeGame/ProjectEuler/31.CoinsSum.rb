#!/usr/bin/env ruby

count = 0

for h in (0..1)                                                     #200
  for i in (0..2 - 2*h)                                             #100
    for j in (0..4 - 2*i - 4*h)                                     #50
      if j % 2 == 0
        jtimes = 2.5
      else
        jtimes = 3
      end
      jbound = 10 - 2*j - 5*i - 10*h

      for k in (0..jbound).step(1)                                  #20
        for l in (0..20 - 2*k - 5*j - 10*i - 20*h)                  #10
          for m in (0..40 - 2*l - 4*k - 10*j - 20*i - 40*h)          #5
            if m % 2 == 0
              mtimes = 2.5
            else
              mtimes = 3
            end
            mbound = 100 - 2*m - 5*l - 10*k - 25*j - 50*i - 100*h

            for n in (0..mbound)  #2
              for o in (0..200 - 2*n - 5*m - 10*l - 20*k - 50*j - 100*i - 200*h)
                if (200*h + 100*i + 50*j + 20*k + 10*l + 5*m + 2*n + o) == 200
                  count += 1
                end
              end
            end
          end
        end
      end
    end
  end
end

p count
