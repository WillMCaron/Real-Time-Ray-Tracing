from abc import ABC, abstractmethod
from ray import Ray
from vector import Vector
#from main import random_in_unit_sphere
from math import sqrt
from random import random

def random_in_unit_sphere():
  p = 2.0*Vector(random(),random(),random()) - Vector(1,1,1)
  while (p.dot(p) >= 1.0):
    p = 2.0*Vector(random(),random(),random()) - Vector(1,1,1)
  return p

def reflect(v, n):
  return v - 2*(v.dot(n))*n

def refract(v, n, ni_over_nt, refracted):
  uv = v.normalize()
  dt = uv.dot(n)
  discriminant = 1.0 - ni_over_nt*ni_over_nt*(1-dt*dt)
  if (discriminant > 0):
    refracted = ni_over_nt*(uv - n*dt) - n*sqrt(discriminant)
    return True, refracted
  else:
    return False, refracted

def schlick (cosine, ref_idx):
  r0 = (1-ref_idx)/(1+ref_idx)
  r0 = r0*r0
  return r0 + (1-r0)*pow((1-cosine),5)

class Material(ABC):
  @abstractmethod
  def scatter(ray_in, hit_record, attentuation, scattered):
    pass

class Lambertian(Material):
  def __init__(self,albedo):
    self.albedo = albedo

  def scatter(self, ray_in, hit_record, attenuation, scattered):
    target = hit_record.p + hit_record.normal + random_in_unit_sphere()
    scattered.origin = hit_record.p
    scattered.direction = target-hit_record.p
    attenuation = self.albedo#/random()
    return True,scattered, attenuation

class Metal(Material):
  def __init__(self,albedo, fuzz):
    self.albedo = albedo
    if fuzz > 1:
      self.fuzz = 1
    else:
      self.fuzz = fuzz
  
  def scatter(self, ray_in, hit_record, attenuation,scattered):
    reflected = reflect(ray_in.direction, hit_record.normal)
    scattered.origin = hit_record.p
    scattered.direction = reflected+self.fuzz*random_in_unit_sphere()
    attenuation = self.albedo
    return (scattered.direction.dot(hit_record.normal) > 0), scattered, attenuation

class Dialectric(Material):
  def __init__(self, ri):
    self.ref_idx = ri
  
  def scatter(self,ray_in, hit_record, attenuation, scattered):
    outward_normal = Vector()
    reflected = reflect(ray_in.direction, hit_record.normal)
    ni_over_nt = 0.0
    attenuation = Vector(1.0,1.0,1.0)
    refracted = Vector
    #refracted = (refract(ray_in.direction,outward_normal,ni_over_nt,refracted))[1]
    if (ray_in.direction.dot(hit_record.normal)>0):
      outward_normal = -1*hit_record.normal
      ni_over_nt = self.ref_idx
      cosine = self.ref_idx*ray_in.direction.dot(hit_record.normal)/ray_in.direction.magnitude()
    else:
      outward_normal = hit_record.normal
      ni_over_nt = 1.0/self.ref_idx
      cosine = -1*ray_in.direction.dot(hit_record.normal)/ ray_in.direction.magnitude()
    if (refract(ray_in.direction,outward_normal,ni_over_nt,refracted))[0]:
      refracted = refract(ray_in.direction,outward_normal,ni_over_nt,refracted)[1]
      reflect_prob = schlick(cosine, self.ref_idx)
    else:
      scattered = Ray(hit_record.p,reflected)
      reflect_prob = 1.0
    if random() <reflect_prob:
      #scattered = Ray(hit_record.p, reflected)
      scattered.origin = hit_record.p
      scattered.direction = reflected
    else:
      scattered.origin = hit_record.p
      scattered.direction = refracted
    return True, scattered, attenuation

