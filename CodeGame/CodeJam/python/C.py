#!/usr/local/bin/python3
import sys

DEBUG = True

def readCase(fin):
  [L, X] = readIntList(fin)
  s = readStr(fin)
  return (L, X, s)

def handleCase(caseNum, fin, fout):
  fout.write("Case #%d: " % caseNum)

  ########## Code Here ###########

  L,X,s = readCase(fin)

  p('\ncase #{0}'.format(caseNum))
  p("L {0}, X {1}, s {2}".format(L,X,s))

  string = ""
  for i in range(0, X):
    string += s

  p("string {0}".format(string))

  for i in range(0, X*L -3):

  # outputIntList(soluces, fout)
  # outputStrList(soluces, fout)
  # outputStr(soluce, fout)
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
