a = "Pratham"

x= "p"+a[1:] ## DEEP COPY : Will be saved not deleted
print("p"+a[1:]) ## SHALLOW COPY : Gets deleted later
print(x)


