s = {8, 7, 12, "Harry", [1,2]} # Sets cannot contain lists because lists are mutable (unhashable)

s[4][0]= 9  # So this code will raise TypeError