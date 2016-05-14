#!/usr/local/bin/python3
import sys

DEBUG = True

def readCase(fin):
  [X, R, C] = readIntList(fin)
  return (X, R, C)

def handleCase(caseNum, fin, fout):
  fout.write("Case #%d: " % caseNum)

  ########## Code Here ###########

  (X, R, C) = readCase(fin)
  soluce = "GABRIEL"

  small = 0
  large = 0
  if R < C:
    small = R
    large = C
  else:
    small = C
    large = R

  if (R*C % X != 0):
    soluce = "RICHARD"
  elif X == 1:
    soluce = "GABRIEL"
  elif X == 2:
    if (small == 1 and large ==3) or (small == 3 and large == 3):
      soluce = "RICHARD"
    else:
      soluce = "GABRIEL"
  elif X == 3:
    if small == 1 or large == 1:
      soluce = "RICHARD"
    elif small == 2 and large == 3:
      soluce = "GABRIEL"
    elif small == 2:
      soluce = "RICHARD"
    elif small == 3:
      soluce = "GABRIEL"
    else:
      soluce = "RICHARD"
  else:
    if (small >= 3 and large == 4):
      soluce = "GABRIEL"
    else:
      soluce = "RICHARD"

  # outputIntList(soluces, fout)
  # outputStrList(soluces, fout)
  outputStr(soluce, fout)
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
