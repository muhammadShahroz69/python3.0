class Employee:
    
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id
        print("Employee Created")
        print("Name:", self.name)
        print("Employee ID:", self.emp_id)

    def work(self):
        print(self.name, "is working")

    def __del__(self):
        print("Employee Deleted")
        print(self.name, "has left the company")


# creating object
emp1 = Employee("Obito", 101)

# calling method
emp1.work()

# deleting object
del emp1
