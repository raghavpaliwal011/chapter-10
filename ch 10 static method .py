class employee :    
    company = "Google"
    def getsalary(self, signature):
        print(f"salary for this employee workingin {self.company} is {self.salary}\n{signature}")
    @staticmethod
    def greet():
        print ("good morning ,sir")


raghav = employee()
raghav.salary = 100000
raghav.getsalary("thanks!")
raghav.greet()