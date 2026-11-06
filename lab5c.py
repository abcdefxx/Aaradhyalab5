#!/usr/bin/env python3
# Author:Aaradhya Shrestha
# Date:2026-11-05
# Purpose: Process File data.
# Usage: ./lab5c.py

with open("rhyme.txt", "w") as dataFile :
  dataFile.write("I made myself a snowball\nAs perfect as could be.\nI thought I'd keep it as a pet\nAnd let it sleep with me.")
f= open("rhyme.txt", "r")
line = f.readline()
while line != '':
  line= line.strip().strip('.')
  words = line.split()
  print(line, '---', len(words), 'words')
  line = f.readline()
f.close()
