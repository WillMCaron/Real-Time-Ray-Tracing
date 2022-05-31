from math import sqrt
from hitable import Hitable

class Sphere(Hitable):
  def __init__(self, center, radius, material):
    self.center = center
    self.radius = radius
    self.material = material
  
  def hit(self,ray, t_min, t_max, hit_record):
    sphere_to_ray = ray.origin-self.center
    #print(ray.direction)
    a = ray.direction.dot(ray.direction)
    b = sphere_to_ray.dot(ray.direction)
    c = sphere_to_ray.dot(sphere_to_ray) - self.radius * self.radius
    discriminant = b*b -a*c
    if discriminant > 0:
      temp = (-b - sqrt(b*b-a*c))/(a)
      if (temp < t_max and temp > t_min):
        hit_record.t = temp
        hit_record.p = ray.point_at_parameter(hit_record.t)
        hit_record.normal = (hit_record.p - self.center) / self.radius
        hit_record.material = self.material
        return True
      temp = (-b + sqrt(b*b-a*c))/(a)
      if (temp < t_max and temp > t_min):
        hit_record.t = temp
        hit_record.p = ray.point_at_parameter(hit_record.t)
        hit_record.normal = (hit_record.p - self.center) / self.radius
        hit_record.material = self.material
        return True
    return False
