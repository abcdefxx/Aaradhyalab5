#!/usr/bin/env python3
# Author:Aaradhya Shrestha  
# Date: 2026-11-05
# Purpose: Process File data.
# Usage: ./lab5d.py

statements_path= 'pythonStatements.txt'
machine_path= 'machineCode.txt'
output_path= 'output.txt'
statements_file = open(statements_path, 'r')
machine_file=open(machine_path, 'r')
output_file= open(output_path, 'w')
statement= statements_file.readline()
code = machine_file.readline()
while statement != '' and code != '':
    statement =statement.split('#')[0].strip()
    code= code.strip()
    output_file.write(statement + '\t' + code + '\n')
    print (statement + '\t' + code)
    statement = statements_file.readline()
    code= machine_file.readline()
statements_file.close()
machine_file.close()
output_file.close()
print("output.txt has been created")