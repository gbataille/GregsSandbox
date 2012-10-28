(println(time
  (#(second
    (reduce 
      (fn [x y] 
        (let [[gmax gmaxlist lmax lmaxlist] x]
          (if (or
                (empty? lmaxlist)
                (= y (inc (peek lmaxlist))))
            (if (> (inc lmax) gmax)
              [(inc lmax) (conj lmaxlist y) (inc lmax) (conj lmaxlist y)]
              [gmax gmaxlist (inc lmax) (conj lmaxlist y)])
            [gmax gmaxlist 1 [y]])))
      [1 [] 0 []]
      %))
  ;[1 0 1 2 3 4 0 5 6]))
     [1 0 1 2 3 4 0 2 4 6 8 10 12 14])))


(println(time
  ((fn [[h & t :as s]]
     (->>
       (map #(list (- % %2) %2 %) t s)
       (partition-by (comp pos? first))
       (sort-by (comp - count))
       (filter (comp pos? ffirst))
       first
       (mapcat next)
       distinct))

     ;[1 0 1 2 3 4 0 5 6]))
     [1 0 1 2 3 4 0 2 4 6 8 10 12 14])))

