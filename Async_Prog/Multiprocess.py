from multiprocessing import Process

def showSquare(num = 2):
    print(num ** 2)
procss=[]

for i in range(5):
    procss.append(Process(target=showSquare,args=(i+1,)))

for proc in procss:
    proc.start()
print("Hello")

# for proc in procss:
#     proc.join() 
