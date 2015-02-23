#!/usr/local/bin/python3
import sys

def readCase(fin):
  return readStr(fin)

def handleCase(caseNum, fin, fout):
  fout.write("Case #%d: " % caseNum)

  ########## Code Here ###########
  touch = { 
       'a' : '2'
      , 'b' : '22'
      , 'c' : '222'
      , 'd' : '3'
      , 'e' : '33'
      , 'f' : '333'
      , 'g' : '4'
      , 'h' : '44'
      , 'i' : '444'
      , 'j' : '5'
      , 'k' : '55'
      , 'l' : '555'
      , 'm' : '6'
      , 'n' : '66'
      , 'o' : '666'
      , 'p' : '7'
      , 'q' : '77'
      , 'r' : '777'
      , 's' : '7777'
      , 't' : '8'
      , 'u' : '88'
      , 'v' : '888'
      , 'w' : '9'
      , 'x' : '99'
      , 'y' : '999'
      , 'z' : '9999'
      , ' ' : '0'
      }

  s = readCase(fin)
  prev = 'a'
  for c in s:
    comb = touch[c]
    comb1 = comb[0]
    if comb1 == prev:
      outputStr(' ', fout)
    prev = comb1
    outputStr(comb, fout)


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

# Main invoke
if __name__ == "__main__":
  sys.exit(main())
