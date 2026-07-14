import tkinter as tk

root = tk.Tk()
root.title("My App Window")
root.geometry("400x300")

canvas = tk.Canvas(root, width=500, height=300, bg="white")
canvas.pack(pady=20)

#--------MAIN-----------

# Draw a static line: create_line(x1, y1, x2, y2, options)
label = tk.Label(root, text="Hello! This is running like an app.")


x1 = 50
y1 = 50

x2 = 70


for i in range(3):
    
    x1 += 20
    x2 += 20
    canvas.create_line(x1, y1, x2, y1, fill="blue", width=3)
    x1 += 5
    x2 += 5
    

#-----------------------


label.pack(pady=50)

root.mainloop()
