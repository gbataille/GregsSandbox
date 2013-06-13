package main

import (
  "gxbUtils";
  // "strconv";
  // "strings";
  // "math";
  "fmt"
)

func main() {
  // CONFIG TO DO EVERY TIME
  const headerLines int   = 1
  const caseSize int      = 3

  fmt.Println("-- Start")
  filename := gxbUtilsOld.SetupEnv()
  _, problems := gxbUtilsOld.ReadInputFile(filename, headerLines, caseSize)
  solutions := make([][]string, len(problems), len(problems))

  for i := 0; i < len(problems); i++ {
    solutions[i] = handleCase(problems[i])
  }

  gxbUtilsOld.OutputResults(solutions, filename)
  fmt.Println("-- Done")
}

func handleCase(pb [][]string) []string {
  return nil
}
