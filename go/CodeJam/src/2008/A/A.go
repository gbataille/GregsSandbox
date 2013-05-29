package main

import (
  "gxbUtils";
  "strconv";
  "strings";
  "sort"
)

func main() {
  // CONFIG TO DO EVERY TIME
  const headerLines int   = 1
  const caseSize int      = 3

  filename := gxbUtils.SetupEnv()

  _, problems := gxbUtils.ReadInputFile(filename, headerLines, caseSize)
  solutions := make([][]string, len(problems), len(problems))

  for i := 0; i < len(problems); i++ {
    solutions[i] = handleCase(problems[i])
  }

  gxbUtils.OutputResults(solutions, filename)
}

func handleCase(pb []string) []string {
  nbValues, _ := strconv.Atoi(pb[0])
  xstring := strings.Split(pb[1], " ")
  ystring := strings.Split(pb[2], " ")
  x := make([]int, nbValues, nbValues)
  y := make([]int, nbValues, nbValues)
  for i := 0; i < nbValues; i++ {
    x[i], _ = strconv.Atoi(xstring[i])
    y[i], _ = strconv.Atoi(ystring[i])
  }
  sort.IntSlice(x).Sort()
  sort.IntSlice(y).Sort()

  product := 0
  for i := 0; i < len(y); i++ {
    product += x[i]*y[len(y) - 1 - i]
  }

  return []string{strconv.Itoa(product)}
}
