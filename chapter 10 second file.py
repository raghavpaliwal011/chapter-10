class Employee:
    company = "google"
    salary = 100
raghav = Employee()
deepti = Employee()
print (raghav.company)
print (deepti.company)
raghav.salary ="500"
deepti.salary ="600"
Employee.company = "isro"
print (raghav.company)
print (deepti.company)
print (raghav.salary)
print (deepti.salary)