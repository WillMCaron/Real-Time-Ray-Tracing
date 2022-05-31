# sys for sys.exit(), better for comprehension
import pygame,sys
# contains many constant variables that will be used (QUIT)
# also shorter calls in program
from pygame.locals import *
from time import sleep

pygame.init()

WIDTH = 200
HEIGHT = 100
delay = 0
windowSurface = pygame.display.set_mode((WIDTH,HEIGHT), 0, 32)
pygame.display.set_caption('Hello World')
RED = (255,0,0)
GREEN = (0,255,0)
pxarray = pygame.PixelArray(windowSurface)
pygame.display.update()

def main1():
    """The goal is to show a simple image"""
    # goes through the rows, and in each row it loops through the cols
    for rows in reversed(range(HEIGHT-1)):
      for cols in range(WIDTH-1):
        row = (HEIGHT-1)-rows
        #increment method by just calculating and setting through loops
        #Red increases across the width
        r = float(cols)/WIDTH
        #green decreases across rows
        g = float(rows)/HEIGHT
        #b is constant
        b=0.2
        # changes the range from 0,1 to 0,256
        ir = int(255.99*r)
        ig = int(255.99*g)
        ib = int(255.99*b)
        #print(ir)
        #        x      y
        pxarray[cols][row] = (ir, ig, ib)
        #print(ir,ig,ib)
        pygame.display.update()
        sleep(delay)
        
if __name__ == "__main__":
  main1()
