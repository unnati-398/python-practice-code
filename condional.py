#check whether the number is even , odd or zero


num=int(input("Enter a number:"))
rem=num%2
if num==0:
    print("number is zero")
elif rem==0:
    print("number is even")
else:
    print("number is odd")
     
#check if person is eligible to vote
age=int(input("Enter your age:"))
if age>=18:
    print("you are eligible to vote")
else:
    print("you are not eligible to vote")

# printing factors   
num = int(input("Enter a number : "))
for a in range (1,num+1):
    rem = num%a
    if rem==0:
        print("factors of " , num , " is " , a)

# printing multiplication table of 5 using formatting function
for i in range(0,11):
    table=5*i
    print( f"5 X {i} = {table}")

# sum of N natural number and here N is user input
num = int(input("Enter a number : "))
sum=0
for a in range (0,num+1):
    sum=sum+a
print("sum : " , sum)

# print all even numbers between 1 to 50
for a in range (1,51):
    rem=a%2
    if (rem==0):
        print(a)


# take number from user and then print its factorial
number = int(input("Enter a number : "))
factorial=1
for i in range(1,number+1):
    factorial=i*factorial
print("factorial of " , number , "is " , factorial)

# checking whether the three number is armstrong or not
num = int(input("Enter a three digit number : "))
a=num
sum=0
for i in range(0,3):
    rem=num%10
    sum=sum + (rem**3)
    num=num//10
if (sum==a):
    print(a , "is a armstrong number")
else:
    print(a , "is not a armstrong number")

# checking whether the number of any length is armstrong or not
num=int(input("Enter a number of any length : "))
a=num
length=len(str(a))
sum=0
for i in range(0,length):
    rem=num%10
    sum=sum+(i**length)
    num=num//10
if (sum==a):
    print(a , "is a armstrong number")
else:
    print(a , "is not a armstrong number")

#chck whetherb number is prime or not
a=int(input("Enter a number : "))
count=0
for i in range(1,a+1):
    rem=a%i
    if (rem==0):
        count+=1
    else:
        continue
if (count==2):
    print(a , "is a prime number")
else:
    print(a , "is not a prime number")

#entering a password and if the password is correct then it should show you are logged in if password is incorrect it should show try again and there will be only 3 chances
password=453676
for i in range(0,3):
    passwd=int(input("Enter your password to login: "))
    if (passwd==password):
        print("you are logged into your account")
        break
    else:
        if (i<2):
            print("please try again")
        else:
            print("your login attemps are completed try after sometime")

#print numbers 1 to 100 , but print "fizz" for multiple of 3 , "buzz" for the multiple for 5 and "fizzbizz" for multiple for both
for i in range(1,101):
    a=i%3
    b=i%5
    if (a==0 and b==0):
        print("fizzbuzz")
    elif(a==0):
        print("fizz")
    elif(b==0):
        print("buzz")
    else:
        print(i)
            






            





















    


        


    

