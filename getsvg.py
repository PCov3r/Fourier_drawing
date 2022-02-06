from cv2 import *
from svgpathtools import svg2paths2,wsvg

# Extract path from svg
def fromsvg(path):
    paths, attributes, svg_attributes = svg2paths2(path)
    # take the first path
    path = paths[0]

    n = 700  # number of samples

    pts = []
    # add points affixes 
    for i in range(0,n+1):
        f = i/n
        complex_point = path.point(f)
        pts.append(complex(complex_point.real,complex_point.imag))

    return(pts)
