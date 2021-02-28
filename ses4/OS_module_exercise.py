# os_exercise.py
# Do the following task using the os module

#1. create a folder and name the folder 'os_exercises.'                                                  
#2. In that folder create a file. Name the file 'exercise.py'                                                                            
#3. get input from the console and write it to the file.                                                 
#4. repeat step 2 and 3 (name the file something else).                                                  
#5. read the content of the files and and print it to the console.

import os

os.mkdir('os_exercises')
folder = 'os_exercises'
os.chdir(folder)
open('exercise.py', 'w')
file = open('exercise.py', 'w')
print('Type somthing to write to the file!: ')
consInput = input()
file.write(consInput)
file = open('exercise.py')
print(file.readline())

