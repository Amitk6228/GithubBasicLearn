#it uses yield
def print_fancy_name(prefix):
    try:
        while True:
            name:(yield)
            print(prefix + ":"+name)
    except GeneratorExit:
        print("Done !") 
co = print_fancy_name("Cool")
#initialization
next(co)
#sending data and control
co.send("Amit")
co.send("Kumar")     
co.close()  