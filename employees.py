class Employee:
    def __init__(self, Ename, EGender, EPay):
        self.name = Ename
        self.gender = EGender
        self.pay = EPay
    
    def salary(self):
        # salary based on hours worked
        pass

    def show_detail(self):
        print(f"{self.name}, is {self.gender}, and has a salary of {self.pay}")


employee1 = Employee("Nonk", "Male", "9000")

hours = int(input("Enter number of hours"))
allowance = int(input("Enter allowance"))
fSalary = hours * allowance + employee1.salary()
print(f"Final Salary equals : {fSalary}")


employee1.show_detail()
