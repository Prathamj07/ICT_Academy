import tkinter as tk

root = tk.Tk()

root.title("Widget")
root.geometry("200x100")

# Label

label = tk.Label(root, text="Enter Temp to convert")
label.grid(row=0, column=0, padx=10, pady=10, sticky='w')

# Entry
temp_var = tk.StringVar()
entry = tk.Entry(root, textvariable=temp_var)
entry.grid(row=1, column=0)

output = tk.Label(root, text="")
output.grid(row=2, column=0)
def on_click():
    
    temp = float(temp_var.get())
    temp_in_f = ((temp*9)/5) + 32
    output.config(text=f"Temperature in F is + {temp_in_f} F") 
    
    
# Button
button = tk.Button(root, text="Submit", command=on_click)
button.grid(row=1, column=2)


    
# Text box
# text = tk.Text(root, height=5, width=40)
# text.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# checkbutton = tk.Checkbutton(root, text="Check me")
# checkbutton.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
