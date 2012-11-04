(println
  (time
  (#(vec 
      (apply sorted-set-by 
             (fn [x,y] (< (.indexOf % x) (.indexOf % y)))
             %))
      (range 50))))

(println
  ((fn [x] 
     (reduce 
       #(concat %1 [%2])
       []
       x))
     [:a :a :b :b :c :c]))

(println
  ((fn [x] 
     (reduce 
       (fn [a,b]
         (if (= -1 (.indexOf a b))
           (concat a [b])
           a))
       []
       x))
     [:a :a :b :b :c :c]))

(println
  (reduce #(if (some #{%2} %) % (conj % %2)) [] [:a :a :b :b :c :c]))

(println
    ((fn [x] (into [] (into #{} x))) [1 2 1 3 1 2 4]))
