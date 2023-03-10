class student:
    def __init__(self,name,enroll):
        self.name=name
        self.enroll=enroll
        
    def getinfo(self):
        print("your name is : ",self.name)
        print("your enrol is : ",self.enroll)
        
class est(student):
          
    def get_est(self,py,java):
        self.py=py
        self.java=java
        
class mst(student):
    def __init__(self,name,enroll):
         super().__init__(name,enroll)

         
    def get_mst(self,py1,java1):
        self.py1=py1
        self.java1=java1
 
        

        
class rs(est,mst):
    def __init__(self,name,enroll):
        super().__init__(name,enroll)

     
    def finalresult(self):  
        super().getinfo()   
        self.py=self.py+self.py1
        self.fjava=self.java+self.java1
        print(f" Final java marks :{self.fjava}")
        print(f" Final java marks :{self.py}")


        
nidhi=rs("nidhi",123)
nidhi.get_mst(23,21)
nidhi.get_est(45,54)
nidhi.finalresult()
