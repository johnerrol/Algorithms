class Person:
    def __init__(self,Name,isMale):
        self.Name=Name
        if (isMale==True):
            self.sex="Male"
        else:
            self.sex="Famale"
    def show(self):
           print("%s is %s" %(self.Name,self.sex))
ListOfPerson=[]
ListOfPerson.append(Person("Alice",False))
ListOfPerson.append(Person("Bob",True))
ListOfPerson.append(Person("Carol",False))
ListOfMale=[]
ListOfFemale=[]
for person in ListOfPerson:
    if (person.sex=="Male"):
        ListOfMale.append(person)
    else:
        ListOfFemale.append(person)
print("")
print("Males:")
for male in ListOfMale:
    male.show()

print("")
print("Females:")
for female in ListOfFemale:
    female.show()


    
