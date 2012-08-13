class Apple:
    def __init__(self,Color):
        self.Color=Color

        
ListOfApples=[Apple("Red"),Apple("Red"),Apple("Green"),Apple("Red" ),Apple("Red"),Apple("Green")]
for apple in ListOfApples:
      print("This apple is %s" % (apple.Color))
              
              
Dataset=[Apple("Red"),Apple("Red"),Apple("Green"),Apple("Red" ),Apple("Red"),Apple("Green")]
IndexToSwap1=0
IndexToSwap2=2

temp=Dataset[IndexToSwap1]
Dataset[IndexToSwap1]=Dataset[IndexToSwap2]
Dataset[IndexToSwap2]=temp



print(ListOfApples)
