import tkinter as tk

def on_button_click():
    label.config(text="Button Clicked")
    
root = tk.Tk()

root.title("Button")
root.geometry("500x500")

label = tk.Label(root, text="HELLO")
label.pack(pady=20)

button = tk.Button(root, text = "Click here", command = on_button_click)
button.pack()

root.mainloop()
