module Main where
  fibTuple :: (Integer, Integer, Integer) -> (Integer, Integer, Integer)
  fibTuple (x, y, 0) = (x, y, 0)
  fibTuble (x, y, index) = fibTuble (y, x + y, index - 1)

  fibResult :: (Integer, Integer, Integer) -> Integer
  fibResult (x,y,z) = x

  fibo :: Integer -> Integer
  fibo x = fibResult (fibTuble (0,1,x))
