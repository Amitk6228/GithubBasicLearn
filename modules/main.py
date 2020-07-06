# print("Hello World")

# def func():
#     print("Hello") 

# func() 

# file import method--
#...
# import calc
# print(calc.add(1,2))
# print(calc.mul(1,2))
# print(calc.div(4,2))
# print(calc.sub(5,2))

# a= calc.A()
# print(type(a))

#....

# or in selective approach we can write---
#....
from calc import add 
#.......
# now here only add operation is filetered from calc.py

print(add(1,2))

#but this way is not usually prefered bcoz is not explicit
# so ----#import calc--- is always a good method for future purpose

#topic- Aliases
#....
# import calc as lib 
#....
#...or 2nd way as filtered method...
# from calc import {
#    add as addition,
#    sub as difference,
# } 
# now these addition and difference will work as a alaises for specific features
#....
# print(addition(1,2))
# print(difference(1,2))
#....
#- now this line will work as a aliases which means even if module named "calc"
#gets matched with any word in present code that will not create a problem is the program




