package main
import (
  "fmt";
  "bufio";
  "strconv";
  "strings";
  // "io";
  "os"
)

func main() {
  args := os.Args
  //Display help
  if len(args) != 3 {
    manual()
    return
  }

  filename := args[1]
  outputFile := args[2]
  headerLines := 1
  caseSize := 3

  _, cases := readInputFile(filename, headerLines, caseSize)
  solutions := make([][]int, len(cases), len(cases))

  i := 0
  for i < len(cases) {
    budget, _ := strconv.Atoi(cases[i][0])
    numObjects, _ := strconv.Atoi(cases[i][1])
    articles := strings.Split(cases[i][2], " ")
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
            solutions[i] = []int{j+1, l+j+2}
          }
          l += 1
        }
      }

      j += 1
    }

    i += 1
  }

  outputResults(solutions, outputFile)
}

func outputResults(results [][]int, outputFile string) {
  fo, err := os.Create(outputFile)
  if err != nil {
    panic(err)
  }
  defer func() {
    err := fo.Close()
    if err != nil {
      panic(err)
    }
  }()

  w := bufio.NewWriter(fo)
  i := 0
  for i < len(results) {
    a := results[i][0]
    b := results[i][1]
    _, err = w.WriteString(
      fmt.Sprintf("Case #%d: %d %d\n", i+1, a, b))
    if err != nil {
      panic(err)
    }

    i += 1
  }

  if err = w.Flush(); err != nil {
    panic(err)
  }
}

func readInputFile(filename string,  headerLines int, 
  caseSize int) (header []string, cases [][]string) {

  fi, err := os.Open(filename)
  if err != nil { panic(err) }
  // close fi on exit and check for its returned error
  defer func() {
    if err := fi.Close(); err != nil {
      panic(err)
    }
  }()

  s := bufio.NewScanner(bufio.NewReader(fi))

  // Parses the header
  i := 1
  for i <= headerLines {
    ok := s.Scan()
    if !ok {
      panic("cannot read file header\n")
    }
    header = append(header, s.Text())
    i += 1
  }

  nbCases, _ := strconv.Atoi(header[0])

  j := 0
  for j < nbCases {
    var curCase[]string
    k := 0
    for k < caseSize {
      ok := s.Scan()
      if !ok {
        fmt.Println(s.Text())
        panic(s.Err())
      }
      curCase= append(curCase, s.Text())
      k += 1
    }
    cases = append(cases, curCase)
    j += 1
  }

  return header, cases
}

func manual() {
  fmt.Println("Just pass the input filename as the first argument and the output file as the second")
}
