#!/usr/local/bin/python3
import sys

def readCase(fin):
  ldn = readIntList(fin)
  L = ldn[0]
  D = ldn[1]
  N = ldn[2]
  words = []
  tests = []
  for i in range(0, D):
    words.append(readStr(fin))
  for i in range(0, N):
    tests.append(readStr(fin))
  return (L, D, N, words, tests)

def handleCase(caseNum, fin, fout):

  ########## Code Here ###########

  L, D, N, words, tests = readCase(fin)

  for i in range(0, N):
    fout.write("Case #%d: " % (i+1))
    num = 0
    for j in range(0, D):
      if isWordValid(words[j], tests[i], L):
        num += 1

    outputInt(num, fout)
    fout.write("\n")
  # outputIntList(soluces, fout)
  # outputStrList(soluces, fout)
  # outputStr(soluce, fout)
  # outputInt(soluce, fout)

  ################################

  return

def isWordValid(word, pattern, L):
  tokens = tokenize(pattern, L)
  valid = True
  lword = list(word)
  for i in range(0, L):
    if tokens[i].find(word[i]) == -1:
      valid = False
      break

  return valid

  return tokens

def tokenize(pattern, L):
  lPattern = list(pattern)
  tokens = []
  for i in range(0, L):
    firstChar = lPattern.pop(0)
    if firstChar == '(':
      par = lPattern.index(')')
      patt = lPattern[0:par]
      tokens.append(''.join(patt))
      lPattern = lPattern[par+1:]
    else:
      tokens.append(firstChar)

  return tokens




###############################################################
## Boiler Plate
###############################################################


def main(argv = None):
  pbName = __file__[1 + __file__.rfind("/"):__file__.rfind(".")]

  if argv is None:
    argv = sys.argv

  fin = open(pbName + '.in', 'r')
  fout = open(pbName + '.out', 'w')

  # nbCases = int(fin.readline())
  #
  # for caseNum in range(1, nbCases + 1):
  #   handleCase(caseNum, fin, fout)

  handleCase(0, fin, fout)

  fin.close()
  fout.close()

def readInt(fin):
  return int(fin.readline())

def readIntList(fin):
  return list(map(int, fin.readline().rstrip('\n').split(' ')))

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
