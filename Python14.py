#Max element

a = [1,2,3,4,-500,6,7,8,9]
min=a[0]
for i in range(len(a)):
    if(a[i]<min):
        max = a[i]
print("Min Element = ", max) 
