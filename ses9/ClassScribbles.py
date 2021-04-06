# docker run --rm -p 8888:8888 -v ${PWD}:/home/jovyan/work jupyter/datascience-notebook Laver et docker image med jupyter notebook som er en editor

# Exercise Small exercises 
from datetime import datetime
import time

def my_decorator(func):
    def wrapper(*args):
        log = open('time_log.txt', 'a')
        now = datetime.now()
        value = func(*args)
        log.write(f'{now}, {args}, {value}\n')

    return wrapper

@my_decorator
def add(*args):
    sum = 0
    for i in args:
         sum += i
    return sum

add(1, 2)
add(2, 3)

@my_decorator
def printer(text):
    return f'From printer: {text}\n'

printer('Hola')

# Exercise Time it!

def timeCode(func):
    def wrapper(*args):
        start = time.time()
        func(*args)
        end = time.time()
        print(end - start)
    return wrapper

@timeCode
def count(a, b):
    while a < b:
        a += 1
    return 'Done'

count(1, 1000)

#Exercise 3 Slow down code

def slowdown(func):
    def wrapper(*args):
        time.sleep(1)
        func(*args)
        #time.sleep(1)
    return wrapper

@slowdown
def countdown(n):
     if not n:   # 0 is false, not false is true
         return n
     else:
        print(n)
        #print(n, end=' ')
        return countdown(n-1) # call the same function with n as one less

countdown(5)