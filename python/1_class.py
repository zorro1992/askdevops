# Define a  software engineer set

se1=["Raghu","Software Engineer",20,"Junior",5000]
se2=["Ram","Data Engineer",25,"Senior",8000]

# But you can see this is repeating variable declaration everytime which is not scalable

# Creating a engineer class
class Engineer:

    # Class attributes
    alias = "Major Programmers"

    def __init__(self,name,role,age,stage,salary):
        # instance attributes 
        self.name = name
        self.role = role
        self.age = age
        self.stage = stage
        self.salary = salary

# Instance
se1=Engineer("Raghu","Software Engineer",20,"Junior",5000)
print("Name of the engineer is " + se1.name + " and the role is " + se1.role + " and current salary " + str(se1.salary))
print(se1.alias)

# Instance
se2=Engineer("Ram","Data Engineer",25,"Senior",8000)
print("Name of the engineer is " + se2.name + " and the role is " + se2.role + " and current salary " + str(se2.salary) + " role is " + se2.alias)

# Exercise
# Create a class called BankFD. It should have account number, FD amount, Nominee 
