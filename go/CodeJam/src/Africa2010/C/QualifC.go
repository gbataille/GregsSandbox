package main

import (
  "gxbUtils";
  "strings"
)

func main() {
  // CONFIG TO DO EVERY TIME
  headerLines := 1
  caseSize := 1

  filename := gxbUtils.SetupEnv()

  _, problems := gxbUtils.ReadInputFile(filename, headerLines, caseSize)
  solutions := make([][]string, len(problems), len(problems))

  i := 0
  for i < len(problems) {
    solutions[i] = handleCase(problems[i])
    i += 1
  }

  gxbUtils.OutputResults(solutions, filename)
}

func handleCase(pb []string) []string {
  var letters map[uint8]string
  letters = make(map[uint8]string)
  letters["a"[0]] = "2"
  letters["b"[0]] = "22"
  letters["c"[0]] = "222"
  letters["d"[0]] = "3"
  letters["e"[0]] = "33"
  letters["f"[0]] = "333"
  letters["g"[0]] = "4"
  letters["h"[0]] = "44"
  letters["i"[0]] = "444"
  letters["j"[0]] = "5"
  letters["k"[0]] = "55"
  letters["l"[0]] = "555"
  letters["m"[0]] = "6"
  letters["n"[0]] = "66"
  letters["o"[0]] = "666"
  letters["p"[0]] = "7"
  letters["q"[0]] = "77"
  letters["r"[0]] = "777"
  letters["s"[0]] = "7777"
  letters["t"[0]] = "8"
  letters["u"[0]] = "88"
  letters["v"[0]] = "888"
  letters["w"[0]] = "9"
  letters["x"[0]] = "99"
  letters["y"[0]] = "999"
  letters["z"[0]] = "9999"
  letters[" "[0]] = "0"

  lineToTranslate := pb[0]
  translatedLine := make([]string, len(lineToTranslate), len(lineToTranslate)*5)

  i := 0
  var previousLetter uint8
  previousLetter = 0

  for i < len(lineToTranslate) {
    letter := letters[lineToTranslate[i]]

    if letter[0] == previousLetter {
      letter = " " + letter
    }
    translatedLine[i] = letter

    previousLetter = letter[len(letter) - 1]
    i += 1
  }

  return []string{strings.Join(translatedLine, "")}
}
