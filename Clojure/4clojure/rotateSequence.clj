(println
  (#(split-at 
        (mod (+ (count %2) %1) (count %2))
        %2)
  2 '(1 2 3 4 5 6)))

(println
  (#(flatten(apply conj (split-at 
        (mod (+ (count %2) %1) (count %2))
        %2)))
  2 '(1 2 3 4 5 6)))
