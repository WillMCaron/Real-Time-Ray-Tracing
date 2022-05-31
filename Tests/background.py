# sys for sys.exit(), better for comprehension
import pygame,sys
# contains many constant variables that will be used (QUIT)
# also shorter calls in program
from pygame.locals import *
from time import sleep

sys.path.append('/home/runner/PyRayTraceGame/Modules')
from vector import Vector
from ray import Ray

pygame.init()

WIDTH = 200
HEIGHT = 100
delay = 0
windowSurface = pygame.display.set_mode((WIDTH,HEIGHT), 0, 32)
pygame.display.set_caption('Background')
pxarray = pygame.PixelArray(windowSurface)
pygame.display.update()

def color(r):
  # gets direction of ray (what way is it going)
    #print(r.direction)
    direction = r.direction.normalize()
    # gets the Vector value, how far along the ray
    t = 0.5 * (direction.y +1)
    # as the y increases, the blue increases
    return (1.0-t)*Vector(1.0, 1.0, 1.0) + t*Vector(0.5, 0.7, 1.0)

def main1():
    """The goal is to show a background image"""
  # lower left corner of the screen
    lower_left_corner = Vector(-2,-1,-1)
  # the right of the screen
    horizontal = Vector(4,0,0)
  # top center of screen
    vertical = Vector(0,2,0)
  # camera center
    origin = Vector(0,0,0)
    for rows in reversed(range(HEIGHT-1)):
      for cols in range(WIDTH-1):
        row = (HEIGHT-1)-rows
        u = float(cols)/WIDTH
        v = float(rows)/HEIGHT
        r = Ray(origin, lower_left_corner + u*horizontal + v*vertical)
        # using the vector method now
        col = color(r)
        # changes the range from 0,1 to 0,256
        ir = int(255.99*col.x)
        ig = int(255.99*col.y)
        ib = int(255.99*col.z)
        #print(ir)
        #        x      y
        pxarray[cols][row] = (ir, ig, ib)
        #print(ir,ig,ib)
        pygame.display.update()
        sleep(delay)
        
if __name__ == "__main__":
  main1()
