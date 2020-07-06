

# s=input()
# s=s.title()
# print(s) 

# n = int(input())
# arr = map(int, input().split()) 

# for i in range (1,6):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()    
        
# i=0
# while i<5:
#     print(i)
#     i+=i
#     if i==3:
#         break
# else:
#     print(0)

# n=5
# sum=0
# for i in range(1,n+1):
#     sum=sum+(i*i)/i
# print(sum)    

#to find K th largest element in array 
# part -1 with sort
#  a=[]
# n=int(input())
# for i in range(0,n):
# 	ele=int(input())
# 	a.append(ele) 
# k=int(input())
# a.sort()
# print(a[k+1]) 

# without sort and using max function
# a=[]
# n=int(input())
# for i in range(0,n):
# 	ele=int(input())
# 	a.append(ele) 
# k=int(input())
# for i in range(k-1):
# 	z=max(a)
# 	while max(a)==z:
# 		a.remove(max(a))
# print(max(a)) 

# n=int(input())
# a=[]
# for i in range(0,n):
# 	ele=int(input().split())
# 	a.append(ele)
# print(a)
# total=sum(a)
# print(total)
# s=input()
# a=list(s)
# i=1
# while(i<len(a)):
# 	if(a[i]==a[i-1]):
# 		a.remove(a[i])
# 	i+=1
# b=''.join(str(x)for x in a)		
# print(b)		
	
 
#ewfew
#


#DCB problem
# if((2 not in a) and (5 not in a)):
# 	a.sort()
# 	c=0
# 	for i in range(1,len(a)):
# 		if(a[i]==a[i-1]):
# 			d=0
# 		else:
# 			c=c+1
# 	stdout.write(str(c+1))
# elif(5 in a):
# 	a.sort()
# 	c=0
# 	for i in range(1,len(a)):
# 		if(a[i]==a[i-1]):
# 			continue
# 		else:
# 			c=c+1
# 	stdout.write(str(c))
# else:
# 	a.sort()
# 	c=0
# 	for i in range(1,len(a)):
# 		if(a[i]==a[i-1]):
# 			continue
# 		else:
# 			c=c+1
# 	stdout.write(str(c)) 

# print(5//3) 
# print('Coding'+'Blocks')
# print(str.find('o'))

# t=('Tanya', 'ate' , '3', 'apples')
# print(t[0])
# string=' I study Python '
# print(string[3:9]) 

#To Reverse a string
# string='I study Python at Coding Blocks'
# print(string[::-1])

# string='I study Python at Coding Blocks'
# print(string[0:9:2]) 

# string='I study Python'
# string[2]='Z'
# string[7]='-'  
# a=[4,8,9,0]
# print(a*2) 

# while 5==5:
#    print("CODING BLOCKS") 
# i = sum = 0

# while i <= 4:
#   sum += i
#   i = i+1

# print(sum) 


# self written program for finding mutiples of K with Q queries
# n=int(input("Enter n:"))
# counter=0
# a=[]
# for i in range(0,n):
# 	ele=int(input())
# 	a.append(ele) 
# print(a)
# q=int(input("enter q:"))
# k=[]
# for j in range(0,q):
# 	num=int(input())
# 	k.append(num)
# print(k)	
# for i in range(0,len(a)):
# 	for j in range(0,len(k)):
# 		if(a[i]%k[j]==0):
# 			counter=counter+1
# print(counter)		




# geek for geek method 
# Python3 program to calculate all multiples 
# of integer 'k' in array[] 

# ans is global array so that both countSieve() 
# and countMultiples() can access it. 
# ans = [] 

# # Function to pre-calculate all multiples 
# # of array elements 
# # Here, the arguments are as follows 
# # a: given array 
# # n: length of given array 
# def countSieve(arr, n): 
	
# 	MAX=max(arr) 

# # Accessing the global array in the function 
# 	global ans 

# # Initializing "ans" array with zeros 
# 	ans = [0]*(MAX + 1) 

# # Initializing "cnt" array with zeros 
# 	cnt = [0]*(MAX + 1) 

# #Store the arr[] elements as index in cnt[] array 
# 	for i in range(n): 
# 		cnt[arr[i]] += 1

# # Iterate over all multiples as 'i' 
# # and keep the count of array[] ( In 
# # cnt[] array) elements in ans[] array 
# 	for i in range(1, MAX+1): 
# 		for j in range(i, MAX+1, i): 
# 			ans[i] += cnt[j] 

# def countMultiples(k): 
# # Return pre-calculated result 
# 	return(ans[k]) 

# Driver code 

# n=int(input())
# a=[]
# count=0
# for i in range(n):
# 	j=int(input())
# 	a.append(j)
# countSieve(a,n)
# q=int(input())
# k=[]
# for i in range(q):
# 	c=int(input())
# 	k.append(c)
# i=0
# for i in k:
# 	print(countMultiples(i))

# ans=[]  


#DCB 10-march program - to find sum of two arrays 

# n=int(input("Size of 1st array: "))
# a=[int(n)for n in input().split()]
# print(a)
# m=int(input("size of 2nd array: "))
# b=[int(number)for number in input().split()]
# print(b)
# c=[]
# for i in range(0,len(a)):
#     for j in range(0,len(b)):
#         c=a[i]+b[j]
    
# print(c)    


#program to find lcm
# x=int(input())
# y=int(input())

# if(x>y):
# 	high=x
# else:
# 	high=y

# while(1):
# 	if((high%x==0)and(high%y==0)):
# 		lcm=high
# 		break
# 	high +=1 
# print(lcm) 

#program to find permutations with k swapes
# n,k = map(int, input().split())
# arr=[int(number)for number in input().split()]  
# def KswapPermutation(arr, n, k): 
  
    
#     pos = {} 
#     for i in range(n): 
#         pos[arr[i]] = i 
  
#     for i in range(n): 
  
#         if k == 0: 
#             break
  
#         if (arr[i] == n-i): 
#             continue
  
#         temp = pos[n-i] 
#         pos[arr[i]] = pos[n-i] 
#         pos[n-i] = i 
#         arr[temp], arr[i] = arr[i], arr[temp] 
  
#         k = k-1

# KswapPermutation(arr,n,k)
# print(" ".join(map(str,arr))) 

# program to send all zeros in the last
# n=int(input())
# a=[]
# for i in range(0,n):
#     ele=int(input())
#     a.append(ele)
# a.sort(reverse=True)
# print(*a)  #to print array without brackets and comma

#program to count no. of scholarships
# bool possible(ll n,ll m, ll x,ll y, ll ans)
# {
#     if((ans*x) <= m + (n-ans)*y)
#     return true;
#     else return false;
# }
# ll binary_search(ll n,ll m, ll x,ll y)
# {  ll ans=0, s=0, e=n;// Corrected
#     while(s<=e)
#     {
# 		ll mid=(s+e)/2;
        
#         if(possible(n,m,x,y,mid))
#         {ans=max(mid,ans);
#         s=mid+1;}
#        else
#         e=mid-1;
#     }
# return ans;
# }
# int main() {
#     ll n, m ,x,y, a[10000000],i;
#      cin>>n>>m>>x>>y;
#      //for(i=0;i<n;i++)
#      //a[i]=i+1;
#     cout<<binary_search(n,m,x,y);
# 	return 0;
#}  

#merge sort
# n=int(input())
# arr=[int(n)for n in input().split()]
# arr.sort()
# print(*arr) #to print array without brackets and comma 

#kickstart
# T=int(input("No of test case :"))
# for i in range(T):
#     N ,B=map(int,input().split())
#     arr=[int(N)for N in input("Enter array:").split()] 
#     arr.sort()
#     print(arr)
#     counter=0
#     i=0;j=N-1
#     while(i<j):
#         if(arr[i]+arr[j]<=B):
#             counter+=(j-1)
#             i+=1
#         else:
#             j-=1        
                        
#     print(counter) 

# T=int(input())
# p=[]
# h=[]
# for i in range(T):
#     b=[]
#     n,m=map(int,input().split())
#     p.append(m)
#     b=[int(x)for x in input().split()]
#     b.sort()
#     h.append(b)
# for i in range(T):
#     s=0
#     count=0
#     for j in range(len(h[i])):
#         if((s+h[i][j])>p[i]):
#             print("case #{}: {}".format(i+1,count))
#             break
#         else:
#             s=s+h[i][j]
#             count=count+1 
#  for i in range(0,N):
#         for j in range(N-1):
#             if(arr[i]+arr[j]<=B):
#                 counter+=(j-1)
#                 i+=1
#             else:
#                 j-=1  

#dcb 27/3/20
# def maxProduct(arr, n): 
	
# 	minVal = arr[0] 
# 	maxVal = arr[0] 
#     maxProduct = arr[0] 

# 	for i in range(1, n): 
# 		if (arr[i] < 0): 
# 			temp = maxVal 
# 			maxVal = minVal 
# 			minVal = temp 
# 		maxVal = max(arr[i], maxVal * arr[i]) 
# 		minVal = min(arr[i], minVal * arr[i]) 
#         maxProduct = max(maxProduct, maxVal) 

# 	return maxProduct 

# num=int(input())
# arr=[int(num)for num in input().split()]
# n=len(arr)
# print(maxProduct(arr, n)) 

#dcb 28/3/20
# a=input()
# b=input()
# if (b in a) and (len(a)!= len(b)):
# 	print("Yes")
# else:
# 	print("No")	

#vowels & consonents
# s="javascriptloops"
# vowels="aeiou"
# consonents=" "
# for i in range(len(s)):
#     for j in range(len(vowels)):
#         if s[i]==vowels[j]:
#             print(s[i])
#         else:
#             consonents=consonents+s[i]
# print(consonents) 

# #nested list
# marksheet = []
# z=[]
# for _ in range(0,int(input())):
#     marksheet.append([input(), float(input())])  
# marksheet.sort()
# print(marksheet)
# z=min(marksheet) 
# print(z)   


# second_highest = sorted(list(set([marks for name, marks in marksheet])))[1]
# print('\n'.join([a for a,b in sorted(marksheet) if b == second_highest]))

#finding percentage of query
#   n = int(input())
#     student_marks = {}
#     for _ in range(n):
#         name, *line = input().split()
#         scores = list(map(float, line))
#         student_marks[name] = scores
#     query_name = input()
#     query_scores = student_marks[query_name] 
#     print("{0:.2f}".format(sum(query_scores)/3))

#hackerrank 30/3
# meal_cost = float(input())
# tip_percent = int(input())
# tip=meal_cost*(tip_percent/100)
# tax_percent = int(input())
# tax=meal_cost*(tax_percent/100)
# totalCost=meal_cost+tip+tax
# print(round(totalCost))
# arr=[1,5,6,7,9]
# # while(1):
#     # i,e= [int(x) for x in input("Enter two value: ").split()]
# e=int(input())
# arr.remove(e)
# arr.reverse()
# print(arr)

# N = int(input())
# arr=[]
# op=input()
# while(1):
#     if(op=="insert"):
#         insert()
#     elif(op=="print"):
#         printf()
#     elif(op=="remove"):
#         removef()
#     elif(op=="append"):
#         appendf()
#     elif(op=="sort"):
#         sortf()
#     elif(op=="pop"):
#         popf()
#     elif(op=="reverse"):
#         reversef()
#     else:
#         print("no output")


# def insert():
#     i,e= [int(x) for x in input("Enter two value: ").split()]
#     arr.insert(i,e)
# def printf():
#     print(arr)
# def removef():
#     e=int(input())
#     arr.remove(e) 
# def appendf():
#     e=int(input())
#     arr.append(e) 
# def sortf():
#     arr.sort()
# def popf():
#     arr.pop()
# def reversef():
#     arr.reverse() 

#finding count of string in a whole string
# def printStr(s) : 
  
#     i = 0
#     while( i < len(s) - 1) : 
#         count = 1
#         while s[i] == s[i + 1] : 
#             i += 1
#             count += 1
#             if i + 1 == len(s): 
#                 break
#         print("({}, {})".format(str(count),str(s[i])), end=" ")

#         i += 1
#     print()
# s=input()    
# a=(1,2,3,4)
# del a
# print(a)
# d={"john":40,"peter":45} 
# # print(d["john"])
# print(list(d.keys())) 

#to check property of n - HR
#  n = int(input())
#     if((n % 2 == 1) or ((n % 2 == 0) and (n >=6 and n <= 20))):
#         print("Weird")

#     else:
#         print("Not Weird") 

#to convert lower to upper and vice versa
# s= input()
# print(s.swapcase()) 

#to split a string
# a=input()
# print("-".join(a.split())) 

#minion game 
# def minion_game(string):
#     # your code goes here
#     v='AEIOU'
#     stu=0
#     kev=0
#     for i in range(len(s)):
#         if s[i] in v:
#             kev=kev+(len(s)-i)
#         else:
#             stu=stu+(len(s)-i)
#     if kev>stu:
#         print("Kevin",kev)
#     elif kev<stu:
#         print("Stuart",stu)
#     else:
#         print("Draw")  
#     return minion_game
# s = input()
#     minion_game(s)   

#splitting the string in multiples of k
# def merge_the_tools(string, k):
    
#     subst=''
#     for i in range(0,len(string)):
#         if string[i] not in subst:
#             subst=subst+string[i]  
#         if (i+1)%k==0:
#             print(subst)
#             subst=''

# string, k = input(), int(input())
# merge_the_tools(string, k)  

#for checking condition using "all" & "any" function in python
# n = int(input())

# arr = input().split(" ")

# print(all(int(i)>=0 for i in arr) and any(i == i[::-1]for i in arr)) 

#for split out the string in odd and even
# t=int(input())
# for i in range(t):
#     s=input()  
#     print(s[::2], s[1::2])  
# s=input()

#using dictionary
# n = int(input())
# d = {}
# for i in range(n):
#     x = input().split()
#     d[x[0]] = x[1]
# while True:
#     try:
#         name = input()
#         if name in d:
#             print(name, "=", d[name], sep="")
#         else : print("Not found")   
#     except: break 

#to check prime using recurssion
# def Prime(n, i = 2): 

 
# 	if (n < 2): 
# 		return False 
# 	if (n % i == 0): 
# 		return False
# 	if (i * i > n)or(n==2): 
# 		return True 

# 	return Prime(n, i + 1) 
# n = int(input())
# if (Prime(n)): 
# 	print("Yes, It's a Prime Number") 
# else: 
# 	print("No, It's not a Prime Number")  

#to check if substring present or not 
# def check(string, sub_str): 
#     if (string.find(sub_str) == -1): 
#         print("NO,It's Not Present") 
#     else: 
#         print("YES,It's Present") 
            
# string = input()
# sub_string =input()
# if (string.find(sub_string) == -1): 
#     print("NO,It's Not Present") 
# else: 
#     print("YES,It's Present") 
  

# Program to generate a random number
# import random
# list=[]
# for i in range(0,20):
#     r=random.randint(0,20)
#     list.append(r)
# print(list)

# program to print numbers not divisible
# for i in range(1, 101):
#     if i % 3 != 0 and i % 5 != 0:
#         print("{}".format(i),end=" ")  

#compute n+nn+nn
# n=int(input())
# a=n+(n*n)+(n*n*n)
# print(a) 

#decimal to binary
# n= int(input())
# print(bin(n).split('1'))
# n = int(input().strip())
# print(max(len(length) for length in bin(n)[2:].split('0'))) 

# open website using python
# import webbrowser as wb 
# wb.open('https://www.google.com/') 

#time delay
# import time
# time.sleep(200)

#window shutdown
# import os
# os.system('shutdown -s') 

#inheritance program
# class Person:
# 	def __init__(self, firstName, lastName, idNumber):
# 		self.firstName = firstName
# 		self.lastName = lastName
# 		self.idNumber = idNumber
# 	def printPerson(self):
# 		print("Name:", self.lastName + ",", self.firstName)
# 		print("ID:", self.idNumber)

# class Student(Person,object):
   
#     def __init__(self, firstName, lastName, idNumber, scores):
#         super().__init__(firstName, lastName, idNumber)
#         self.scores = scores
#     def calculate(self):
#         iAvg = sum(self.scores)/len(self.scores)
#         return 'O' if iAvg > 89 else 'E' if iAvg > 79 else 'A' if iAvg > 69 else 'P' if iAvg > 54 else 'D' if iAvg > 39 else 'T'
# line = input().split() 
# firstName = line[0]
# lastName = line[1]
# idNum = line[2]
# numScores = int(input()) 
# scores = list( map(int, input().split()) )
# s = Student(firstName, lastName, idNum, scores)
# s.printPerson()
# print("Grade:", s.calculate())  

#bubble sort
# n = int(input().strip())
# a = list(map(int, input().strip().split(' ')))
# count = 0
# is_sorted = False
# while not is_sorted:
#     is_sorted = True
#     i = 0
#     for i in range(0, len(a)):
#         if i < len(a) - 1:
#             if a[i] > a[i+1]:
#                 a[i], a[i+1] = a[i+1], a[i]
#                 is_sorted = False
#                 count += 1

# print('Array is sorted in {} swaps.'.format(count))
# print('First Element: {}'.format(a[0]))
# print('Last Element: {}'.format(a[len(a)-1])) 

#BST in python and finding length of the node
# class Node:
#     def __init__(self,data):
#         self.right=self.left=None
#         self.data = data
# class Solution:
#     def insert(self,root,data):
#         if root==None:
#             return Node(data)
#         else:
#             if data<=root.data:
#                 cur=self.insert(root.left,data)
#                 root.left=cur
#             else:
#                 cur=self.insert(root.right,data)
#                 root.right=cur
#         return root

#     def getHeight(self,root):
       
#         if root:
#             leftDepth = self.getHeight(root.left)
#             rightDepth = self.getHeight(root.right)
#             if leftDepth > rightDepth:
#                 return leftDepth + 1
#             else: 
#                 return rightDepth + 1
#         else:
#             return -1

# T=int(input())
# myTree=Solution()
# root=None
# for i in range(T):
#     data=int(input())
#     root=myTree.insert(root,data)
# height=myTree.getHeight(root)
# print(height)    

# n=int(input())
# l=[]
# for i in range(n):
#     ele=int(input())
#     l.append(ele)
# print(l[9:8:1])

# list=[-5,-3,0,3,6]
# print([x*2 for x in list])
# print([x for x in list if x>=0])

# lm,lcm=[int(lm) for lm in input("Enter two length in m and cm : ").split()]
# cm=((lm*100)+lcm)
# print( "length in cm is",cm,"cm")

#print name from email in a regular expression from database
# import math
# import os
# import random
# import re
# import sys
# l=[]
# n=int(input())
# for i in range(0,n):
#     firstName,emailId=[str(s) for s in input().split()]
#     if re.search('@gmail\.com$',emailId):
#         l.append(firstName)
# print(*sorted(l),sep='\n')


  
	


	
 















                       






          






    







           










       



    

    
 





 




	


