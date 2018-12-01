# container.py
# Dec. 27, 2016

class container:
    def __init__(self, contType, color, capacity):
        self.contType = contType
        self.capacity = capacity
        
    def FillC(self, volumeOther):
        FullC = "Your " + str(self.contType) + " cannot take any more."
        a = self.room - volumeOther
        if a < 0:
            return FullC
        else:
            self.room = a

    def RemoveC(self, volumeOther):
        EmptyC = "Your " + str(self.contType) + " is empty."
        a = self.room + volumeOther
        if self.capacity >= a > 0:
            self.room = a
        else:
            self.room = self.capacity
            return EmptyC
            
class backpack(container):
    def __init__(self, contType="Backpack", color="Grey", capacity=1000):
        self.contType = contType
        self.color = color
        self.capacity = capacity
        self.room = capacity

class barrel(container):
    def __init__(self, contType="Barrel", color="Black", capacity=4000):
        self.contType = contType
        self.color = color
        self.capacity = capacity
        self.room = capacity

class chest(container):
    def __init__(self, contType="Chest", color="Red", capacity=12000):
        self.contType = contType
        self.color = color
        self.capacity = capacity
        self.room = capacity

class flask(container):
    def __init__(self, contType="Flask", color="Clear", capacity=100):
        self.contType = contType
        self.color = color
        self.capacity = capacity
        self.room = capacity

class pouch(container):
    def __init__(self, contType="Pouch", color="White", capacity=200):
        self.contType = contType
        self.color = color
        self.capacity = capacity
        self.room = capacity

class vial(container):
    def __init__(self, contType="Vial", color="Green", capacity=10):
        self.contType = contType
        self.color = color
        self.capacity = capacity
        self.room = capacity

