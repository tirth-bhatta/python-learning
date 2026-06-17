marks={
    "Harry": 100,
    "Shubham": 56,
    "Rohan": 23,
    0: "Tirth"
}

# print(marks.items())
# print(marks.keys())
# print(marks.values())
# marks.update({"Harry": 99, "Renuka": 100})
# print(marks)

print(marks.get("Harry2")) # prints None if the key is not found, instead of throwing an error
print(marks["Harry2"]) # throws an error if the key is not found, instead of printing None


