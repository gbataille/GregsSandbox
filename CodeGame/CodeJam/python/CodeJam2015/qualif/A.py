#!/usr/local/bin/python3
import sys

def readCase(fin):
  return readStrList(fin)

def handleCase(caseNum, fin, fout):
  fout.write("Case #%d: " % caseNum)

  ########## Code Here ###########

  [nbPerson_s, shynesses] = readCase(fin)
  nbPerson = int(nbPerson_s)

  # print('\n' + str(caseNum))
  runningTot = []
  missing = 0
  for i, shyness in enumerate(shynesses):
    # print("i = {0}, shyness = {1}".format( i, shyness ))
    if i == 0:
      runningTot.append(int(shyness))
    else:
      runningTot.append(int(shyness) + runningTot[i-1])

      if int(shyness) > 0:
        missingPerson = i - runningTot[i-1] - missing
        # print("runningTot = {0}, {1}".format(runningTot[i-1], missingPerson))
        if missingPerson > 0:
          missing += missingPerson
          # print(missing)

  # outputIntList(soluces, fout)
  # outputStrList(soluces, fout)
  # outputStr(soluce, fout)
  outputInt(missing, fout)

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

def readStrList(fin):
  return list(fin.readline().rstrip('\n').split(' '))

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
