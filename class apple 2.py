class Apple:
    def __init__(self,Color):
        self.Color=Color

        
ListOfApples=[Apple("Red"),Apple("Red"),Apple("Green"),Apple("Red" ),Apple("Red"),Apple("Green")]

for apple in ListOfApples:
      print("This apple is %s" % (apple.Color))
              
