import math

class Vector:
  def __init__(self, x = 0.0, y = 0.0, z = 0.0):
    self.x = x
    self.y = y 
    self.z = z
  
  # string rep of vector
  def __str__(self):
    return "({},{},{})".format(self.x,self.y,self.z)
  
  def dot(self, other):
    return self.x * other.x + self.y * other.y + self.z * other.z
  
  def magnitude(self):
    return math.sqrt(self.dot(self))
  
  def normalize(self):
    return self / self.magnitude()
  
  # operator overloading
  
  def __add__(self,other):
    return Vector(self.x+other.x, self.y+other.y, self.z+other.z)

  def __sub__(self,other):
    return Vector(self.x-other.x, self.y-other.y, self.z-other.z)
  
  def __mul__(self,other):
    assert not isinstance(other, Vector)
    return Vector(self.x*other, self.y*other, self.z*other)
  
  def __rmul__(self,other):
    return self.__mul__(other)
  
  def mul(self,other):
    return Vector(self.x*other.x, self.y*other.y, self.z*other.z)

  def __truediv__(self, other):
    assert not isinstance(other, Vector)
    return Vector(self.x/other, self.y/other, self.z/other)
  
  def cross(self,v2):
    return Vector((self.y*v2.z - self.z*v2.y),
                -1*(self.x*v2.z - self.z*v2.x),
                  (self.x*v2.y - self.y*v2.x))
