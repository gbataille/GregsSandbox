module Main where
  fibNextPair :: (Integer, Integer) -> (Integer, Integer)
  fibNextPair (x, y) = (y, x + y)

  fibNthPair :: Integer -> (Integer, Integer)
  fibNthPair 1 = (1, 1)
  fibNthPair x = fibNextPair (fibNthPair (x - 1))

  fib :: Integer -> Integer
  fib = fst . fibNthPair
