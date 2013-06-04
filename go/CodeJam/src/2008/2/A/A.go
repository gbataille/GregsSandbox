/*
 * Lots of duplication, there are smarter less verbose way to write it
 * comparing the value searched to the current gate (0 or 1) for example
 * but anyway, I don't have the patience to clean it up
 * I'm a bit sad I can't do better/faster in one go though
 */
package main

import (
  "gxbUtils";
  "strconv";
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
  _, problems := gxbUtilsOld.ReadInputFileWithVariablePbSizesInAnArray(filename, headerLines, 1, 0)
  solutions := make([][]string, len(problems), len(problems))

  for i := 0; i < len(problems); i++ {
    solutions[i] = handleCase(problems[i])
  }

  gxbUtilsOld.OutputResults(solutions, filename)
  fmt.Println("-- Done")
}

func handleCase(pb [][]string) []string {
  // nbNodes, _ := strconv.Atoi(pb[0][0])
  targetValue, _ := strconv.Atoi(pb[0][1])
  nodes := pb[1:]

  cost := make([]int, len(nodes), len(nodes))

  for i:=len(nodes) - 1; i >= 0; i-- {
    if targetValue == 0 {
      updateCostFor0(cost, nodes, i)
    } else {
      updateCostFor1(cost, nodes, i)
    }
  }

  var result string
  if cost[0] == -1 {
    result = "IMPOSSIBLE"
  } else {
    result = strconv.Itoa(cost[0])
  }

  return []string{result}
}

func updateCostFor0(cost []int, nodes [][]string, index int) {
  //if it hasn't any child nodes
  if 2*index + 2 > len(nodes) {
    if nodes[index][0] == "0" {
      cost[index] = 0
    } else {
      cost[index] = -1
    }
  } else {
    minCost := 9999999
    //logic will depend on the current gate and its ability to mutate
    //child node are 2index+1 and 2index+2
    if nodes[index][0] == "0" {
      //OR gate -- both must be 0
      if cost[2*index+1] != -1 && cost[2*index+2] != -1 {
        minCost = cost[2*index+1] + cost[2*index+2]
      }
    } else {
      //AND gate -- one child node must be zero
      minCost = assignIfSmallerAndNotMinusOne(minCost, cost[2*index+1], 0)
      minCost = assignIfSmallerAndNotMinusOne(minCost, cost[2*index+2], 0)
    }
    if nodes[index][1] == "1" {
      //attempt with changing the gate
      if nodes[index][0] == "1" {
        //OR gate
        if cost[2*index+1] != -1 && cost[2*index+2] != -1 {
          minCost = assignIfSmallerAndNotMinusOne(minCost, cost[2*index+1] + cost[2*index+2], 1)
        }
      } else {
        //AND gate -- both child node must be zero
        minCost = assignIfSmallerAndNotMinusOne(minCost, cost[2*index+1], 1)
        minCost = assignIfSmallerAndNotMinusOne(minCost, cost[2*index+2], 1)
      }
    }

    if minCost == 9999999 {
      //we haven't got a solution to make this node 0
      minCost = -1
    }
    cost[index] = minCost
  }
}

func updateCostFor1(cost []int, nodes [][]string, index int) {
  //if it hasn't any child nodes
  if 2*index + 2 > len(nodes) {
    if nodes[index][0] == "1" {
      cost[index] = 0
    } else {
      cost[index] = -1
    }
  } else {
    minCost := 9999999
    //logic will depend on the current gate and its ability to mutate
    //child node are 2index+1 and 2index+2
    if nodes[index][0] == "1" {
      //AND gate -- both child node must be zero
      if cost[2*index+1] != -1 && cost[2*index+2] != -1 {
        minCost = cost[2*index+1] + cost[2*index+2]
      }
    } else {
      //OR gate
      minCost = assignIfSmallerAndNotMinusOne(minCost, cost[2*index+1], 0)
      minCost = assignIfSmallerAndNotMinusOne(minCost, cost[2*index+2], 0)
    }
    if nodes[index][1] == "1" {
      //attempt with changing the gate
      if nodes[index][0] == "0" {
        //AND gate -- both child node must be zero
        if cost[2*index+1] != -1 && cost[2*index+2] != -1 {
          minCost = assignIfSmallerAndNotMinusOne(minCost, cost[2*index+1] + cost[2*index+2], 1)
        }
      } else {
        //OR gate
        minCost = assignIfSmallerAndNotMinusOne(minCost, cost[2*index+1], 1)
        minCost = assignIfSmallerAndNotMinusOne(minCost, cost[2*index+2], 1)
      }
    }

    if minCost == 9999999 {
      //we haven't got a solution to make this node 0
      minCost = -1
    }
    cost[index] = minCost
  }
}

func assignIfSmallerAndNotMinusOne(target int, newValue int, offset int) int {
  if newValue == -1 {
    return target
  } else {
    if newValue + offset < target {
      return newValue + offset
    } else {
      return target
    }
  }
}
