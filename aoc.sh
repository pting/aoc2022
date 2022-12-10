#!/bin/bash
set -e

echo ""
echo "\033[36m"
if [ "$4" ]; then
    echo "Starting Week $4"
fi
echo "Running $1 \033[0m"
echo ""
python $1 $2
echo ""
echo "\033[36m============================= \033[0m"
echo ""
time python $1 $3
echo ""
