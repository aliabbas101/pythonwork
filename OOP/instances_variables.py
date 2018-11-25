class Employee:
    raise_amount=1.04
    totalemp=0
    def __init__(self, first, last, pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first+last+'@wennovation.com'
        Employee.totalemp+=1
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    def apply_raise(self):
    	return str(int(self.pay * self.raise_amount))
    
emp_1=Employee('Ali','Rizvi',5000)
emp_2=Employee('John','Doe',5000)
emp_1.raise_amount=1.05;
print(emp_1.raise_amount)
print(emp_2.raise_amount)
print(Employee.totalemp)