#! python3
class Employee:
    def __init__(self, firstName, lastName, wage, position):
        self.firstName = firstName
        self.lastName = lastName
        self.wage = wage
        self.position = position

    def __str__(self) -> str:
        return f"{self.firstName} {self.lastName}"
    
    def job(self):
        return f"{self.firstName} is the {self.position}"
    
    def salary(self):
        return f"{self.firstName} is paid Ksh {self.wage} per month"


emp_1 = Employee('John', 'Doe', 40000, 'sales manager')

print(emp_1)
print(emp_1.job())
print(emp_1.salary())


