/**
 * Add after a while one good intuition when expressing the result as
 * a + b*sqrt(5)
 * and describing an and bn recursively.
 * however to then optimize the computation and be able to use %1000 every step
 * of the way, expressing the transformation as a matrix would have been 
 * necessary which I clearly don't master.
 *
 * The following is incomplete and does not work
 */
package main

import (
  "gxbUtilsOld";
  "strconv";
  // "strings";
  "math";
  "fmt"
)

func main() {
  // s := (math.Trunc(math.Sqrt(5)*math.Pow(10,10)) + 1) / math.Pow(10,10)
  s := math.Sqrt(5)
  t := 31
  results := make([][4]uint64, t, t)
  results[0] = [4]uint64{1,0,0,0}
  results[1] = [4]uint64{3,0,1,0}
  for i := 2; i < t; i++ {
    a := results[i-1][0]
    b := results[i-1][1]
    c := results[i-1][2]
    d := results[i-1][3]

    ai := 3*a + 3000*b + 5*c + 5000*d
    ci := 3*c + 3000*d + a + 1000*b

    results[i] = [4]uint64{ai%1000, (ai/1000)%10000000000, ci%1000, (ci/1000)%10000000000}
  }

  // CONFIG TO DO EVERY TIME
  const headerLines int   = 1
  const caseSize int      = 1

  fmt.Println("-- Start")
  filename := gxbUtilsOld.SetupEnv()
  _, problems := gxbUtilsOld.ReadInputFile(filename, headerLines, caseSize)
  solutions := make([][]string, len(problems), len(problems))

  for i := 0; i < len(problems); i++ {
    solutions[i] = handleCase(problems[i], results, s)
  }

  gxbUtilsOld.OutputResults(solutions, filename)
  fmt.Println("-- Done")
}

func handleCase(pb []string, results [][4]uint64, s float64) []string {
  i, _ := strconv.Atoi(pb[0])
  a := results[i][0]
  c := results[i][2]
  d := results[i][3]

  soluce := uint64(math.Trunc(float64(a) + float64(c + 1000*d)*s)) % 1000
  stringSoluce := strconv.Itoa(int(soluce))
  for j := 0; j < 3 - len(stringSoluce); j++ {
    stringSoluce = "0" + stringSoluce
  }
  return []string{stringSoluce}
}
