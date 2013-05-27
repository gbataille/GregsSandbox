package main

import (
  "gxbUtils";
  "strings";
  "strconv"
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
  budget, _ := strconv.Atoi(pb[0])
  numObjects, _ := strconv.Atoi(pb[1])
  articles := strings.Split(pb[2], " ")
  prices := make([]int, len(articles), len(articles))
  k := 0
  for k < len(articles) {
    prices[k], _ = strconv.Atoi(articles[k])
    k += 1
  }
  j := 0

  for j < numObjects {
    curObj := prices[j]
    if curObj < budget {
      subPrices := prices[j+1:]
      l := 0
      for l < len(subPrices) {
        if curObj + subPrices[l] == budget {
          return []string{strconv.Itoa(j+1), strconv.Itoa(l+j+2)}
        }
        l += 1
      }
    }

    j += 1
  }

  // If we reach here, we have not found the solution
  return nil
}
