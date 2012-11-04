(println
  ((fn [x n]
     (count (filter #(= n %) x)))
     [1 1 2 3 2 1 1] 1))

(println(time
  ((fn [x]
    (apply hash-map (flatten(map 
      #(concat [(first %)] [(count (second %))]) 
      (group-by first (map (juxt identity identity) x))))))
     [1 1 2 3 1 2 4])))

(println
  ((fn [x] 
    (apply hash-map(mapcat 
      #(concat [(first %)] [(count (second %))]) 
      (group-by identity x))))
  [1 1 1 2 3 1 4 3]))

(println
  ((reduce #(assoc % %2 (+ 1 (% %2 0))) {}) [1 1 1 2 3 1 4 3]))
