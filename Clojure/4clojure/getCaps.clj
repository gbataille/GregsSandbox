(println
  ((fn caps [x]
     (clojure.string/join
       (let [l (first x) r (rest x)]
         (concat
           (if (= (clojure.string/upper-case l) (str l))
             (if (not= (clojure.string/upper-case l) (clojure.string/lower-case l))
               [l]
               [])
             [])
           (if (empty? r)
             nil
             (caps r))))))
     "HeLlO, WoRlD!"))
