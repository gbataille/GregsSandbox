(println 
  ((fn [y]
    (into '() (rseq ((fn [x] 
      (if (> (count x) (- y 1)) x (recur
        (conj x (+
          (first (subvec x (- (count x) 2)))
          (last (subvec x (- (count x) 2)))
          )
        ))
      ))
    [1 1])
  ))) 10)
)
