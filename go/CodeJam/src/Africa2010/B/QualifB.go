package main

import (
  "gxbUtilsOld";
  "strings"
)

func main() {
  // CONFIG TO DO EVERY TIME
  headerLines := 1
  caseSize := 1

  filename := gxbUtilsOld.SetupEnv()

  _, problems := gxbUtilsOld.ReadInputFile(filename, headerLines, caseSize)
  solutions := make([][]string, len(problems), len(problems))

  i := 0
  for i < len(problems) {
    solutions[i] = handleCase(problems[i])
    i += 1
  }

  gxbUtilsOld.OutputResults(solutions, filename)
}

func handleCase(pb []string) []string {
  lineToInvert := pb[0]
  token := strings.Split(lineToInvert, " ")
  invertedList := make([]string, len(token), len(token))
  i := 0
  for i < len(invertedList) / 2 {
    invertedList[i] = token[len(token)-i-1]
    invertedList[len(token)-i-1] = token[i]

    i += 1
  }
  if len(invertedList) % 2 == 1 {
    invertedList[len(invertedList)/2] = token[len(invertedList)/2]
  }

  return invertedList
}
