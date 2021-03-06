package gxbUtilsOld

import (
  "fmt";
  "bufio";
  "strconv";
  "strings";
  "os"
)

func SetupEnv() string {
  args := os.Args
  //Display help
  if len(args) != 2 {
    manual()
    return ""
  }

  return args[1]
}

func OutputResults(results [][]string, inputFilePath string) {
  outputFile := strings.TrimSuffix(inputFilePath, ".in") + ".out"
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
    //Use a simple join!
    format := "Case #%d: %s\n"
    _, err = w.WriteString(
      fmt.Sprintf(format, i+1, strings.Join(results[i], " ")))
    if err != nil {
      panic(err)
    }

    i += 1
  }

  if err = w.Flush(); err != nil {
    panic(err)
  }
}

func ReadInputFile(filename string,  headerLines int, 
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

func ReadInputFileWithVariablePbSizesInAnArray(
  filename string,  headerLines int, caseSizeIndex int, 
  caseSizeIndexInArray int) (header []string, cases [][]string) {

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

  for j := 0; j < nbCases; j++ {
    var curCase[]string
    for k := 0; k < caseSizeIndex; k++ {
      ok := s.Scan()
      if !ok {
        panic(s.Err())
      }
      curCase= append(curCase, s.Text())
    }
    // We have reached the place where we know how many more lines there is to parse
    lineWithCaseSize := strings.Split(curCase[caseSizeIndex-1], " ")
    caseSize, _ := strconv.Atoi(lineWithCaseSize[caseSizeIndexInArray - 1])
    for k := 0; k < caseSize; k++ {
      ok := s.Scan()
      if !ok {
        panic(s.Err())
      }
      curCase= append(curCase, s.Text())
    }
    cases = append(cases, curCase)
  }

  return header, cases
}
func ReadInputFileWithVariablePbSizes(filename string,  headerLines int, 
  caseSizeIndex int) (header []string, cases [][]string) {

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

  for j := 0; j < nbCases; j++ {
    var curCase[]string
    for k := 0; k < caseSizeIndex; k++ {
      ok := s.Scan()
      if !ok {
        panic(s.Err())
      }
      curCase= append(curCase, s.Text())
    }
    // We have reached the place where we know how many more lines there is to parse
    caseSize, _ := strconv.Atoi(curCase[caseSizeIndex-1])
    for k := 0; k < caseSize; k++ {
      ok := s.Scan()
      if !ok {
        panic(s.Err())
      }
      curCase= append(curCase, s.Text())
    }
    cases = append(cases, curCase)
  }

  return header, cases
}
func manual() {
  fmt.Println("Just pass the input filename as the first argument")
}
