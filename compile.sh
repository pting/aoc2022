#!/bin/bash

echo "Usage: compile.sh <myprog> (without .c or .py)"
python -m nuitka $1.py

if [ -e $1.c ]
then
    echo "gcc -O3 $1.c -o $1"
    gcc -O3 $1.c -o $1
fi

echo "Run: ./$1.bin and ./$1"