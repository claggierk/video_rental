#!/bin/bash

pythonNumLines=0
for i in *.py; do pythonNumLines=$(($pythonNumLines+$(cat $i | wc -l))); done
echo "python lines: $pythonNumLines"
