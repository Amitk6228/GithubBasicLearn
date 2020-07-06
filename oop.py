#Methods in Python
class Parrot:

    #instance attributes for class parrot
    def __init__(self, name , age):
        self.name=name
        self.age=age
    #instance methods    
    def sing(self,song):
        return "{} sings {}".format(self.name,song)

    def dance(self):
        return "{} was dancing".format(self.name)    

    def danceplus(self,dance):
        return "{} is now dancing {}".format(self.name,dance)
#instantiate the object
blu=Parrot("Blu",10)

#call our instance methods
print(blu.sing("Masakali"))
print(blu.dance())
print(blu.danceplus("hip-hop"))

