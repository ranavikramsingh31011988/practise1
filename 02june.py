class Employee:



    def __init__(self, name, position):
        self.name = name  # Instance attribute
        self.position = position
    @classmethod

    def change_company(cls, new_company):



        cls.company = "ABC Corp"

        print(cls.company)

    def display_info(self):
        print(f"Employee: {self.name}, Position: {self.position}")

# Creating instances
employee1 = Employee("John", "Developer")
employee2 = Employee("Alice", "Manager")

# Displaying initial company (class-level data)
employee1.display_info()  # Output: Employee: John, Position: Developer, Company: ABC Corp
employee2.display_info()  # Output: Employee: Alice, Position: Manager, Company: ABC Corp

#Using the class method to change the company
Employee.change_company("XYZ Ltd")

# Displaying updated company (class-level data)
employee1.display_info()  # Output: Employee: John, Position: Developer, Company: XYZ Ltd
employee2.display_info()  # Output: Employee: Alice, Position: Manager, Company: XYZ Ltd
