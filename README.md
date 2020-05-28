# GameOfLife  

This project was a labor of love and a tribute to John Conway. I wrote a blog post outlining my external influences [here](https://ethanmjansen.github.io/2020-05-27-GOL/). The game workes based off of these three rules:  

1. Any live cell with two or three live neighbours survives.
2. Any dead cell with three live neighbours becomes a live cell.
3. All other live cells die in the next generation. Similarly, all other dead cells stay dead.  

From these rules complex behavior can emerge. Namely, the game of life is a Turing complete cellular automata. The app has a low level description of what it means to be Turing complete but a more detailed description can be found [here](https://en.wikipedia.org/wiki/Turing_machine). Alan Turing called the Turing machine an "a-machine" or an automatic machine. A Turning machine had the ability to replicate itself through the use of what he called a sequential tape that was generated in the CPU of the machine. This tape could be used as a sort of blueprint to build other machines. Turing machines were considered complete if they could answer any computable question given to them.  

Stanislav Ulim, a popular science fiction writer during the 40's created something called a cellular automata. The simplest way to describe a cellular automata is a grid of cells who have a finite number of states. In The Game of Life cells are either alive or dead. John Conway brought the ideas of a Ulim and Turing together when he made his titular game.  

## This Repo  
The aptly named `main.py` contains all of the code that was used in the meat of this application. It can be ran by using the following steps.  

1. Fork this repo.  
2. Clone this repository to your local machine.  
3. cd into the repository.  
4. `python 3 main.py`  

There are some nuances with the tKinter application. The tKinter library isn't ver intuitive and trying to make a clean layout is hard to to. I superimposed lines on a picture of the final product to show how I packed the frames into the root tk widget.  

![GOL](/img/GameOfLifeFrames.jpg)  

The app does what I intended it to do but there are some unitended features. Pressing the Play button more than once will actually increase the speed of the program but the Pause button needs to be pressed multiple times to slow the program down to actually stop. The generation counter keeps ticking after a formation has stabilized. I find this appropriate because although the automata appear static, they are continually updating. Fully pausing will result in the generation counter to stop. Pressing the reset button will clear the grid but the simulation has to be fully stopped to successfully add a new generation. There two standard presets and one random function to showcase the functionality without manual automata formation. The edge of the grid doesn't wrap around. I only look at each cell in the grid and because of that the grid has a hard edge where automata will stop. The rainbow colors can be turned off if the `paint_grid` function is edited to comment out the random color choice and bring the black fill back on line 121.  

# The Future  
I would like to implement a better speed function and allow users to toggle the rainbow mode from the app. I would imagine finding a consistent loop for every time the play button was pressed would increase the speed and then pressing pause would loop through the amount of times the play button was pressed. This would appear nearly simultaneous but have the desired effect. I also would like to find out how to stor past generations and step through the simulation one generation at a time forwards and backwards. I don't have an idea for that yet.