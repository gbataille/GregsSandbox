(println
  ((fn [x y]
      (apply + (concat (second x) [y])))
     [[] []] 0))

(println "-----")

(println
(take 5
  (first ((fn [func a]
      (reduce
        ;I want a function that returns a list of 2 elements.
        ;First element is the consecutive list of intermediate answers
        ;Second element is the new answer
        (fn [x y]
          (let [z (concat (second x) [y])]
          ;(println x)
          ;(println y)
          ;(println z)
          ;(println "")
          (conj []
            (concat (first x) [(apply func z)])
            [(apply func z)])))
        [[] []] (lazy-seq a)))
      + (range)))))
