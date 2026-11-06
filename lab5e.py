#!/usr/bin/env python3
# Author: aaradhya Shrestha
# Date: 2026-11-05
# Purpose: Handle FileNotFoundError
# Usage: ./lab4e.py

def add(number1, number2):
    try:
        return int(number1) + int(number2)
    except Exception as e:
        return str(e)    
def read_file(filename):
    f=None
    numbers = []
    try:
        f= open(filename, 'r')
        for line in f:
            numbers.append(int(line.strip()))
        return numbers   
    except OSError:
        return 'Error: could not open the file '+ filename
    except ValueError:
        return 'Error: could not convert the data in '+ filename + ' to an integer'
    finally:
        if f is not None:
            f.close()

def main():
    print(add(10,5))                        
    print(add('10',5))                      
    print(add('abc',5))                     
    print(read_file('file10000.txt'))       
    print(read_file('numbers.txt'))          
main()