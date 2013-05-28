package main

import (
  "gxbUtils"
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
  return nil
}
