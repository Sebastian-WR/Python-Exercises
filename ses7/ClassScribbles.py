class P:
   def __init__(self, name, alias):
      self.name = name       # public
      self.__alias = alias   # private

   def who(self):
      print('name  : ', self.name)
      print('alias : ', self.__alias)

p = P('Sebber', 'Serberen')
print(p.who())

class D: # Not often that it's nescesarry to make private fields in Python the pythonic way is that it is oublic and easy acceseble
    def __init__(self, x):
        self.x = x # public variable so the client side doesnt change d1.x = .... but its private behind it with the annotations

    @property # property itys called but works as a getter but in the code same syntax as without privvate.
    def x(self):
        return self.__x

    @x.setter # It's set here as a private, but the syntax is still d1 = ... and then the constructor grabs this setter method cause its a property
    def x(self, x): # also called decorated the @x.setter
        if x > 1000:
            self.__x = 1000
        elif x < 0:
            self.__x = 0
        else:
            self.__x = x
    
    def __str__(self):
        return str(self.x)
    
    def __repr__(self):
        return f'{self.__dict__}' # f string, variable in a string

d1 = D(3)
d2 = D(1003)
d1.x = d1.x + d2.x
print(d1.x)
print(d1)
print(str(d1))
print(repr(d1))

      # docker run -it --rm -v ${PWD}:/docs python bash
      # python -i ClassScribbles.py i'et betyder at man åbner det i interpreter 