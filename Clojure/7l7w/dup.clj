(println
  ((fn dup [x]
     (if (empty? x)
       nil
       (concat
         [(first x) (first x)]
         (dup (next x)))))
     '(1 2 3)))

(println
  ((fn [x y]
     (reduce (fn [a b] (concat a (repeat y b)) ) [] x))
     '(1 2 3) 4))
