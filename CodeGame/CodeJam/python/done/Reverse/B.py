#!/usr/local/bin/python3
import sys

def readCase(fin):
  s = readStr(fin)
  return s

def handleCase(caseNum, fin, fout):
  fout.write("Case #%d: " % caseNum)

  ########## Code Here ###########

  s = readCase(fin)
  listWords = list(s.split(' '))
  listWords.reverse()
  outputStr(' '.join(listWords), fout)

  # outputIntList(soluces, fout)
  # outputStrList(soluces, fout)
  # outputInt(soluce, fout)

  ################################

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

def readStr(fin):
  return fin.readline().rstrip()

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
