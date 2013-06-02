/*
 * After some time I found a solution that seems to be right.
 * I did not implement it successfully and this is partly due to the fact
 * that I attempted several things and the code starts to be messed up.
 * I'll change a bit my Google Code Jam toolbox library and I'll restart
 * fram scratch, timed, to see how I do starting with a known solution
 */
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

  fmt.Println("-- Start")
  filename := gxbUtilsOld.SetupEnv()
  _, problems := gxbUtilsOld.ReadInputFileWithVariablePbSizesInAnArray(filename, headerLines, 1, 1)
  solutions := make([][]string, len(problems), len(problems))

  for i := 0; i < len(problems); i++ {
    solutions[i] = handleCase(problems[i])
  }

  gxbUtilsOld.OutputResults(solutions, filename)
  fmt.Println("-- Done")
}

func handleCase(pb []string) []string {
  header := strings.Split(pb[0], " ")
  nbNodes, _ := strconv.Atoi(header[0])
  desiredSolution, _ := strconv.Atoi(header[1])
  nbInternalNodes := (nbNodes - 1) / 2
  // nbLeaves := (nbNodes + 1) / 2
  //nodeDescriptor : [value, subTreeChangeable?, gateType?, changeable?]
  nodesDescriptor := make([][4]int, nbNodes, nbNodes)

  //Building the tree node descriptor structure.
  for i:=0; i < nbNodes; i++ {
    curNode := pb[1+i]
    if i < nbInternalNodes {
      nodeDesc := strings.Split(pb[1+i], " ")
      gate, _ := strconv.Atoi(nodeDesc[0])
      changeable, _ := strconv.Atoi(nodeDesc[1])
      nodesDescriptor[i] = [4]int{-1, -1, gate, changeable}
    } else {
      value, _ := strconv.Atoi(curNode)
      nodesDescriptor[i] = [4]int{value, 0, -1, 0}
    }
  }

  //Computing the current value of each node
  for i:=0; i < (nbNodes-1)/2; i++ {
    node1 := nbNodes - (2*i) - 1
    node2 := nbNodes - (2*i) - 1 - 1
    node1Value := nodesDescriptor[node1][0]
    node2Value := nodesDescriptor[node2][0]
    // if node1 <= nbInternalNodes {
    // }
    resultNode := node2 / 2
    operator := nodesDescriptor[resultNode][2]
    if operator == 1 {
      nodesDescriptor[resultNode][0] = node1Value & node2Value
    } else {
      nodesDescriptor[resultNode][0] = node1Value | node2Value
    }
    subtreeChangeable := nodesDescriptor[node1][1] | nodesDescriptor[node1][3] |
      nodesDescriptor[node2][1] | nodesDescriptor[node2][3]
    nodesDescriptor[resultNode][1] = subtreeChangeable

    //shortcut
    if ((nodesDescriptor[node1][0] == 1 &&
        nodesDescriptor[node2][0] == 1 ) ||
      (nodesDescriptor[node1][0] == 0 &&
        nodesDescriptor[node2][0] == 0)) &&
        nodesDescriptor[resultNode][1] == 0 {
      nodesDescriptor[resultNode][3] = 0
    }
  }

  fmt.Println("Desc")
  fmt.Println(nodesDescriptor)
  // from the bottom computing each value that a node can take, with the penalty incurred.
  penalty := make([][2]int, nbNodes)
  alt := [2]int{1,0}
  for i:=nbNodes; i > 0; i-- {
    node := nodesDescriptor[i-1]
    leftNodeIndex := i*2-1
    rightNodeIndex := i*2
    //the current value is free
    penalty[i-1][node[0]] = 0
    penalty[i-1][alt[node[0]]] = -1
    //changing this node if possible and not any other incurs a penalty of 1
    if node[3] == 1 {
      var res int
      if node[2] == 1 {
        res = nodesDescriptor[leftNodeIndex][0] | nodesDescriptor[rightNodeIndex][0]
      } else {
        res = nodesDescriptor[leftNodeIndex][0] & nodesDescriptor[rightNodeIndex][0]
      }
      if res == alt[node[0]] {
        penalty[i-1][alt[node[0]]] = 1
      }
    }
    //At this point, if we can change the node value for a penalty of 1, that's
    //clearly the minimum penalty, we can exit
    if penalty[i-1][alt[node[0]]] == -1 {
      possiblePenalty := 9999999999
      leftNode := nodesDescriptor[leftNodeIndex]
      rightNode := nodesDescriptor[rightNodeIndex]
      //Changing only left sub node value (with penalty) if possible
      if penalty[leftNodeIndex][alt[leftNode[0]]] != -1 {
        if test(node[2], alt[leftNode[0]], rightNode[0], alt[node[0]]) {
          possiblePenalty = penalty[leftNodeIndex][alt[leftNode[0]]]
        }
      }
      //Changing only the right sub node value
      if i == 1 {
        fmt.Println(penalty[rightNodeIndex][alt[rightNode[0]]])
        fmt.Println(node[2])
        fmt.Println(leftNode[0])
        fmt.Println(alt[rightNode[0]])
        fmt.Println(alt[node[0]])
        fmt.Println(test(node[2], leftNode[0], alt[rightNode[0]], alt[node[0]]))
      }
      newPenalty := penalty[rightNodeIndex][alt[rightNode[0]]]
      if newPenalty != -1 {
        if test(node[2], leftNode[0], alt[rightNode[0]], alt[node[0]]) {
          if newPenalty < possiblePenalty {
            possiblePenalty = newPenalty
          }
        }
      }

      //Changing both subnodes values
      newPenalty = penalty[rightNodeIndex][alt[rightNode[0]]] +
                    penalty[leftNodeIndex][alt[leftNode[0]]]
      if penalty[rightNodeIndex][alt[rightNode[0]]] != -1 &&
      penalty[leftNodeIndex][alt[leftNode[0]]] != -1 {
        if test(node[2], alt[leftNode[0]], alt[rightNode[0]], alt[node[0]]) {
          if newPenalty < possiblePenalty {
            possiblePenalty = newPenalty
          }
        }
      }

      //Changing the current node gate and the left subnode value
      newPenalty = penalty[leftNodeIndex][alt[leftNode[0]]] + 1
      if newPenalty != 0 {
        if test(alt[node[2]], alt[leftNode[0]], rightNode[0], alt[node[0]]) {
          if newPenalty < possiblePenalty {
            possiblePenalty = newPenalty
          }
        }
      }

      //Changing the current node gate and the right subnode value
      newPenalty = penalty[rightNodeIndex][alt[rightNode[0]]] + 1
      if newPenalty != 0 {
        if test(alt[node[2]], leftNode[0], alt[rightNode[0]], alt[node[0]]) {
          if newPenalty < possiblePenalty {
            possiblePenalty = newPenalty
          }
        }
      }

      //Changing the current node gate and both subnodes value
      newPenalty = penalty[rightNodeIndex][alt[rightNode[0]]] +
                    penalty[leftNodeIndex][alt[leftNode[0]]] + 1
      if penalty[rightNodeIndex][alt[rightNode[0]]] != -1 &&
      penalty[leftNodeIndex][alt[leftNode[0]]] != -1 {
        if test(alt[node[2]], alt[leftNode[0]], alt[rightNode[0]], alt[node[0]]) {
          if newPenalty < possiblePenalty {
            possiblePenalty = newPenalty
          }
        }
      }

      //if there is a possibility, stores the minimum penalty
      if possiblePenalty != 9999999999 {
        penalty[i-1][alt[node[0]]] = possiblePenalty
      }
    }
    fmt.Println(penalty)
  }

  var res string
  if penalty[0][desiredSolution] == -1 {
    res = "IMPOSSIBLE"
  } else {
    res = strconv.Itoa(penalty[0][desiredSolution])
  }
  return []string{res}
}

func test(gate int, node1 int, node2 int, expected int) bool {
  var comp int
  if gate == 0 {
    comp = node1 | node2
  } else {
    comp = node1 & node2
  }
  return comp == expected
}
