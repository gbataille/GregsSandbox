(println
  ((fn inter [x list1]
     (if (> (count list1) 1)
           (concat
                   [(first list1)]
                   [x]
                   (inter x (next list1)))
           list1))
     0 [1 2 3]))
