#!/bin/sh
if [ "$#" -ne "2" ]; then
  echo "Usage: testRun.sh go_program_path.go input_filename_without_suffix\n"
  exit 1
fi

INPUT="$2.in"
OUTPUT="$2.out"
SOLUCE="$2_correct.out"
go run $1 $INPUT && diff $OUTPUT $SOLUCE
