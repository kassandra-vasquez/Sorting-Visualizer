from tkinter import *
from tkinter import ttk
import random
from colors import *

# making a basic window
window = Tk()
window.title("Sorting Algorithms Visualization")
window.maxsize(1000, 700)
window.config(bg = WHITE)

algorithm_name = StringVar()
algo_list = ["Bubble Sort", "Merge Sort"]

speed_name = StringVar()
speed_list = ["Fast", "Medium", "Slow"]

# empty list will be filled with random values everytime a new array is generated
data = []

# function will draw randomly generated list data[] on canvas vertical bars
def drawData(data, colorArray):
    pass

# function will generate array with random values eveytime generate button hit
def generate():
    pass

# function will set sorting speed
def set_speed():
    pass

# function triggers selected algorithm and starts sorting
def sort():
    pass

## UI HERE ##
UI_frame = Frame(window, width=900, height=300, bg=WHITE)
UI_frame.grid(row=0, column=0, padx=10, pady=5)

# dropdown to select algorithm
L1 = Label(UI_frame, text="Algorithm", bg=WHITE)
L1.grid(row=0, column=0, padx=10, pady=5, sticky=W)

algo_menu = ttk.Combobox(UI_frame, textvariable=algorithm_name, values=algo_list)
algo_menu.grid(row=0, column=1, padx=5, pady=5)
algo_menu.current(0)

# dropdown for selecting speed
L2 = Label(UI_frame, text="Sorting Speed: ", bg=WHITE)
L2.grid(row=1, column=0, padx=1, pady=5, sticky=W)

speed_menu = ttk.Combobox(UI_frame, textvariable=speed_name, values=speed_list)
speed_menu.grid(row=1, column=1, padx=5, pady=5)
speed_menu.current(0)

# the sort button
B1 = Button(UI_frame, text="Sort", command=sort, bg=LIGHT_BEIGE)
B1.grid(row=2, column=1, padx=5, pady=5)

# button that generates array
B3 = Button(UI_frame, text="Generate Array", command=generate, bg=LIGHT_BEIGE)
B3.grid(row=2, column=0, padx=5, pady=5)

# canvas to draw array
canvas = Canvas(window, width=800, height=400, bg=WHITE)
canvas.grid(row=1, column=0, padx=10, pady=5)


window.mainloop()
