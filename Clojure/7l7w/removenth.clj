;(println
;  ((fn [x n]
;    (keep (filter #(not= 0 (mod % n)) (iterate inc 1)) x))
;     [1 2 3 4 5 6 7 8] 3))

(println
  ((fn [x n]
    (keep-indexed #(if (not= 0 (mod (+ 1 %1) n)) %2)  x))
     [1 2 3 4 5 6 7 8] 3))

(println
  ((fn [list1 diviseur]
    (map
      (fn [n] (keep-indexed (fn [ind elem] (if (= (mod n diviseur) (mod (inc ind) diviseur)) elem)) list1))
      (range 1 (inc diviseur))))
  [1 2 3 4 5 6] 2))
