#!/bin/bash
set -e

echo ""
echo "#############################"
echo "####   Running Week $1   ####"
echo "#############################"
echo ""
python day$1.py test$1.txt
echo ""
echo "  ========================="
echo ""
python day$1.py input$1.txt
