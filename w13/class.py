class Dog(object):
    def __init__(self,name):
        name="dog"
        sound="mung mung"
    def bark(self):
        print self.sound

        
class Sichu(Dog):
    name="Sichu"
    sound="si si"

class Martis(Dog):
    name="Martis"
    sound="Mai Mai"

dog2=Sichu("Max")
dog3=Martis("Crikat")
dog2.bark()
dog3.bark()