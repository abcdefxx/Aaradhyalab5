# Add comments before you do anything else.
#!/usr/bin/env python3
# Author:Aaradhya Shrestha
# Date:2026-11-5
# Purpose: Catch ZeroDivisionError
# Usage: ./lab5f.py

def safe_divide(a,b):
  try:
    if b==0:
      raise ZeroDivisionError ('cannot divide ' + str(a) + ' by zero')
    result= a/b
    print(a, '/', b, '=', result)
    return result
  except ZeroDivisionError as e:
    print('Error: ', e)

def main():
  safe_divide(10,5)  
  safe_divide(10,0)
main()  
