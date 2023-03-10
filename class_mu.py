class student:
    university="Mandsaur university"

    def set(self,name,rollno):
        self.name=name
        self.rollno=rollno

    def get(self):
        print("name : ",self.name)
        print("rollno", self.rollno)
        print(self.university)
    
s=student()
s.set("ram", 1)
s.get()

s1=student()
s1.set("sham", 2)
s1.get()

s2=student()
s2.set("abc", 3)
s2.get()