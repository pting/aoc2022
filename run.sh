#!/bin/bash
#set -ex

pip install -r requirements.txt

for f in $(find . -name "day*.py")
do
  echo "attempting to run $f"
  time python $f
  echo ""
done
