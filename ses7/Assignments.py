prefix = 'from property'
class Car:
    def __init__(self, make, model, bhp, mph):
        self.make = make
        self.model = model
        self.bhp = bhp
        self.mph = mph

    # make property(getter) & setter
    @property # property itys called but works as a getter but in the code same syntax as without privvate.
    def make(self):
        return self.__make +  " " + prefix 

    @make.setter # It's set here as a private, but the syntax is still d1 = ... and then the constructor grabs this setter method cause its a property
    def make(self, make): # also called decorated the @x.setter
        self.__make = make

    # model property(getter) & setter
    @property 
    def model(self):
        return self.__model
    
    @model.setter 
    def model(self, model): 
        self.__model = model

    # bhp property(getter) & setter
    @property 
    def bhp(self):
        return self.__bhp

    @bhp.setter 
    def bhp(self, bhp): 
        self.__bhp = bhp

    # mph property(getter) & setter
    @property 
    def mph(self):
        return self.__mph

    @mph.setter 
    def mph(self, mph): 
        self.__mph = mph 

    # ToString methods, str for user firendly output and repr for the object output kind of for the programmer
    def __str__(self):
        return str("Make: " + self.make + "\nModel: " + self.model + "\nBHP: " + self.bhp + "\nMPH: " + str(self.mph))
    
    def __repr__(self):
        return f'{self.__dict__}' # f string, variable in a string

Citroen = Car('Sebber', 'C1', 'What dis?', 400)
Mercedes = Car('Mercedes', 'AMG C 63 S', 'Que?', 510)

print(str(Citroen))
print()
print(str(Mercedes))
print(Mercedes.make)
