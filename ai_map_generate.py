import tkinter as tk
import random
import time

root = tk.Tk()
root.title("My App Window")
root.geometry("400x300")

canvas = tk.Canvas(root, width=500, height=300, bg="white")
canvas.pack(pady=20)




def generate_map():
    #--------MAIN-----------

    time.sleep(key_value_random_pause)

    x1 = 0
    y1 = 150

    key = x1
    value = y1

    step_size = 20

    for i in range(30):
        x2 = x1 + step_size
        y2 = y1 + (random.randint(-15, 15))

        y2 = max(50, min(y2, 250))

        canvas.create_line(x1, y1, x2, y2, fill="green", width=3)
    
        x1 = x2
        y1 = y2


    #-----------------------

gen_button = tk.Button(root, text="Generate Map", command=generate_map, font=("Arial", 10, "bold"))
gen_button.pack(pady=10)


root.mainloop()
