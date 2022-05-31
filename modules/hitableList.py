from hitable import Hitable, HitRecord

class HitableList(Hitable):
  def __init__(self, hitable_objects):
    self.hitable_objects = hitable_objects
  
  def hit(self, ray, t_min, t_max, hit_record):
    temp_rec = HitRecord()
    hit_anything = False
    closest_so_far = t_max
    for item in self.hitable_objects:
      if item.hit(ray, t_min, closest_so_far, temp_rec):
        hit_anything = True
        closest_so_far = temp_rec.t
        hit_record.t = temp_rec.t
        hit_record.p = temp_rec.p
        hit_record.normal = temp_rec.normal
        hit_record.material = temp_rec.material
        
    return hit_anything
