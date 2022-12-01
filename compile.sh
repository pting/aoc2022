#!/bin/sh

echo "Usage: compile.sh <myprog> (without .c or .py)"
python -m nuitka $1.py

gcc -O3 $1.c -o $1

echo "Run: ./$1.bin and ./$1"