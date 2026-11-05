#!/usr/bin/env python3
# Author: Aaradhya Shrestha
# Date:2026-11-05
# Purpose: Read a text file.
# Usage: ./lab5a.py
 
def read_file_lineByLine(file_name):
    with open(file_name,'r') as f:
        for line in f:
            print(line.rstrip('\n'))
def read_file_list(file_name):
    lines= []
    with open(file_name, 'r') as f:
        for line in f:
            lines.append(line.rstrip('\n'))
    return lines
def main():
    file_name= 'data2.txt'
    read_file_lineByLine(file_name)
    print(read_file_list(file_name))
main()        