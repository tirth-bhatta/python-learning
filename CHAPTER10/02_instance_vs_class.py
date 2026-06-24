class Employee:
    language = "Python" # this is a class attribute
    salary = 1200000


tirth = Employee()
tirth.language = "JavaScript" # this is an object/instance attribute
print( tirth.language, tirth.salary)