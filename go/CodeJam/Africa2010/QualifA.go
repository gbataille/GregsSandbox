package main
import (
  "fmt";
  "bufio";
  "strconv";
  // "io";
  "os"
)

func main() {
  args := os.Args
  //Display help
  if len(args) != 2 {
    manual()
    return
  }

  filename := args[1]
  headerLines := 1
  caseSize := 3

  _, cases := readInputFile(filename, headerLines, caseSize)

  fmt.Println(cases)
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
  fmt.Println("Just pass the input filename as an argument")
}
