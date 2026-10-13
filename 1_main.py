print ( "Hello world , i am learning python as a language as i can write code in python only in accenture summer internship drive ")



# terminal --> gives i/p o/p both 
# output  --> only gives o/p doesn't take i/p
# problem --> shows the problems /errors inside the code 
#

st = 'c'
strrrr= "c"

print (type(st))
print(type(strrrr))

#so both line 13and 14 will have same o/p as string , nothing like char , as in the latest python there is nothing called character ,  " "==' '

b = True

print ( type(b))

a = 'Afgf'

#print (ord(a));
print(chr(128522))
 
#---------------strings---------------

a= 'sher coders'

print(a[0:3:1])

print(a[0:3+1:1]) #.   [start index: stop index +1: steps]

print ( a[ 5::1])


#.          -------------TYPE CONVERSION ___________----------------


print( str(65))

a =" 5"

print  ( float(5))
print  ( str(5))

print  ( bool(5))
print  ( int(5))

#---------------OUTPUT-----------------------

name =" prince"
age = "20"


#strucured way 

print( "My name is",name,"and my age is",age)

# formatted way
print( f"My name is{name} and my age is {age}")


#---------------INPUT-----------------------------

#age = int(input( "hello what is your age")) #.  --- jo bhi input me ata h , uska predefined DT string hota h  output int ki tarah dikh to raha h but internally wo string hota h
# so always do typecasting of the i/p


print(age)
print(type(age))


#number = int(input("Enter any number" ))
#print ( number)


#----------------------OPERATORS----------------------

    #print("OPERETAOR")
#-- 1 ) ARITHMETIC OPERATORS

print ( 5/4) # division. ->>  float value ( as p/q format h)
print(5//4) # flow dviison --> only int value
print( 5%4) # rem
print ( 5*4) # multiply
print( 5**4) # power

#

a= ( 'A'<='D')
print ( 'A'<='D')


#-----------LOgical operator---------------

print( not 48<32 and 34==32 or 334>33)

print( True and bool(0))

# Python Operator Precedence (Highest to Lowest)

# 1.  ()
# 2.  x[i], x[i:j], x(), x.attribute
# 3.  await
# 4.  **
# 5.  +x, -x, ~x
# 6.  *, @, /, //, %
# 7.  +, -
# 8.  <<, >>
# 9.  &
# 10. ^
# 11. |
# 12. <, <=, >, >=, !=, ==, in, not in, is, is not
# 13. not
# 14. and
# 15. or
# 16. if-else
# 17. lambda
# 18. :=

#------------------CONDITIONAL--------------------

# syntax of for loop .py
a = 10
if a>10:
    print  ( "a is greater than 10")

elif a==10:
    print( "a is equal to 10")

else :
    print( " a is less than 10")


#q 5. -- if the taken year is leap or not

"""year = int(input( "Enter year"))

if ( year %400)==True :
    print("year is leap")

elif ( year%4==0 and year%100!=0):
    print ( "year is leap")

else: 
    print ("year is not a leap year")
 """
#q -4  voting right
"""
name = str(input( "Enter your name "))
age = int(input("Enter your age"))

if ( age>=18):
    print ( f"hello {name} you are a valid voter")

else:
    print ( f"hello {name} you are a valid voter")"""

# elif ladder question
"""
temp = int ( input("Enter the temperature"))

if (temp<0):
    print(" Freezing c")

elif( temp<10):
    print( " Very cold") 

elif(temp<20):
    print("cold")

elif(temp<30):
    print("pleasant")

elif(temp<40):
    print("Hot")

elif(temp>=40):
    print("Very Hot")
"""
#-----------------------FOR LOOP-----------------------

# FOR LOOP

a= range(1,11,1)

for i in a :
    print(i)

print("    ")   

for i in range(0,40,5):
    print(i)

# 20 , 19 , ...,1
for i in range(20,0,-1):
    print(i)

print(   "    ")


#printing the table of n  

n = int(input("Enter the number whose table you want to print"))

for i in range( n, 10*n+1,n):
    print (i)


# loop for string

name = "sheryansh"

for i in range(9):
    print (name[i])

print (len(name))

