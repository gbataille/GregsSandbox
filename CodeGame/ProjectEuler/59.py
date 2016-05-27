#!/usr/local/bin/python3
from functools import reduce


def isSolution(text):
    the = text.count("the")
    spaces = text.count(" ")
    return (the > 3) and (spaces > 10)


def decrypt():
    encAsciiList = readEncFile()
    for i in range(0, 26):
        for j in range(0, 26):
            for k in range(0, 26):
                pwdStr = chr(i + 97) + chr(j + 97) + chr(k + 97)

                decAsciiList = applyPwd(pwdStr, encAsciiList)
                decStr = "".join(list(map(chr, decAsciiList)))
                if isSolution(decStr):
                    print(decStr)
                    asciiSum = reduce(
                        lambda x, y: x + y,
                        decAsciiList)
                    print(asciiSum)
                    return


def applyPwd(pwdStr, encAsciiList):
    decAsciiList = list(encAsciiList)
    pwdBytes = list(map(ord, list(pwdStr)))
    for i in range(0, len(encAsciiList)):
        pwdByteToApply = pwdBytes[(i + 1) % 3]
        decAsciiList[i] = int(encAsciiList[i]) ^ pwdByteToApply

    return decAsciiList


def readEncFile():
    f = open('input/p059_cipher.txt', 'r')
    text = f.read()
    text.replace('\n', '')
    return text.split(",")


def main():
    decrypt()


if __name__ == "__main__":
    main()
