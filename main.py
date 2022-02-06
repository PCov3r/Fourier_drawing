#!/usr/bin/env python

import sys
from matplotlib.animation import FuncAnimation
from getsvg import *
from fourierseries import *
from draw import *


def main(path, order, show=True):
    pts = fromsvg(path)
    coeff = computeCoeff(pts, order)
    fig, ax, epi, Pointlist, Circlelist, Thetalist = processpath(coeff)
    if(show == False):
        hidefig(Pointlist, Circlelist)
    ani = FuncAnimation(fig, update, interval=1, blit=False, repeat=False, frames=361, fargs=[ax, epi, Pointlist, Circlelist, Thetalist])
    # Uncomment the following if you want to save the result as a gif
    #ani.save('./animation.gif', writer='pillow', fps=30)

    plt.show()

    
if __name__ == "__main__":
    if (len(sys.argv) < 3):
        print("Not enough argument: python -m main path order [show]")
        exit()
    path = sys.argv[1]
    order = int(sys.argv[2])
    if (len(sys.argv) > 3):
        if (sys.argv[3].lower() in ['true', '1']):
            main(path, order, True)
        else :
            main(path, order, False)
    else:
        main(path, order)
