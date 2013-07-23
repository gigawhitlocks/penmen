#!/usr/bin/python2

from scipy.misc import imread, imsave
import random

def increaserowcontrast():
    p1 = imread("penmen1rowsubset.jpg")
    for row in p1:
        for (i,pixel) in enumerate(row):
            avg = 0
            for rgb in pixel:
                avg += rgb
            avg = avg/3
            if avg > 110:
                row[i] = [255,255,255]
            else:
                row[i] = [0,0,0]


                
    imsave("processedrowoutput.jpg",p1)

increaserowcontrast()
p1 = imread("processedrowoutput.jpg")
for (height, row) in enumerate(p1):
    newpixel = [random.randint(0,255)
            ,random.randint(0,255)
            ,random.randint(0,255)]

    cont = False
    for (width, pixel) in enumerate(row):
        r, g, b = pixel
        cont = ( r == 0 )
        if cont:
            p1[height][width] = newpixel
        else:
            newpixel = [random.randint(0,255)
                    ,random.randint(0,255)
                    ,random.randint(0,255)]

        
imsave("coloredrowoutput.jpg",p1)        
