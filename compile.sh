#!/bin/sh

echo "Usage: compile.sh <myprog>.py"
python -m nuitka $1
