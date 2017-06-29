class Person:
    def __init__(self, hair, eyes , arms ):
        self.hair = hair
        self.eyes = eyes
        self.arms = arms
    
    def printer(self):
        print(self.hair, self.eyes, self.arms)
        
Andre = Person("brown", "brown", "long")
Andre.printer()


import turtle
