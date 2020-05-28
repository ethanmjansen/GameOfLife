from tkinter import *
from colors import COLORS
from random import choice, randint

# Root
root = Tk()

root.title("Ethan Jansen CS29 Buildweek 1")

eight = 8

# Title
GOL = Label(root, text = "Conway's Game of Life", font=('Georgia', 18))
GOL.pack(side = TOP)

# Frame1
frame1 = Frame(root)
frame1.pack()

# Frame1 subframes
frame3 = Frame(frame1)
frame3.pack(side = LEFT, fill=BOTH, padx=10)

'''++++++++++++++++++++++++++++++++++Main Game of Life Start++++++++++++++++++++++++++++++++++++'''
# Main Game Canvas
canvas = Canvas(frame3)

# Generation counter frame
frame6 = Frame(frame3)
frame6.pack()

def counter_label(label):
    '''Counts up while main game loop is running'''
    counter = 0
    def count():
        global counter
        counter += 1
        label.config(text=str(counter))
    count()

def counter_reset(label):
    '''Resets the counter when the reset button is pressed'''
    global counter
    counter = 0
    label.config(text=str(counter))

# Making Generation labels to be used as the counter
generation_part1 = Label(frame6, text = "Generation#", font=('Georgia', 16))

generation_part2 = Label(frame6, text = "Generation#", font=('Georgia', 16))

class Cell:
    def __init__(self, x, y, i, j):
        self.isAlive = False
        self.nextStatus = None
        self.pos_screen = (x, y)
        self.pos_matrix = (i, j)

    def __str__(self):
        return str(self.isAlive)

    def __repr__(self):
        return str(self.isAlive)

    def switchStatus(self):
        self.isAlive = not self.isAlive


def create_grid():
    """This function creates the board on which the game will take place"""
    x = 10
    y = 10
    global grid # Variable to store the Cell objects
    global rectangles # Variable to store rectangles
    rectangles = []
    grid = []
    for i in range(25):
        grid.append([])
        rectangles.append([])
        for j in range(35):
            rect = canvas.create_rectangle(x, y, x+10, y+10, fill="white")
            rectangles[i].append(rect)
            grid[i].append(Cell(x, y, i, j))
            x += 10
        x = 10
        y += 10
    counter_reset(generation_part2)


def find_rect_coordinates(x, y):
    """Find the co-ordinates of the rectangle which has been clicked"""
    return (x- x%10, y - y%10)


def change_colour_on_click(event):
    """ Change the colour of the clicked grid and change the status of cell in the grid """
    # print(event.x, event.y)
    x, y = find_rect_coordinates(event.x, event.y)
    try:
        iy = x // 10 - 1
        ix = y // 10 - 1
        if ix == -1 or iy == -1:
            raise IndexError
        if grid[ix][iy].isAlive:
            canvas.itemconfig(rectangles[ix][iy], fill="white")
        else:
            canvas.itemconfig(rectangles[ix][iy], fill="black")
        grid[ix][iy].switchStatus()
        # print(grid[ix][iy].pos_matrix, grid[ix][iy].pos_screen)
    except IndexError:
        return


def paint_grid():
    for i in grid:
        for j in i:
            if j.nextStatus != j.isAlive:
                x, y = j.pos_matrix
                # print(x, y)
                if j.nextStatus:
                    # canvas.itemconfig(rectangles[x][y], fill="black")
                    canvas.itemconfig(rectangles[x][y], fill=choice(COLORS))
                    # print("changed", j.pos_matrix, "from dead to alive")
                else:
                    canvas.itemconfig(rectangles[x][y], fill="white")
                    # print("changed", j.pos_matrix, "from alive to dead")
                j.switchStatus()
                # print("Current status of", j.pos_matrix, j.isAlive)


def changeInStatus(cell):
    ''' If the cell's status changes in the next gen, return True else False '''
    num_alive = 0
    x, y = cell.pos_matrix
    for i in (x-1, x, x+1):
        for j in (y-1, y, y+1):
            if i == x and j == y:
                continue
            if i == -1 or j == -1:
                continue
            try:
                if grid[i][j].isAlive:
                    num_alive += 1
            except IndexError:
                pass
    if cell.isAlive:
        return not( num_alive == 2 or num_alive == 3 )
    else:
        return num_alive == 3


def begin_game():
    for i in grid:
        for j in i:
            if changeInStatus(j):
                j.nextStatus = not j.isAlive
                # print("change in", j.pos_matrix, "from", j.isAlive, "to", j.nextStatus)
            else:
                j.nextStatus = j.isAlive
    paint_grid()
    counter_label(generation_part2)
    global begin_id
    begin_id = root.after(200, begin_game)


def stop_game():
    root.after_cancel(begin_id)  

create_grid()
canvas.bind("<Button-1>", change_colour_on_click)

# Packing in the rest
generation_part1.pack(side=LEFT)
generation_part2.pack(side=LEFT)
canvas.pack()

''''++++++++++++++++++++++++++++++++++Main Game of Life End++++++++++++++++++++++++++++++++++++'''

# Frame3 subframe
# Frame 6
frame7 = Frame(frame3)
frame7.pack()

# Controls
Play = Button(frame7, text = "Play", font = ('Georgia', 12), command=begin_game)
Pause = Button(frame7, text = "Pause", font = ('Georgia', 12), command=stop_game)
Reset = Button(frame7, text = "Reset", font = ('Georgia', 12),command=create_grid)
Play.pack(side = LEFT, padx=10)
Pause.pack(side = LEFT, padx=10)
Reset.pack(side = RIGHT, padx=10)

# Frame 4 
frame4 = Frame(frame1)
frame4.pack(side = LEFT, fill=BOTH, padx = 10, pady = 40)

# Frame 5
frame5 = Frame(frame1)
frame5.pack(side = LEFT,fill=BOTH,anchor=CENTER)

# Presets

# Glider
def glider():
    canvas.itemconfig(rectangles[21][4], fill="black")
    grid[21][4].switchStatus()
    canvas.itemconfig(rectangles[21][5], fill="black")
    grid[21][5].switchStatus()
    canvas.itemconfig(rectangles[21][6], fill="black")
    grid[21][6].switchStatus()
    canvas.itemconfig(rectangles[22][6], fill="black")
    grid[22][6].switchStatus()
    canvas.itemconfig(rectangles[23][5], fill="black")
    grid[23][5].switchStatus()
Preset1 = Button(frame4, text = "Glider", font = ('Georgia', 12), command=glider)
Preset1.pack(anchor = W, pady=10)

# Random
def random_config():
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            n = randint(0,3)
            if n == 0:
                canvas.itemconfig(rectangles[i][j], fill="black")
                grid[i][j].switchStatus()
Preset2 = Button(frame4, text = "Random", font = ('Georgia', 12), command=random_config)
Preset2.pack(anchor = W, pady=10)

# Spaceship
def spaceship():
    canvas.itemconfig(rectangles[12][32], fill="black")
    grid[12][32].switchStatus()
    canvas.itemconfig(rectangles[14][32], fill="black")
    grid[14][32].switchStatus()
    canvas.itemconfig(rectangles[15][31], fill="black")
    grid[15][31].switchStatus()
    canvas.itemconfig(rectangles[15][30], fill="black")
    grid[15][30].switchStatus()
    canvas.itemconfig(rectangles[15][29], fill="black")
    grid[15][29].switchStatus()
    canvas.itemconfig(rectangles[15][28], fill="black")
    grid[15][28].switchStatus()
    canvas.itemconfig(rectangles[15][27], fill="black")
    grid[15][27].switchStatus()
    canvas.itemconfig(rectangles[14][27], fill="black")
    grid[14][27].switchStatus()
    canvas.itemconfig(rectangles[13][27], fill="black")
    grid[13][27].switchStatus()
    canvas.itemconfig(rectangles[12][28], fill="black")
    grid[12][28].switchStatus()
    canvas.itemconfig(rectangles[11][30], fill="black")
    grid[11][30].switchStatus()
Preset3 = Button(frame4, text = "Space Ship", font = ('Georgia', 12), command=spaceship)
Preset3.pack(anchor = W, pady=10)

# Rules
QuoteBody = """
1. Any live cell with two or three live neighbours\nsurvives.

2. Any dead cell with three live neighbours\nbecomes a live cell.

3. All other live cells die in the next generation.\nSimilarly, all other deadcells stay dead.
"""
RulesHead = Label(frame5, text = "Game of Life Rules:", font = ('Georgia', 16))
RulesBody = Label(frame5, text = QuoteBody, font = ('Georgia', 12), justify = LEFT)
RulesHead.pack()
RulesBody.pack(padx=20)

# Frame 2
frame2 = Frame(root)
frame2.pack()

# About
InfoBody = """
At fifty years old, The Game of Life has aged well. John Conway first imagined the game on a Go board and discussed it's rules regularly during coffee breaks with his collegues. The idea can be traced to a much earlier date in the 1940's when John von Neumann wanted to find a way to populate the planets by sending autonomous machines that could replicate themselves to Mars. A machine able to replicate itself would be a good way to start exploration to other worlds. These machines, according to von Neumann, would be possible through a simulation of a Turing machine. A Turing machine is a theoretical machine that houses a CPU that can write a tape in sequential order which can be manipulated through the CPU. To be Turing Complete, is to be able to answer any computationaly answerable question given to the theoretical machine. Stanislav Ulim strived to create such a machine when he invented the cellular automata, a grid whose cells had a finite numbers of states (dead or alive). Conway brought these ideas together when he created a Turing complete cellular automata with the purpose of being as unpredictable as life was.
"""

AboutHead = Label(frame2, text = "About this Algorithm:", font = ('Georgia', 16))
AboutBody = Label(frame2, text = InfoBody, font = ('Georgia', 12), wraplength = 900, justify = LEFT)
AboutHead.pack()
AboutBody.pack(padx = 10)

root.mainloop()