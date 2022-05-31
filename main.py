# sys for sys.exit(), better for comprehension
import pygame,sys
# contains many constant variables that will be used (QUIT)
# also shorter calls in program
from pygame.locals import *
from time import sleep
from math import sqrt, pi, cos

sys.path.append('/home/runner/PyRayTraceGame/Modules')
from sphere import Sphere
from vector import Vector
from random import uniform
from camera import Camera
from material import Lambertian, Metal, Dialectric
from random import random
from hitable import HitRecord
from hitablelist import HitableList
from ray import Ray

pygame.init()

WIDTH = 400
HEIGHT = 300
delay = 0
ns = 1
aperature = 0.1
windowSurface = pygame.display.set_mode((WIDTH,HEIGHT), 0, 32)
pygame.display.set_caption('Basic Sphere')
pxarray = pygame.PixelArray(windowSurface)
pygame.display.update()


def random_in_unit_sphere():
  p = 2.0*Vector(random(),random(),random()) - Vector(1,1,1)
  while (p.dot(p) >= 1.0):
    p = 2.0*Vector(random(),random(),random()) - Vector(1,1,1)
  return p
  

def color (r, world, depth=0):
  hit_record = HitRecord()
  if world.hit(r,0.001, sys.float_info.max, hit_record):
    scattered = Ray(Vector(),Vector())
    #!#
    attenuation = Vector()
    hit = hit_record.material.scatter(r, hit_record, attenuation, scattered)
    scattered = hit[1]
    attenuation =  hit[2]
    if (depth < 50 and hit[0]):
      return attenuation.mul(color(scattered, world, depth+1))#.mul(hit[1])
    else:
      return Vector()
  else:
    # gets direction of ray (what way is it going)
    #print(r.direction)
    direction = r.direction.normalize()
    # gets the Vector value, how far along the ray
    t = 0.5 * (direction.y +1)
    # as the y increases, the blue increases
    return (1.0-t)*Vector(1.0, 1.0, 1.0) + t*Vector(0.5, 0.7, 1.0)


def random_scene():
  n = 500
  listn = []
  listn.append(Sphere(Vector(0,-1000,0),1000,Lambertian(Vector(0.5,0.5,0.5))))
  #i = 1
  for a in range(-11,11,1):
    for b in range(-11,11,1):
      choose_mat = random()
      center = Vector(a+.9*random(),0.2,b+.9*random())
      if ((center-Vector(4,0.2,0)).magnitude() > 0.9):
        if choose_mat <0.8: #Diffuse
          listn.append(Sphere(center,0.2,Lambertian(Vector(random()*random(),random()*random(),random()*random()))))
        elif choose_mat < 0.95: # Metal
          listn.append(Sphere(center,0.2,Metal(Vector(0.5*(1+random()),0.5**1+random(), 0.5*(1+random())),0.5*random())))
        else: # glass
          listn.append(Sphere(center,0.2, Dialectric(1.5)))

  listn.append(Sphere(Vector(0,1,0),1.0, Dialectric(1.5)))
  listn.append(Sphere(Vector(-4,1,0),1.0, Lambertian(Vector(0.4,0.2,0.1))))
  listn.append(Sphere(Vector(4,1,0),1.0, Metal(Vector(0.7,0.6,0.5),0.0)))
  return listn



def main():
    """The goal is to show a sphere on an image"""
  # lower left corner of the screen
    lower_left_corner = Vector(-2,-1,-1)
  # the right of the screen
    horizontal = Vector(4,0,0)
  # top center of screen
    vertical = Vector(0,2,0)
  # camera center
    origin = Vector(0,0,0)

    # number samples
    listn = []
    #listn = random_scene()
    #listn.append(Sphere(Vector(0,1,0),1,Lambertian(Vector(1,.2,.1))))
    listn.append(Sphere(Vector(0,1,0),1,Metal(Vector(.7,.6,.5),0)))
    listn.append(Sphere(Vector(0,-1000,0),1000,Lambertian(Vector(0.5,0.5,0.5))))

    world = HitableList(listn)


    lookfrom = Vector(0,2,-15)
    lookat = Vector(0,0,0)
    dist_to_focus = (lookfrom-lookat).magnitude()
    #aperature = 2.0

    cam = Camera(lookfrom, lookat,Vector(0,1,0),20,float(WIDTH)/float(HEIGHT), aperature, dist_to_focus)
  
    for rows in reversed(range(HEIGHT-1)):
      row = (HEIGHT-1)-rows
      for cols in range(WIDTH-1):
        col = Vector()
        for s in range(ns):
            u = float(cols+uniform(0,.99)) / WIDTH
            v = float(rows+uniform(0,.99)) / HEIGHT
            r = cam.get_ray(u, v)
            
            col += color(r,world,0)
        col /= ns
        col = Vector(sqrt(col.x), sqrt(col.y),sqrt(col.z))
        ir = int(255.99*col.x)
        if ir > 255:
          ir = 255
        ig = int(255.99*col.y)
        if ig > 255:
          ig = 255
        ib = int(255.99*col.z)
        if ib > 255:
          ib = 255
        #        x      y
        #print(cols,row,(ir,ig,ib))
        pxarray[cols][row] = (ir, ig, ib)
        #print(ir,ig,ib)
        pygame.display.update()
        sleep(delay)
      print("\t",int(100-(rows/HEIGHT)*100),"%", end = "\r")
        
if __name__ == "__main__":
  main()
