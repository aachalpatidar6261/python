class circle:
    def set(self,r):
        self.r=r

    def area(self):
        self.ar = 3.14*self.r*self.r
        
    def get(self):
        print("area of circle" ,self.ar)

c=circle()
c.set(2)
c.get()
