import tkinter as tk
from tkinter import PhotoImage

root = tk.Tk() 
## TK is the class created and root is the object of it
root.title("My APP") ## Title is METHOD and usme text push kar rahe he
root.geometry("400x400") ## again geometry is method usme screen size pushed(in px unit)

icon=PhotoImage(file= 'D:\Study\ICT\GUI_Development\GUI\image.png')
root.iconphoto(True, icon)


###### PACK LAYOUT
# label1= tk.Label(root, text="Label1", bg="red")
# label1.pack(fill= tk.BOTH, expand = True)

# label2= tk.Label(root, text="Label2", bg="blue")
# label2.pack(fill= tk.BOTH, expand = True)

# label3= tk.Label(root, text="Label3", bg="yellow")
# label3.pack(fill= tk.BOTH, expand = True)

##### GRID LAYOUT
# label1= tk.Label(root, text="Label1", bg="red")
# label1.grid(row=0, column=0)

# label2= tk.Label(root, text="Label2", bg="blue")
# label2.grid(row=1, column=1)

# label3= tk.Label(root, text="Label3", bg="yellow")
# label3.grid(row=2, column=2)

label1= tk.Label(root, text="Label1", bg="red")
label1.place(x=50,y=50)

label2= tk.Label(root, text="Label2", bg="blue")
label2.place(x=150,y=150)

label3= tk.Label(root, text="Label3", bg="yellow")
label3.place(x=200,y=200)



root.mainloop() ## Always at last as it acts as main file
