import matplotlib.pyplot as plt
import numpy as np
from cmath import *

angle = np.linspace(0,2*np.pi,360, endpoint=False)
drawx = []
drawy = []

# Add a point on a circle of radius r with a phase of phi + theta
# In the following functions, theta is used as phase #0, and phi is increasing or decreasing to move the point
def radius_point(phi, r, theta):
    return np.array([r*np.cos(phi+theta), r*np.sin(phi+theta)])

  
# Calculate the points and circle from the complex Fourier coefficients
def processpath(coeff):
    # create a figure with an axes
    fig, ax = plt.subplots()
    # set equal aspect such that the circle is not shown as ellipse
    ax.set_aspect("equal")
    
    # create the origin point of the drawing
    point0, = ax.plot(0,0, marker="o")

    Pointlist = [point0]
    Circlelist = []
    Thetalist = []
    # size will be used to adapt the plot window limits
    size = 0

    # drawpt is the point used to draw the final shape
    drawpt, = ax.plot([],[],'g-')
    x = 0
    y = 0
    h = len(coeff) // 2
    for l in range(1, h+1):
        size += abs(coeff[l])+abs(coeff[-l])
        # add the circle associated with coefficient c[-l], whose origin is the previous point
        circlek = plt.Circle((x,y), abs(coeff[l]), color='r', fill=False)
        ax.add_patch(circlek)
        Circlelist += [circlek]
        # add the next point on the previous circle
        x += abs(coeff[l])*np.cos(phase(coeff[l]))
        y += abs(coeff[l])*np.sin(phase(coeff[l]))
        pointk, = ax.plot(x,y, marker="o")
        Thetalist += [phase(coeff[l])]

        # add the circle associated with coefficient c[-l], whose origin is the previous point
        circlekm = plt.Circle((x,y), abs(coeff[-l]), color='r', fill=False)
        ax.add_patch(circlekm)
        Circlelist += [circlekm]
        # add the next point on the previous circle
        x += abs(coeff[-l])*np.cos(phase(coeff[-l]))
        y += abs(coeff[-l])*np.sin(phase(coeff[-l]))
        pointkm, = ax.plot(x,y, marker="o")
        Thetalist += [phase(coeff[-l])]
        
        Pointlist += [pointk, pointkm]

    # set fig limits to 80% of the sum of the circles radius
    ax.set_ylim([-0.8*size, 0.8*size])
    ax.set_xlim([-0.8*size, 0.8*size])

    return(fig, ax, drawpt, Pointlist, Circlelist, Thetalist)


# Draw the shape using epicycloids
def update(i, ax, drawpt, Pointlist, Circlelist, Thetalist):

    end = len(Pointlist)//2
    for l in range (1,end+1):
        # k is used to set the rotation speed of the circle
        k = (i*l)%360
        phi = angle[k]
        # obtain previous point coordinates
        x,y = radius_point(phi,Circlelist[2*l-2].radius, Thetalist[2*l-2])
        x += Circlelist[2*l-2].center[0]
        y += Circlelist[2*l-2].center[1]
        # set new point coordinates
        Pointlist[2*l-1].set_data([x],[y])
        Circlelist[2*l-1].center = (x,y)

        # obtain previous point coordinates
        x,y = radius_point(-phi,Circlelist[2*l-1].radius, Thetalist[2*l-1])
        x += Circlelist[2*l-1].center[0]
        y += Circlelist[2*l-1].center[1]
        # set new point's coordinates
        Pointlist[2*l].set_data([x],[y])
        # if the current point is the last, there is no circle attached to it
        if(l != end):
            Circlelist[2*l].center = (x,y)

    # draw the shape
    drawx.append(x)
    drawy.append(y)
    drawpt.set_data(drawx,drawy)

    # clear all epicycloids at the end
    if(i == 360):
        clearfig(Pointlist, Circlelist)

        
# Hide the circles and points
# Useful to reduce lagging
def hidefig(Pointlist, Circlelist):
    end = len(Pointlist)
    for l in range (end):
        Pointlist[l].set_visible(False)
        if(l < end-1):
            Circlelist[l].set_visible(False)

# Clear circles and points from figure
def clearfig(Pointlist, Circlelist):
    end = len(Pointlist)
    for l in range (end):
        Pointlist[l].remove()
        if(l < end-1):
            Circlelist[l].remove()

