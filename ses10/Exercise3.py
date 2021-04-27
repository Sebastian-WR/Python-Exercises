class RangeClone:
    def __init__(self,startInt,endInt):
        self.startInt = startInt
        self.endInt = endInt
        self.last = startInt
    
    def __iter__(self):
        return self
    
    def __next__(self):
        rv = self.last
        if self.last <= self.endInt:
            self.last += 1
        if self.last > self.endInt:
            raise StopIteration
        return rv

rc = RangeClone(0,10)
test = iter(rc)

# print(next(test))
# print(next(test))

# for i in test:
#     print(next(test))

for i in rc:
    print(i)

