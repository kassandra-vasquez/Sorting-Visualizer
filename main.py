from tkinter import *
from tkinter import ttk
import random
from colors import *
from algorithms.bubblesort import bubble_sort
from algorithms.mergesort import merge_sort
from algorithms.selectionsort import selection_sort
from algorithms.quicksort import quick_sort


# making a basic window
window = Tk()
window.title("Sorting Algorithms Visualization")
window.maxsize(1000, 700)
window.config(bg = WHITE)

algorithm_name = StringVar()
algo_list = ["Bubble Sort", "Merge Sort", "Selection Sort", "Quick Sort"]

speed_name = StringVar()
speed_list = ["Fast", "Medium", "Slow"]

# empty list will be filled with random values everytime a new array is generated
data = []

# function will draw randomly generated list data[] on canvas vertical bars
def drawData(data, colorArray):
    canvas.delete("all")
    canvas_width = 800
    canvas_height = 400
    x_width = canvas_width / (len(data) + 1)
    offset = 4
    spacing = 2
    normalizedData = [i / max(data) for i in data]

    for i, height in enumerate(normalizedData):
        x0 = i * x_width + offset + spacing
        y0 = canvas_height - height * 390
        x1 = (i + 1) * x_width + offset
        y1 = canvas_height

        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
    window.update_idletasks()

# function will generate array with random values eveytime generate button hit
def generate():
    global data
    data = []

    for i in range(0, 100):
        random_value = random.randint(1, 150)
        data.append(random_value)
    drawData(data, [BLUE for x in range(len(data))])

# function will set sorting speed
def set_speed():
    if speed_menu.get() == "Slow":
        return 0.3
    elif speed_menu.get() == "Medium":
        return 0.1
    else:
        return 0.001

# function triggers selected algorithm and starts sorting
def sort():
    global data
    timeTick = set_speed()

    if algo_menu.get() == "Bubble Sort":
        bubble_sort(data, drawData, timeTick)
    elif algo_menu.get() == "Merge Sort":
        merge_sort(data, 0, len(data)-1, drawData, timeTick)
    elif algo_menu.get() == "Selection Sort":
        selection_sort(data, drawData, timeTick)
    elif algo_menu.get() == "Quick Sort":
        quick_sort(data, 0, len(data)-1, drawData, timeTick)

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

# canvas to draw array
canvas = Canvas(window, width=800, height=400, bg=WHITE)
canvas.grid(row=1, column=0, padx=10, pady=5)

# the sort button
B1 = Button(UI_frame, text="Sort", command=sort, bg=LIGHT_BEIGE)
B1.grid(row=2, column=1, padx=5, pady=5)

# button that generates array
B3 = Button(UI_frame, text="Generate Array", command=generate, bg=LIGHT_BEIGE)
B3.grid(row=2, column=0, padx=5, pady=5)


window.mainloop()
