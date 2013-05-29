package main

import (
  "gxbUtils";
  "strconv";
  "strings";
  "sort"
)

func main() {
  // CONFIG TO DO EVERY TIME
  headerLines := 1
  caseSize := 3
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
  nbValues, _ := strconv.Atoi(pb[0])
  xstring := strings.Split(pb[1], " ")
  ystring := strings.Split(pb[2], " ")
  x := make([]int, nbValues, nbValues)
  y := make([]int, nbValues, nbValues)
  i := 0
  for i < nbValues {
    x[i], _ = strconv.Atoi(xstring[i])
    y[i], _ = strconv.Atoi(ystring[i])
    i += 1
  }
  sort.IntSlice(x).Sort()
  sort.IntSlice(y).Sort()

  i = 0
  product := 0
  for i < len(y) {
    // yinv[i] = y[len(y)-1-i]
    product += x[i]*y[len(y) - 1 - i]
    i += 1
  }

  sval := strconv.Itoa(product)
  return []string{sval}
}
