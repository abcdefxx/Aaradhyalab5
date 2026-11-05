# Add comments before you do anything else.
#!/usr/bin/env python3
# Author:Aaradhya Shrestha
# Date:2026-11-05
# Purpose: Write data to a file.
# Usage: ./lab5b.py

f = open('fruits.txt', 'w')
f.write('1. Apples are crunchy.\n2. Oranges are sweet, sour and juicy.\n3. Strawberries are sweet.\n4. Which fruit do you like?')
f.close()
print("file fruits.txt has been created")
print("Reading the file fruits.txt")
f=open ('fruits.txt', 'r')
line= f.readline()
while line != '':
        print(line.rstrip('\n'))
        line = f.readline()
f.close()