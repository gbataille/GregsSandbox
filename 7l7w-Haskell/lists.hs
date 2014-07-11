module Main where
  size [] = 0
  size (h:t) = 1 + size t

  prod [] = 1
  prod (h:t) = h * prod t

  rev ([], x) = ([], x)
  rev (h:t, x) = rev (t, h:x)

  second (a, b) = b

  reverso  = second . rev
