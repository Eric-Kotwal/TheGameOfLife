#!/usr/bin/python2

import sys
import time
import random
import Tkinter
import matplotlib
import matplotlib.pyplot as plt

# ------------------------- #

clrarena = 'black'
clrpltbg = '#4B5320'
clrpltfg = 'yellow'

# ------------------------- #

GRID = 120

arena = None
mplfgr = None

valPixelT0 = [[0 for PixelCol in range(GRID)] for PixelRow in range(GRID)]
valPixelT1 = [[0 for PixelCol in range(GRID)] for PixelRow in range(GRID)]

mplX = []
mplY = []

blnPlay = False

# ------------------------- #

def defT0toMPL():
# ---------- #
    global mplX, mplY 
# ---------- #
    mplX[:] = []
    mplY[:] = []
    for PixelRow in range(GRID):
        for PixelCol in range(GRID):
            if valPixelT0[PixelRow][PixelCol] == 1:
                mplX.append(PixelCol)
                mplY.append(PixelRow)
                
# ------------------------- #

def defbtnRandom():
# ---------- #
    global valPixelT0
# ---------- #
    valPixelT0 = [[random.randint(0,1) for PixelCol in range(GRID)] for PixelRow in range(GRID)]
    defT0toMPL()
    defPlotUpdate()

# ------------------------- #

def defbtnPlay():
# ---------- #
    global blnPlay
# ---------- #
    blnPlay = True

# ------------------------- #

def defbtnExit():
    defInTheEnd()

# ------------------------- #

def defPlotUpdate():
# ---------- #
    global mplfgr 
    global mplX, mplY 
# ---------- #
    try:
        plt.plot(mplX, mplY, 'o', color=clrpltfg, marker='.')
        plt.xlim(-3,GRID+3)
        plt.ylim(-3,GRID+3)
        plt.axis('off')
    except:
        defInTheEnd()
    
# ------------------------- #

def defLiveOrDie():

    for PixelRow in range(GRID):
        for PixelCol in range(GRID):
            total1s = valPixelT0[(PixelRow-1)%GRID][(PixelCol-1)%GRID] + \
                      valPixelT0[(PixelRow-1)%GRID][(PixelCol)] + \
                      valPixelT0[(PixelRow-1)%GRID][(PixelCol+1)%GRID] + \
                      valPixelT0[(PixelRow)][(PixelCol-1)%GRID] + \
                      valPixelT0[(PixelRow)][(PixelCol+1)%GRID] + \
                      valPixelT0[(PixelRow+1)%GRID][(PixelCol-1)%GRID] + \
                      valPixelT0[(PixelRow+1)%GRID][(PixelCol)] + \
                      valPixelT0[(PixelRow+1)%GRID][(PixelCol+1)%GRID]

            if valPixelT0[PixelRow][PixelCol] == 1:
                if (total1s < 2) or (total1s > 3):
                    valPixelT1[PixelRow][PixelCol] = 0
                else:
                    valPixelT1[PixelRow][PixelCol] = 1
            else:
                if total1s == 3:
                    valPixelT1[PixelRow][PixelCol] = 1
                else:
                    valPixelT1[PixelRow][PixelCol] = 0

    for PixelRow in range(GRID):
        for PixelCol in range(GRID):
            valPixelT0[PixelRow][PixelCol] = valPixelT1[PixelRow][PixelCol]

    defT0toMPL()
    defPlotUpdate()

# ------------------------- #

def defInTheEnd():
# ---------- #
    global arena
# ---------- #
    try:
        arena.destroy()
    except:
        pass
    else:
        plt.close('all')
        sys.exit()

# ------------------------- #
    
def main():
# ---------- #
    global arena
# ---------- #
    try:
        arena.update()
    except:
        sys.exit()
# ---------- #
    time.sleep(0.1)
# ---------- #
    if blnPlay == True:
        defLiveOrDie()

# ------------------------- #

if __name__ == "__main__":
# ---------- #
    time.sleep(0.1)
# ---------- #

    arena = Tkinter.Tk()
    arena.title('GOL')
    arena.geometry('12x12')
    arena.attributes('-fullscreen', True)
    arena.resizable(0, 0)
    arena.config(bg=clrarena)
    arena.lift()

# ---------- #

    mplfgr.canvas.set_window_title('The Game of Life')
    mplfgr.set_size_inches(7.5,7.5)
    mplfgr.set_facecolor(clrpltbg)

    plt.plot(mplX, mplY, 'o', color=clrpltfg, marker='.')
    plt.xlim(-3,GRID+3)
    plt.ylim(-3,GRID+3)
    plt.axis('off')

    mplfgr.show()

# ---------- #

    time.sleep(1.5)
    defbtnRandom()
    time.sleep(3)
    defbtnPlay()

# ---------- #
    while True:
        main()

# ------------------------- #
