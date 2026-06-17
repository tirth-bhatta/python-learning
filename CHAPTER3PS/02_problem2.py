letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''

a= input("Enter your name: ")
b= input("Enter the date: ")
letter = letter.replace("<|Name|>",a).replace("<|Date|>", b)

print(letter)