# Designed Class for Lab Assignment 3.4 - THE COMBINATION LOCK

class ComboLock :
    def __init__(self, secret1=16, secret2=1, secret3=27):
        self.secret1 = secret1
        self.secret2 = secret2
        self.secret3 = secret3
    
    def ComboLock(self):
        return self.secret1, self.secret2, self.secret3

    def reset(self):
        return 0
        
    def turnLeft(self, ticks):
        return -ticks
        
    def turnRight(self, ticks):
        return ticks

    def open(self):
        print("The lock is now open!")

