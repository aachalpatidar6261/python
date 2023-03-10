class employe:
    def set(self,name,phone,salary):
        self.name=name
        self.phone=phone
        self.salary=salary

    def get(self):
        print("name : ", name)
        print("phone", phone)
        print("salary", salary)

em=employe()
em.set("rj",12345,25000)

        