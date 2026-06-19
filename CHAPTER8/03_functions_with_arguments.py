# Function with parameters
def goodDay(name, ending):
    print("Good Day, " + name)
    print(ending)

# Calling the function with different arguments
goodDay("Tirth", "Thank you")
goodDay("Harry", "Thank you")
goodDay("Divya", "Thanks")


# Function with a return value
def goodDay(name, ending):
    print("Good Day, " + name)
    print(ending)
    return "ok"

# Store the returned value in a variable
a = goodDay("Tirth", "Thank you")

# Print the returned value
print(a)