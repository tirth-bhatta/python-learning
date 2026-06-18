a1 = int(input("Enter number 1: "))
a2 = int(input("Enter number 2: "))
a3 = int(input("Enter number 3: "))
a4 = int(input("Enter number 4: "))

nums = [a1, a2, a3, a4]
mx = max(nums)

print("Greatest number is:", mx)

print("It appears in:")
if a1 == mx:
    print("a1")
if a2 == mx:
    print("a2")
if a3 == mx:
    print("a3")
if a4 == mx:
    print("a4")