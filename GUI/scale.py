import tkinter as tk

def on_scale_change(value):
    label_value.config(text=f"Scale Value: {value}")
    
    
root = tk.Tk()
root.title("Scale Widet")

root.geometry("400x400")
label = tk.Label(root, text="Enter your Phone Number")
label.pack(pady=10)

frame = tk.Frame(root)
scale = tk.Scale(frame, from_=6000000000, to=9999999999,length=1500, orient=tk.HORIZONTAL, command=on_scale_change)
scale.pack(pady=20)

label_value = tk.Label(frame, text="Scale Value: 0")
label_value.pack

frame.pack(pady=20)
root.mainloop()
