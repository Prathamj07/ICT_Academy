# Table of a number 
# x = int(input("Enter a number to make table = "))
# for i in range(1,11):
#     print(x," X ",i," = ", i*x)


# #Divisible by 7 and multiple of 5
# print("Numbers divisible by 7 and Multiple of 5\n")
# for i in range(1500,2701,5):
#     if(i%7==0):
#         print(i)

## c/5 = f-32/9
# ch = int(input("1. C to F\n2. F to C\n"))
# if(ch==1):
#     temp= int(input("Enter temperature in Celcius = "))
#     temp1 = (temp*(9/5))+32
#     print(temp, "in Farenhite is = ", temp1)
# elif(ch==2):
#     temp= int(input("Enter temperature in Farenhite = "))
#     temp1 = (temp-32)*(5/9)
#     print(temp, "in Celcius is = ", temp1)
# else:
#     print("Invalid choice")


# import random
# guess= random.randint(1,10)
# var = 0
# while(var!=guess ):
#     var = int(input("Guess a number between 1-10 = "))
#     print("Try Again")
    
# print("BINGO")
# x= int(input("Enter number of rows = "))    
# for i in range(1,x):
#     print(' * '*i)
# for i in range(x,0,-1):
#     print(' * '*i)


# w = input("Enter a word = ")
# l = len(w)
# for ch in range(l-1,-1,-1):
#     print(w[ch], end="")

# ch1=0
# ch2=0
# l= int(input("Enter the number of numbers = "))
# a=[]
# for i in range(l):
#     ch= int(input("Enter the number = "))
#     a.append(ch)
# for digit in a:
#     if(digit%2==0):
#         ch1 = ch1+1
#     else:
#         ch2 = ch2+1
# print("Number of even digits = ", ch1)
# print("Number of odd digits = ", ch2)


# for i in range(0,6):
#     if(i==3 or i==6):
#         continue
#     print(i,end =" ")
    
# x= int(input("Enter number = "))
# a=0
# b=1

# for i in range(x):
#     print(a)
    
#     a,b= b,a+b

for digit in range(50):
    if(digit%3==0):
        print("FIZZ")
    elif(digit%5==0):
        print("BUZZ")
    else:
        print(digit)
    
    

    
    
    
    
    
    
    
    
    
    
    
    
