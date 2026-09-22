d = {}

name = input("Enter the name : ") 
lang = input("Enter the language : ")
d.update({name : lang})

name = input("Enter the name : ")
lang = input("Enter the language : ")
d.update({name : lang}) # Same name

print(d) # Update the last value in key