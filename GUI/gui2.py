import tkinter as tk

root = tk.Tk()
root.title("LAYOUT")

frame_top = tk.Frame(root)
frame_bottom = tk.Frame(root)

frame_top.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
frame_bottom.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)


label1 = tk.Label(frame_top, text="Top frame - Label1")
label2 = tk.Label(frame_top, text="Top frame - Label2")
label3 = tk.Label(frame_bottom, text="Bottom Frame - Label1")
label4 = tk.Label(frame_bottom, text="Bottom frame - Label2")

label1.pack(side=tk.LEFT)
label2.pack(side=tk.RIGHT)
label3.grid(row=0, column=0)
label4.grid(row=0, column=1)

root.mainloop()
