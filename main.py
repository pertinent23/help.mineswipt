#!/usr/bin/python

import tkinter as tk
from random import randint

NB_COLS = 8
NB_ROWS = 8
NB_MINES = 10

GAME_NAME = "MineSwipt"
WIDTH = 600
HEIGHT = 600

RED = "#FF1122"
GRAY = "#F2F2F2"
GRAY_2 = "#D2D2D2"
GRAY_3 = "#C2C2C2"
GRAY_4 = "#EEEEEE"
WHITE = "#FFFFFF"
BLACK = "#000000"

# show positions of mines
# 0: if is a free case
# -1: there is a mine
content = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
]

# Show the user progression
# if the value of a cell is:
#  0: the cell has not be discover
#  1: already discover
#  2: there is a flag
progress = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
]

#will content all cells
cells = []

# Will content the window 
window = None
is_lost = None

def generate_mine():
    for i in range(0, NB_MINES):
        
        x = randint(0, NB_ROWS-1)
        y = randint(0, NB_COLS-1)
        
        while content[x][y] == -1:
            x = randint(0, NB_ROWS-1)
            y = randint(0, NB_COLS-1)
        
        content[x][y] = -1
        add_indicators(x, y)


def add_indicators(x, y):
    if y-1 >= 0 and content[x][y-1] >= 0:
        content[x][y-1] += 1
    
    if y+1 < NB_COLS and content[x][y+1] >= 0:
        content[x][y+1] += 1
        
    if x-1 >= 0 and content[x-1][y] >= 0:
        content[x-1][y] += 1
    
    if x-1 >= 0 and y-1 >= 0 and content[x-1][y-1] >= 0:
        content[x-1][y-1] += 1
    
    if x-1 >= 0 and y+1 < NB_COLS and content[x-1][y+1] >= 0:
        content[x-1][y+1] += 1
    
    if x+1 < NB_COLS and content[x+1][y] >= 0:
        content[x+1][y] += 1
    
    if x+1 < NB_ROWS and y+1 < NB_COLS and content[x+1][y+1] >= 0:
        content[x+1][y+1] += 1
    
    if x+1 < NB_ROWS and y-1 >= 0 and content[x+1][y-1] >= 0:
        content[x+1][y-1] += 1


def free_cell(x, y):
    if x < NB_ROWS and y < NB_COLS:
        if content[x][y] == 0:
            progress[x][y] = 1
            if y-1 >= 0 and content[x][y-1] >= 0 and progress[x][y-1] == 0:
                free_cell(x, y-1)
            
            if y+1 < NB_COLS and content[x][y+1] >= 0 and progress[x][y+1] == 0:
                free_cell(x, y+1)
                
            if x-1 >= 0 and content[x-1][y] >= 0 and progress[x-1][y] == 0:
                free_cell(x-1, y)
            
            if x-1 >= 0 and y-1 >= 0 and content[x-1][y-1] >= 0 and progress[x-1][y-1] == 0:
                free_cell(x-1, y-1)
            
            if x-1 >= 0 and y+1 < NB_COLS and content[x-1][y+1] >= 0 and progress[x-1][y+1] == 0:
                free_cell(x-1, y+1)
            
            if x+1 < NB_COLS and content[x+1][y] >= 0 and progress[x+1][y] == 0:
                free_cell(x+1, y)
            
            if x+1 < NB_ROWS and y+1 < NB_COLS and content[x+1][y+1] >= 0 and progress[x+1][y+1] == 0:
                free_cell(x+1, y+1)
            
            if x+1 < NB_ROWS and y-1 >= 0 and content[x+1][y-1] >= 0 and progress[x+1][y-1] == 0:
                free_cell(x+1, y-1)
                
        elif content[x][y] >= 0:
            progress[x][y] = 1
            
        else:
            return 1
    
    return 0

def lost(is_mine):
    global is_lost
    
    if not is_lost and not is_mine:
        is_lost = False
    
    if is_mine:
        is_lost = True
        
        for i in range(0, NB_ROWS):
            for j in range(0, NB_COLS):
                progress[i][j] = 1

def isLost():
    global is_lost
    return is_lost

class Cell(tk.Frame):
    x:int = 0
    y:int = 0
    show:bool = False
    canvas: tk.Canvas = None
    
    def __init__(self, master, x, y):
        super().__init__(master, bg=GRAY_2, width=(WIDTH*0.8)/NB_ROWS, height=(WIDTH*0.8)/NB_COLS, highlightbackground=WHITE, highlightthickness=1)
        self.grid(column=y, row=x)
        self.set_x(x)
        self.set_y(y)
        self.main()
    
    def set_x(self, x:int):
        self.x = x
    
    def set_y(self, y:int):
        self.y = y
    
    def main(self):
        self.bind('<Enter>', self.on_motion)
        self.bind('<Leave>', self.on_leave)
        self.bind('<Button>', self.on_button)
        self.bind('<<Change>>', self.on_change)
    
    def on_motion(self, event):
        if not self.show:
            self.configure(bg=GRAY_3)
    
    def on_leave(self, event):
        if not self.show:
            self.configure(bg=GRAY_2)
    
    def on_button(self, event):
        global message, restart
        
        lost(free_cell(self.x, self.y))
        for cell in cells:
            cell.event_generate('<<Change>>', when='tail')
        
        if is_lost:
            message.configure(text="GAME IS OVER", fg=RED)
            restart.grid(row=1, column=1)
    
    def reset(self):
        self.show = False
        if self.canvas:
            self.canvas.pack_forget()
            self.canvas = None
    
    def create_circle(self, x, y, r, canvas: tk.Canvas):
        x0 = x - r
        y0 = y - r
        x1 = x + r
        y1 = y + r
        canvas.create_oval(x0, y0, x1, y1, fill=RED, width=0)

    
    def on_change(self, event):
        if progress[self.x][self.y] == 1 and not self.show:
            if content[self.x][self.y] > 0:
                self.configure(bg=GRAY_4, highlightthickness=0, background=GRAY_4)
                self.canvas = canvas = tk.Canvas(
                    self, 
                    bg=GRAY_4, 
                    highlightthickness=0, 
                    width=(WIDTH*0.8)/NB_ROWS, 
                    height=(WIDTH*0.8)/NB_COLS
                )
                canvas.create_text(30, 30, text="{0}".format(content[self.x][self.y]))
                canvas.pack()
            elif content[self.x][self.y] == 0:
                self.configure(bg=GRAY_4, highlightthickness=0, background=GRAY_4)
            else:
                self.configure(bg=GRAY_4, highlightthickness=0, background=GRAY_4)
                self.canvas = canvas = tk.Canvas(
                    self, 
                    bg=GRAY_4, 
                    highlightthickness=0, 
                    width=(WIDTH*0.8)/NB_ROWS, 
                    height=(WIDTH*0.8)/NB_COLS
                )
                self.create_circle(30, 30, 10, canvas)
                self.create_circle(40, 40, 5, canvas)
                self.create_circle(20, 20, 5, canvas)
                self.create_circle(40, 20, 5, canvas)
                self.create_circle(20, 40, 5, canvas)
                canvas.pack()
            self.show = True
            

def restart_game(event: tk.Event):
    global is_lost
    
    is_lost = False
    message.configure(text="")
    event.widget.grid_forget()
    
    for cell in cells:
        cell.configure(highlightbackground=WHITE, highlightthickness=1, bg=GRAY_2)
        cell.reset()
    
    for i in range(0, NB_ROWS):
        for j in range(0, NB_COLS):
            progress[i][j] = 0
            content[i][j] = 0
    
    generate_mine()

window = tk.Tk()
window.wm_title(GAME_NAME)
window.geometry("{width}x{height}".format(width=WIDTH, height=HEIGHT))
window.resizable(False, False)

head = tk.Frame(window, bg=WHITE, width=WIDTH, height=HEIGHT*0.1)
head.pack_propagate(0)
head.grid(row=0, column=0)

message = tk.Label(head, bg=WHITE)
message.pack(fill=tk.BOTH, expand=tk.TRUE)

body = tk.Frame(window, bg=WHITE)
body.config(width=WIDTH, height=HEIGHT*0.8)

tk.Frame(body, bg=WHITE, width=WIDTH*0.1, height=HEIGHT*0.8).grid(row=0, column=0)
tk.Frame(body, bg=WHITE, width=WIDTH*0.1, height=HEIGHT*0.8).grid(row=0, column=2)

body_content = tk.Frame(body, bg=GRAY, width=WIDTH*0.8, height=HEIGHT*0.8, highlightthickness=2, highlightbackground=GRAY_2)
body_content.grid(row=0, column=1)

for i in range(0, NB_ROWS):
    for j in range(0, NB_COLS):
        cells.append(Cell(body_content, i, j))

body.grid(row=1, column=0)

footer = tk.Frame(window, bg=WHITE, width=WIDTH, height=HEIGHT*0.1)
footer.grid_propagate(0)
footer.grid_columnconfigure(0, weight=3)
footer.grid_columnconfigure(1, weight=3)
footer.grid_columnconfigure(2, weight=3)
footer.grid_rowconfigure(0, weight=3)
footer.grid_rowconfigure(1, weight=3)
footer.grid_rowconfigure(2, weight=3)
footer.grid(row=2, column=0)

restart = tk.Button(footer, text="RESTART", bg=GRAY_4, highlightthickness=0)
restart.bind('<Button>', restart_game)
restart.grid_forget()

generate_mine()

window.mainloop()