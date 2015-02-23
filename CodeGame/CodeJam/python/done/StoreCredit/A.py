#!/usr/local/bin/python3
import sys

def readCase(fin):
  C = readInt(fin)
  I = readInt(fin)
  prices = readIntList(fin)

  return (C, I, prices)

def handleCase(caseNum, fin, fout):
  fout.write("Case #%d: " % caseNum)

  ####

  C, I, prices = readCase(fin)
  trouve = False
  for i1 in range(0, I-1):
    if trouve:
      break
    for i2 in range(i1 + 1, I):
      if trouve:
        break
      if (prices[i1] + prices[i2]) == C:
        outputIntList([i1 + 1, i2 + 1], fout)
        trouve = True

  ####

  fout.write("\n")
  return





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

def outputIntList(l, fout):
  outputStrList(map(str, l), fout)

def outputStrList(l, fout):
  fout.write(' '.join(l))

def outputStr(s, fout):
  fout.write(s)

def outputInt(i, fout):
  outputStr(str(i), fout)

# Main invoke
if __name__ == "__main__":
  sys.exit(main())
