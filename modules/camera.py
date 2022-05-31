from ray import Ray
from vector import Vector
from math import pi, tan
from random import random

def random_in_unit_disk():
  p = 2.0*Vector(random(),random(),0) - Vector(1,1,0)
  while (p.dot(p) >=1.0):
    p = 2.0*Vector(random(),random(),0) - Vector(1,1,0)
  return p

class Camera:
  #vfov is top to bottom in degrees
  def __init__(self, lookfrom, lookat, vup, vfov, aspect, aperature, focus_dist):
    self.lens_radius = aperature/2
    self.theta = vfov*pi/180
    self.half_height = tan(self.theta/2)
    self.half_width = aspect*self.half_height
    self.origin = lookfrom
    self.w = (lookfrom-lookat).normalize()
    self.u = (vup.cross(self.w)).normalize()
    self.v = self.w.cross(self.u)
    self.lower_left_corner = Vector(-1*self.half_width, -1*self.half_height, -1.0)
    self.lower_left_corner = self.origin - self.half_width*focus_dist*self.u - self.half_height*focus_dist*self.v - self.w*focus_dist
    self.horizontal = 2*self.half_width*focus_dist*self.u
    self.vertical = 2*self.half_height*focus_dist*self.v

  
  def get_ray(self, s, t):
    rd = self.lens_radius*random_in_unit_disk()
    offset = self.u * rd.x + self.v*rd.y
    return Ray(self.origin+offset, self.lower_left_corner + s*self.horizontal + t*self.vertical - self.origin - offset)
