from tkinter import *
from PIL import Image, ImageTk

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

# Generation Counter
Generation = Label(frame3, text = f"Generation # {eight}", font=('Georgia', 16))
Generation.pack()

canvas = Canvas(frame3)
canvas.pack(pady = 10)
pilImage = Image.open("Bove Island.jpg")
image = ImageTk.PhotoImage(pilImage)
imagesprite = canvas.create_image(400,400,image=image)

# Frame3 subframe
# Frame 6
frame6 = Frame(frame3)
frame6.pack()

# Controls
Play = Button(frame6, text = "Play", font = ('Georgia', 12))
Pause = Button(frame6, text = "Pause", font = ('Georgia', 12))
Reset = Button(frame6, text = "Reset", font = ('Georgia', 12))
Play.pack(side = LEFT, padx=10)
Pause.pack(side = LEFT, padx=10)
Reset.pack(side = RIGHT, padx=10)

# Frame 4 
frame4 = Frame(frame1)
frame4.pack(side = LEFT, fill=BOTH, padx = 10, pady = 10)

# Frame 5
frame5 = Frame(frame1)
frame5.pack(side = LEFT,fill=BOTH,anchor=CENTER)

# Presets
Preset1 = Button(frame4, text = "Glider", font = ('Georgia', 12))
Preset2 = Button(frame4, text = "Random", font = ('Georgia', 12))
Preset3 = Button(frame4, text = "Space Ship", font = ('Georgia', 12))
Preset4 = Button(frame4, text = "Glider Gun", font = ('Georgia', 12))
Preset1.pack(anchor = W, pady=10)
Preset2.pack(anchor = W, pady=10)
Preset3.pack(anchor = W, pady=10)
Preset4.pack(anchor = W, pady=10)

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