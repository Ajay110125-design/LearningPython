


"""
val=43861       # to reverse the num by getting the values to list
vals=[]
while val>0:
    rem=val%10
    vals.append(rem)  #vals.insert(0,rem) get in same order [1,2,3,4], append will get in last [4,3,2,1]
    val=val//10
print(vals)    # to get the values in list in same or reverse order based on append and insert
#vals.sort(reverse=True)

#vals.sort()    # to get in ascending order
#print(vals)
#vals.sort(reverse=True) # to grt in descending order  # enable this line to get highest num
#print(vals)

reverse=0
for i in vals:
    reverse=reverse*10+i
print(reverse)
"""


"""
input_amt=-123    #int(input(" Enter the value:"))
lst=[500,200,100]
for note in lst:
    total_notes = input_amt // note
    print(total_notes, note)
    input_amt = input_amt % note

# above logic is without any conditions

for note in lst:
    total_notes = input_amt // note

# Print ATM Machine logic ----how many 500,200,100 notes will get for given amount
input_amt=-123    #int(input(" Enter the value:"))
lst=[500,200,100]
if isinstance(input_amt,int):
#print(isinstance(input_amt,str))  #it is inbuilt function which is used for verifying the value is particular type or not ex:inp_amu="abc"
    if input_amt>0 and input_amt%100 :    # if u need to give with conditions
        for note in lst:
            total_notes = input_amt // note
            print(total_notes, note)
            input_amt = input_amt % note
    else:
         print("Given invalid amount, please enter the valid amount")
else:
    print("Please enter a int number")
"""

"""
#armstrong number x power of its length
n=370
l=str(n)
new=0
temp=n
for i in range(0,len(l)):
    r=temp%10
    new=new+r**len(l)
    temp=temp//10
print(new)
if n==new:
    print(n,"is a armstrong number")
else:
    print(n,"is not a armstrong number")
"""

"""
n=2342  #Palindrome    #we can change that int to str and can follow like str logic s=str(n)
r=0
temp=n
while temp>0:
    val=temp%10
    r=r*10+val
    temp=temp//10
if n==r:
    print(n,"is a palindrome")
else:
    print(n,"is not a palindrome")
"""


"""
str="malayalam"    #Print palindrome or reverse string   this logic work for the num if it is in string str="1231"
emp=""
for char in str:
    emp=char+emp
print(emp)
print(str)
if str==emp:
    print(str, "is a palindrome")
else:
    print(str, "is not a palindrome")

"""


"""
lst=[2,3,5,7,9,8,23,34,45,37,99,77,202,101,113,13]    # prime numbers from the list
for i in lst:
    count=0
    for j in range(1,(i+1)):
        if i%j==0:
           count=count+1
    if count==2:
        print(i,"is prime number")
"""

"""
lst=[1,2,3,4,5]     #factorial of each num in the list
for i in lst:
    fac=1
    for j in range(1,i+1):
        fac=fac*j
    print(fac)
"""

"""
# Factorial
val=5
fac=1
for i in range(1,val+1):
    fac*=i
print(fac)
"""

"""
# Find even num from the list if the even is at the starting then no need to run loop
vals=[35,36,33,333,333,22,55,77,79,99]
for val in vals:
    if val%2==0:
        print(val)
        break
print(val, "is even num")
"""

"""
val=int(input("Enter a number:"))    #Input method  or val=input("Enter a number:") l=int(val)-10
print(val-10)
"""

"""
#Pyramid
val=5
for i in range(1,val+1):
    print(" "*(val-i)+("*"*((i*2)-1)))
"""
"""
val=5
for i in range(1,6):
    print(" " * (val- i) + (i * "*"))
for k in range(5,0,-1):             # this for loop is easy to get both right and reverse right angle triangle
    print(" "*(val-k)+(k*"*"))
"""

"""
star="*"                 #Left angle triangle
for i in range(1,6):
    print(i*star)
for j in range(5,0,-1):  #reverse left angle triangle
    print(j*star)
"""

"""
lst1=[1,3,5,7,9]
lst2=[2,4,6,8,10]
lst=[]
for i in range(0,len(lst1)):
    val=lst1[i]
    val2=lst2[i]
    lst.append(val)        # instead of above 2 lines we can use like lst.append(lst1[i])
    lst.append(val2)       # instead of above 2 lines we can use like lst.append(lst1[i])
print(lst1)
print(lst2)
print(lst)
"""


"""
lst=[23,34,54,-23,-45,34,346,-345,-9,245,345,213456,23456,-23456,12345]
min_value=lst[0]
max_value=lst[0]
for i in range(1,len(lst)):      #instead of line 4 and 5 we can use for val in lst:
    val=lst[i]
    if val<min_value:
        min_value=val
    elif val>max_value:
        max_value=val
print(min_value)
print(max_value)
"""


"""
vals=[-10,-20,-30,-4,-80,-39,-5,-2]    #Find min value
min_value=vals[0]
for val in vals:
    if val<min_value:
        min_value=val
print(min_value)

vals=[-10,-20,-30,-4,-80,-39,-5,8]   #Find max value
max_value=vals[0]
for val in vals:            #for i in range(1,len(vals)) we can use
                            #val=vals[i]
    if val>max_value:
        max_value=val
print(max_value)
"""

"""
vals=[10,20,30,4,80,39]    #Find min value
min_value=vals[0]
for val in vals:
    if val<min_value:
        min_value=val
print(min_value)

vals=[10,20,30,4,80,39]    #Find max value
max_value=0
for val in vals:
    if val>max_value:
        max_value=val
print(max_value)
"""

"""
for num in range(1,11):  #print 1 to 10
    print(num)
for val in range(10,0,-1):  #print 10 to 1
    print(val)
"""

"""
#Multip[ication of a num
num=int(input("Enter a number:"))
for i in range(1,11):
    val=num*i
    print(num,"*",i,"=",val)
"""
"""
for num in range(1,11):  #print 1 to 10
    print(num)
for val in range(10,0,-1):  #print 10 to 1
    print(val)

n=5
total=0
for i in range(1,n+1):   #add upto nth num
    total=total+i
print(total)
"""
"""
# Check the given character is vowel or consonant
char='e'
if char=='a' or char=='e' or char=='i' or char=='o' or char=='u':
    print("The given character",char,"is one the vowel")
else:
    print("The given character is not the vowel/consonant")
"""

"""
# Check the person is available for loan or not based on salary and age
salary=30001
age=35
if age>21 and salary>30000:
    print("the person is eligible for loan")
else:
    print("the person is not eligible for loan")
"""
"""
#Check the number is muliplied with both 5 and 11
num=110
if num%5==0 and num%11==0:
    print(num, "is multiple of both 5 and 11")
else:
    print(num, "is not a multiple of both 5 or 11")
"""
"""
#Print prime numbers
nums=[1,3,5,9,15,13,23,45,67,89,76,23,99,111,113]
k = []
for i in nums:
    count = 0
    for m in range (1,i):
        if i%m==0:
           count=count+1
    if count==1:
          k.append(i)
print("prime numbers are", k)
"""

"""
num=27      #Check the given number is prime or not
count=0
for i in range(1,num+1):
    if num%i==0:
        count+=1
if count==2:
    print(num,"is a prime number")
else:
    print(num,"is not a prime number")
"""


