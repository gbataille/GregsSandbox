(println
  (((fn [& func]
     (fn [& l]
       (next(reduce 
         #(concat
            %1
            [(apply %2 (first %1))])
         [l] func))))
     + min max)
      1 2 3 4))
