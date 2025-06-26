class Employee():
    def __init__(self, name, age, role):
        self.name = name
        self.age = age
        self.role = role

class EmployeeManager():
    def __init__(self, name, employees: list[Employee], roles: list[str]):
        self.name = name
        self.employees = employees
        self.roles = roles

    def add_employee(self, employee: Employee):
        self.employees.append(employee)
        print(f"Added employee: {employee.name}")

    def remove_employee(self, employee: str):
        emp = list(filter(lambda x: x.name == employee, self.employees))[0]
        if emp:
            self.employees.remove(emp)

    def promote(self, name: str):
        emp = list(filter(lambda x: x.name == name, self.employees))[0]
        if emp:
            current_role = self.roles.index(emp.role)
            if current_role == len(self.roles)-1:
                print("Employee is already at highest position")
            else:
                self.employees.remove(emp)
                emp.role = self.roles[current_role+1]
                self.employees.append(emp)
        else:
            print("Employee not found")
        
    def demote(self, name: str):
        emp = list(filter(lambda x: x.name == name, self.employees))[0]
        if emp:
            current_role = self.roles.index(emp.role)
            if current_role==0:
                print("Employee is already at lowest position")
            else:
                self.employees.remove(emp)
                emp.role = self.roles[current_role-1]
                self.employees.append(emp)
        else:
            print("Employee not found")

    def display_employees(self):
        for employee in self.employees:
            print(f"Name: {employee.name}\tAge: {employee.age}\tRole: {employee.role}")
        print("--------------------------")

rishi = Employee("rishi", 25, "Junior")
john = Employee("john", 28, "Senior")
jayne = Employee("jayne", 45, "Manager")

company = EmployeeManager("company", roles=["Junior", "Senior", "Manager", "Board of Directors"], employees=[rishi, john, jayne])
company.display_employees()
company.demote("john")
company.display_employees()
company.promote('rishi')
company.display_employees()
company.demote("jayne")
company.display_employees()
company.promote("rishi")
company.display_employees()