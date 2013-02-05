(println
  (((fn [& list]
     (apply comp list))
     inc +) 1 2 3))

(println
  ((fn [a b]
     (fn [& list] (a (b list))))
     inc +) )

(println
  (((fn [a b]
     (fn [& l] (a (apply b l))))
     inc +) 1 2 3))

(println
  (((fn ComposeFunc [h & t]
     (if (nil? t)
       h
       (fn [& l] (h (apply (apply ComposeFunc t) l)))))
     inc inc +)
  1 2 3))
