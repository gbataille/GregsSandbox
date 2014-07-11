from random import Random
from io import FileIO

f = file("out.csv", 'w')

r = Random()

for i in range(4000):
  f.writelines(str(r.uniform(95, 105)))
  f.writelines("\n")

f.close()
