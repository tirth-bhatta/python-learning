class Employee:
    name = "Tirth"
    language = "py" # this is a class attribute
    salary = 1200000


tirth = Employee()
tirth.name = "Tirth" # this is an object/instance attribute
print(tirth.name, tirth.language, tirth.salary)

rohan = Employee()
rohan.name = "Rohan"
print(rohan.name,rohan.salary, rohan.language)

# Here name is object/instance attribute and salary and language
# are class attributes as they directly belong to the class