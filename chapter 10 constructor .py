#whta is this??

class employee :    
    company = "Google"

    def __init__(self, name , salary, subunit):
        self.name = name
        self.salary = salary
        self.subunit = subunit
        print("employee is created!")

    def getdetails(self):
        print("the name of the employee is {self.name}")
        print("the salary of the employee is {self.salary}")
        print("the subunit of the employee is {self.subunit}")
    company = "Google"
    def getsalary(self, signature):
        print(f"salary for this employee workingin {self.company} is {self.salary}\n{signature}")
    @staticmethod
    def greet():
        print ("good morning ,sir")
    def getsalary(self, signature):
        print(f"salary for this employee workingin {self.company} is {self.salary}\n{signature}")
    @staticmethod
    def greet():
        print ("good morning ,sir")

    @staticmethod
    def time():
        print("the time is 9 am in the morning")

raghav = employee("raghav",100,"youtube")
raghav.getdetails()