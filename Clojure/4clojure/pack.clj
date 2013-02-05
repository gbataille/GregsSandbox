(println
  ((fn pack [x]
     (if (empty? x)
       nil
       (let [f (take-while (fn [y] (= (first x) y)) x)
             r (drop-while (fn [y] (= (first x) y)) x)]
         (println f)
         (println r)
         (println "-")
         (concat
           [f]
           (pack r)))))
     '(1 1 1 2 3 3)))
