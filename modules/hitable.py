from abc import ABC, abstractmethod
from vector import Vector
class HitRecord:
  def __init__(self,t=0.0,p=Vector(),n=Vector()):
    self.t = t
    self.p = p
    self.normal = n
    self.material=None

class Hitable(ABC):
  @abstractmethod
  def hit(self,ray,t_min,t_max,hit_record):
    pass
