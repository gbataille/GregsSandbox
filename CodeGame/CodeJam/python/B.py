#!/usr/local/bin/python3
import sys
from math import ceil, floor

DEBUG = True

def readCase(fin):
  D = readInt(fin)
  diners = readIntList(fin)
  return (D, diners)

def handleCase(caseNum, fin, fout):
  fout.write("Case #%d: " % caseNum)
  p('\ncase #' + str(caseNum))

  ########## Code Here ###########

  (D, diners) = readCase(fin)
  p(" input {0}".format(diners))
  diners.sort(reverse = True)
  done = False
  special = 0
  p(slice([5,5]))
  while not done:
    maxPancake = diners[0]
    fHalfMax = floor(maxPancake / 2.0)
    cHalfMax = ceil(maxPancake / 2.0)
    n = count(diners, cHalfMax)
    p("n {0}".format(n))
    if cHalfMax > n and n > 0:
      special += n
      diners = split(diners, fHalfMax)
    else:
      done = True

    p("  iter: special {0}, diners {1}".format(special, diners))

  p("answer {0}".format(special + diners[0]))
  p("diners {0}".format(diners))

  # outputIntList(soluces, fout)
  # outputStrList(soluces, fout)
  # outputStr(soluce, fout)
  outputInt(special + diners[0], fout)

  ################################

  fout.write("\n")
  return

def slice(diners):
  vMax = diners[0]
  vMaxCount = diners.count(vMax)
  rest = diners[(vMaxCount):len(diners)]

  while (len(rest) > 1) and (rest[0] >= vMax - vMaxCount):
    p("rest[0] {0}, vMax {1}, vMaxCount {2}".format(rest[0], vMax, vMaxCount))
    vCount = rest.count(rest[0])
    vMaxCount += vCount
    rest = rest[(vCount):len(rest)]

  return vMaxCount

def split(diners, threshold):
  done = False
  newDiners = []
  while not done:
    value = diners.pop(0)
    if value > threshold:
      # print("value {0}, threshold {1}".format(value, threshold))
      # print(ceil(value/2.0))
      # print(floor(value/2.0))
      newDiners.append(ceil(value/2.0))
      newDiners.append(floor(value/2.0))

      if diners == []:
        done = True
    else:
      done = True

  newDiners.extend(diners)
  newDiners.sort(reverse=True)
  return newDiners

def count(l, threshold):
  res = 0
  for e in l:
    if e > threshold:
      res += 1
    else:
      break

  return res




###############################################################
## Boiler Plate
###############################################################


def main(argv = None):
  pbName = __file__[1 + __file__.rfind("/"):__file__.rfind(".")]

  if argv is None:
    argv = sys.argv

  fin = open(pbName + '.in', 'r')
  fout = open(pbName + '.out', 'w')

  nbCases = int(fin.readline())

  for caseNum in range(1, nbCases + 1):
    handleCase(caseNum, fin, fout)

  fin.close()
  fout.close()

def readInt(fin):
  return int(fin.readline())

def readIntList(fin):
  return list(map(int, fin.readline().split(' ')))

def readStr(fin):
  return fin.readline().rstrip('\n')

def outputIntList(l, fout):
  outputStrList(map(str, l), fout)

def outputStrList(l, fout):
  fout.write(' '.join(l))

def outputStr(s, fout):
  fout.write(s)

def outputInt(i, fout):
  outputStr(str(i), fout)

def p(s):
  if DEBUG:
    print(s)

# Main invoke
if __name__ == "__main__":
  sys.exit(main())
