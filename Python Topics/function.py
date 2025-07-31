# # def fun(*a):
# def max(a,b,c):
#     if(a>b>c or a>c>b):
#         print("Maximum Number is ", a)
#     elif(b>c>a or b>a>c):
#         print("Maximum Number is ", b)
#     else:
#         print("Maximum Number is ", c)

# max(5,100,2)

# def sumList(a):
#     sum =0
#     for i in a:
#         sum+=i
#     print("Sum = ", sum)
# sumList((8,2,3,0,7))


# def sumList(a):
#     product = 1
#     for i in a:
#         product*= i
#     print("Product = ",product)
# sumList((8,2,3,-1,7))


# def rev(s):
#     print(s[::-1])
# rev("Pratham")


def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n* factorial(n-1)
print(factorial(5))


def check(a,b,c):
    if c in range(a,b):
        print("YES")
    else:
        print("NO")
check(50,100,49)


var = lambda x: x+15
print(var(8))


var = lambda x,y,z: x+y+z
print(var(1,2,3))


var = lambda x,y: x**y
print(var(8,2))





        


