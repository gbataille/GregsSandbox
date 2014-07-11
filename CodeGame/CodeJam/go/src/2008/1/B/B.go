package main

import (
  "gxbUtilsOld";
  "strconv";
  "strings";
  // "math";
  "fmt"
)

func main() {
  // CONFIG TO DO EVERY TIME
  const headerLines int   = 1
  const caseSize int      = 3
  const caseSizeIndex int = 2

  fmt.Println("-- Start")
  filename := gxbUtilsOld.SetupEnv()
  // _, problems := gxbUtilsOld.ReadInputFile(filename, headerLines, caseSize)
  _, problems := gxbUtilsOld.ReadInputFileWithVariablePbSizes(filename, headerLines, caseSizeIndex)
  solutions := make([][]string, len(problems), len(problems))

  for i := 0; i < len(problems); i++ {
    solutions[i] = handleCase(problems[i])
  }

  return
  gxbUtilsOld.OutputResults(solutions, filename)
  fmt.Println("-- Done")
}

func handleCase(pb []string) []string {
  nbMilkshake, _ := strconv.Atoi(pb[0])
  nbClients, _ := strconv.Atoi(pb[1])
  clientsTaste := make([][]int, nbClients, nbClients)
  for i := 0; i < nbClients; i++ {
    clientTasteString := strings.Split(pb[2+i], " ")
    clientTaste := make([]int, len(clientTasteString), len(clientTasteString))
    for j := 0; j < len(clientTasteString); j++ {
      clientTaste[j], _ = strconv.Atoi(clientTasteString[j])
    }
    clientsTaste[i] = clientTaste
  }
  popularity := make([]int, nbMilkshake*2, nbMilkshake*2)
  for i := 0; i < nbMilkshake*2; i++ {
    popularity[i] = 0
  }
  for i := 0; i < nbClients; i++ {
    for j := 1; j <= clientsTaste[i][0]; j++ {
      offset := 0
      if clientsTaste[i][j*2] == 1 {
        offset = nbMilkshake
      }
      fmt.Println(clientsTaste)
      fmt.Println(i)
      fmt.Println(j)
      popularity[clientsTaste[i][j*2-1] + offset - 1] += 1
    }
  }

  fmt.Println(popularity)
  return nil
}
