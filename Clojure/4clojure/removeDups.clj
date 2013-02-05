(println
  ((fn removeDups [x]
     (if (nil? x)
       []
       (let [[a b _] x]
         (println a)
         (println b)
         (println "-")
         (concat 
           (if (= a b)
             nil
             [a])
           (removeDups (next x))))))
     [1 2 3 3 3 4 4 5 5 5 5 6]))
