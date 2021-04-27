from time import sleep
# Callable
def add(x, y):
    return x + y

print(add(1,2))

print(callable(add)) # Det er en metode så returner true kan ikke burges på tværs af klasser i samme fil

class Add:
    def __call__(self, x, y):
        return x + y
add1 = Add()
print(callable(add1))

# Generators & Iterators class

def compute():
    list = []
    for i in range(10):
       # sleep(.5)
        list.append(i)
    return list

print(compute())

list1 = [1, 2, 3, 4, 5]
for i in list1:
    print(i)

li = iter(list1)
print(next(li))
print(next(li))

class Compute: # Generator class
    def __iter__(self): # always self in class method
        self.last = 0 # the last value i have looke at
        return self

    def __next__(self):
        if self.last >= 10:
            raise StopIteration()
        self.last += 1
        return self.last

compute1 = Compute()
ic = iter(compute1)
for i in compute1:
    print(i)
    print(next(ic)) # next element method forstår ikke helt ideen, skulle komme hver gang man kalder men virker ikke altså +1

# Generator functions (generator object) yields and doesnt returns anything
def compute_x():
    for i in range(10):
        yield i # seems as the same as return? but its different yields 1 element and keeps track

x = compute_x()
print(next(x))

# Generator expressions similiar to list comprehensions
list = [i for i in range(10)] # list comprehension
print(list)

gen_expr = (i for i in range(10)) # generator expresson
print(next(gen_expr))
