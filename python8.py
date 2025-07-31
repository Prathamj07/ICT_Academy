## Count even odd
ch1=0
ch2=0
l= int(input("Enter the number of numbers = "))
a=[]
for i in range(l):
    ch= int(input("Enter the number = "))
    a.append(ch)
for digit in a:
    if(digit%2==0):
        ch1 = ch1+1
    else:
        ch2 = ch2+1
print("Number of even digits = ", ch1)
print("Number of odd digits = ", ch2)
