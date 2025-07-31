
# c/5 = f-32/9
ch = int(input("1. C to F\n2. F to C\n"))
if(ch==1):
    temp= int(input("Enter temperature in Celcius = "))
    temp1 = (temp*(9/5))+32
    print(temp, "in Farenhite is = ", temp1)
elif(ch==2):
    temp= int(input("Enter temperature in Farenhite = "))
    temp1 = (temp-32)*(5/9)
    print(temp, "in Celcius is = ", temp1)
else:
    print("Invalid choice")

