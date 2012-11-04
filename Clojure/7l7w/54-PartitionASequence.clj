(println
  ((fn [n l]
     (->>
       (map-indexed #(list (quot %2 n) %1) l)
       (group-by first)
       vals
       (map #(map second %))
       (filter (comp #(= n %) count))
       ))

     3 (range 10)))

(println
  (#(take-nth % (apply map list (take % (iterate next %2))))
      3 (range 10)))

(println
  (#(take %1 (iterate next %2))
      3 (range 10)))

(println(apply map list [[0 1 2 3 4 5 6 7 8 9] [1 2 3 4 5 6 7 8 9] [2 3 4 5 6 7 8 9]]))
(println(apply map + [[0 1 2 3 4 5 6 7 8 9] [1 2 3 4 5 6 7 8 9] [2 3 4 5 6 7 8 9]]))
(println(apply map + [[0 1 2 3 4 5 6 7 8 9] [1 2 3 4 5 6 7 8 9] [2 3 4 5 6 7 8 9]]))

(println(map + [1 2 3] [10 11 12]))
