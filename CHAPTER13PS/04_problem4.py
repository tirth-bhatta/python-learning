def divisibles(n):
    if(n%5==0):
        return True
    return False

a = [1, 2, 34234, 53, 748385, 65, 877, 45, 55]

f = list(filter(divisibles, a))
print(f)