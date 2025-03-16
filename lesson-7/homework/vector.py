import math

class Vector:
    def __init__(self,*args):
        self.dim=list(args)
    def __add__(self,other):
        if len(self.dim)!=len(other.dim):
            raise ValueError("Dimentions don't match for addition")
        return Vector(*(self.dim[i]+other.dim[i] for i in range(len(self.dim))))
    
    def __sub__(self,other):
        if len(self.dim)!=len(other.dim):
            raise ValueError("Dimentions don't match for subtraction")
        return Vector(*(self.dim[i]-other.dim[i] for i in range(len(self.dim))))
    
    def __mul__(self,other):
        if isinstance(other,Vector):
            if len(self.dim)!=len(other.dim):
                raise ValueError("Dimentions don't match for multiplication")
            return sum(self.dim[i]*other.dim[i] for i in range(len(self.dim)))
        elif isinstance(other,(float,int)):
            return Vector(*(other*i for i in self.dim))
        else:
            raise TypeError("Data types are not supported for multiplication")
    
    def magnitude(self):
        return math.sqrt(sum(i**2 for i in self.dim))
    
    def normalize(self):
        magnitude=self.magnitude()
        if magnitude==0:
            raise ValueError("Cannot normalize a zero vector")
        l=(round(i/magnitude,3) for i in self.dim)
        return Vector(*l)

        
    def __str__(self):
        return "Vector(" + ", ".join(map(str,self.dim))+")"
    



