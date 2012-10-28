(println
  ((fn flat [x]
     (println x)
     (if (sequential? x)
       (if (empty? x)
         x
         (concat (flat (first x)) (flat (rest x))))
       [x]))
     '((1 2) (3 4))))

(println(
(fn flt [coll]
    (let [l (first coll) r (next coll)]
          (println l)
          (println r)
          (println "-")
          (concat 
                  (if (sequential? l)
                            (flt l)
                            [l])
                  (when (sequential? r)
                            (flt r)))))
         '((1 2) (3 4))))
