#----AFTER 2:50:00------------------------
#--------for loop questions

#prerequiste
#range( start, end, step). --> end is compulsary 


#q1-- print hello world n times

"""n= int(input("Enter n"))

for i in range(1,n+1,1):
    print( f"{i}_hello world")
"""

#q2---reverse for loop print from n to 1

"""n=int(input("Enter n : ")) 

for i in range(n,0,-1):
    print (i)"""


#q4 take a no and print it's table 
"""n=int(input("Enter n : ")) 

for i in range(n,10*n+1,n):
    print(i)
"""

#q5  sum upto n terms

n=int(input("Enter n : ")) 
"""
sum =0
for i in range(1,n+1,1):
    sum=sum+i

print(sum)

"""

#q6 factorial of num

a=0
b=1






#q7  print all the factors of number

"""for i in range(1,n+1,1):
    if(n%i==0):
        print(i)"""

#q8 print the sum  of all even and odd numbers in a range

"""EvenSum=0
OddSum=0
for i in range(0,n+1,1):

    if (i%2==0):
        EvenSum=EvenSum+i
    else:
        OddSum=OddSum+i

print(EvenSum)
print(OddSum)
"""

#q9  a no is perfect or not -- perfect if sum of all the factors == n
factorSum=0
"""for i in range(1,n,1):
    if(n%i==0):
        factorSum=i+factorSum

print(factorSum)
if(factorSum==n):
    print(True) 

else:
    print(False)"""

#q10. check whether a no is prime or not

"""flag=True
for i in range(2,n,1):
    if(n%i==0):
       # print(i)
        flag=False

print(flag)  """

#q 11 Reverse a string without using any builtin fnx



"""string =str(input("Enter the string :")) # "prince". 6
"""
"""reversed= ""

for i in range(len(string)-1,-1,-1):   #basically 0 tk travel karna h so 0 se ek km tk likho ie -1
    reversed=reversed+string[i]

print(reversed)"""    


#M_2. print(string[0:0:-1])

#q 12 string is a pallindrome or not

"""reversed=""

for i in range(len(string)-1,-1,-1):
    reversed=reversed+string[i]


if(reversed==string):
    print(f"string {string} is a valid pallindrome")

else:
    print(f"string {string} is not a pallindrome")
"""


#q13. count all the letters ,digits,special characters

# isalnum() returns true  if that char is alphabet

#isalpha()  returns true  if that char is alphabet
"""
chars=0 
digits=0
symbol=0

for i in range(0,len(string),1):
    if(string[i].isdigit()==True):
       digits+=1
    elif ( string[i].isalpha()==True):
       chars+=1
    else:
       symbol+=1

    
print(chars, " ",digits," ",symbol)   

                                   
"""



#-------------------while loop--------------------------------------

"""a =1

while(a<=30):
    print(a)
    a+=1
"""

# -- get the digits of a number

while(n>0):
    digit =n%10
    print(digit)
    n= n//10

# see it is the way , which is different from the while loop in cpp



