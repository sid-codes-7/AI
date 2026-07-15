import tkinter as tk
import random
import time

root = tk.Tk()
root.title("My App Window")
root.geometry("400x300")

canvas = tk.Canvas(root, width=500, height=300, bg="white")
canvas.pack(pady=20)

count = 0

def generate_map1():
        global count
    #----The Straight Line at the beginning-----
    
        count += 1
        canvas.delete("all")

        if count == 1:
            canvas.create_line(0, 215, 1355, 215, fill="green", width=3)
        else:
            generate_map2()
        
gen_button = tk.Button(root, text="Generate Map", command=generate_map1, font=("Arial", 10, "bold"))

def generate_map2():
    #--------MAIN-----------
    x1 = 0
    y1 = 150

    key = x1
    value = y1

    step_size = 20

    terrain_strength = min(count * 1, 15)

    for i in range(30):
        x2 = x1 + step_size

        y2 = y1 + (random.randint(-terrain_strength, terrain_strength))

        y2 = max(50, min(y2, 250))

        canvas.create_line(x1, y1, x2, y2, fill="green", width=3)
    
        x1 = x2
        y1 = y2

    #-----------------------
gen_button.pack(pady=10)
root.mainloop()
