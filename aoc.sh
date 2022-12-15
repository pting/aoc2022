#!/bin/bash
set -e

echo ""
echo "\033[36m"
if [ "$4" ]; then
    echo "Starting Week $4"
fi
echo "Running $1"
echo ""
echo "test.txt:"
echo "\033[0m"
python $1 $2
echo ""
echo "\033[36m============================="
echo ""
echo "input.txt:"
echo " \033[0m"
time python $1 $3
echo ""
