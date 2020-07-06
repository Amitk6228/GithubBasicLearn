# Comprehension methods-total 3 methods
# List Comprehension method  
listCom= [i**2 for i in range (10) if i%2==0]
print(listCom)

# Dict Comprehension method 
dictCom= { i:i**2 for i in range(10) if i%2==0}
print(dictCom)

# Dict-2 Comprehension method 
dictCom2= { i**2 for i in range(10) if i%2==0}
print(dictCom2)


