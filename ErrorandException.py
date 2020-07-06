#Example of try except block
def div(a,b):
    try:
        print(a/b)
    except :
        print("Error !")
    print("Executed")     
div(10,0)    #--will give error-- 

#Zero Division Error
def div2(a,b):
    try:
        print(a/b)
    except ZeroDivisionError:
        print("Error : You were trying to divide by zero")
    print("Executed")     
div2(10,0) 

#Value Error
try:
    a=int("Amit")
except ZeroDivisionError:
    print("Error : You were trying to divide by zero")
except ValueError:
    print("Value Error Occured")  

#Universal statement for finding Error
try:
    print(10/0)
except Exception as e:
    print(type(e)) #Zero division Error

#creating Custom Error and Exceptions
#-raise statement
try:
    raise Exception("My Custom Error")
except Exception as e:
    print(e)

#my Exception class
#Exception- base exception class
class MyException(Exception):
    def __init__(self,message):
        self.message=message
    def __str__(self):
        return self.message
try:
    raise MyException("some Error")
except Exception as e:
    print(e)  
#----------# 
print("------smarter way-----")

#Smarter way for writing Error and Exception-
# else:will always exceute if the try block didn't threw any error
# finally:will always execute

try:
    print("Hello world")
    print(10/0)
except:
    print("Ok error occured")
else:
    print("Woah")
finally:
    #cleanup code or exiting code
    print("bye bye world")

#----Trick question asked in interview----
print("------Trick Question------")
def func():
    try:
        return 1
    except:
        return 2 
    else:
        return 3 
    finally:
        return 4
#so here -
# > finally block will always be executed whether at any condition
# > else block will only be executed when try block fails

#-----with statement----
print("------with statement------")         
 

        







      



