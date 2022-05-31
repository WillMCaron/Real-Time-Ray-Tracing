class Ray:
  """Ray is half line with an origin and a normalized direction"""
  def __init__(self,origin,direction):
    self.origin = origin
    self.direction = direction
    #print(self.direction)
  def point_at_parameter(self,t):
    return self.origin+t*self.direction
