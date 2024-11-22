class Vector:
    def __init__(self, x=0, y=0):
        """Initialize a vector with x and y coordinates."""
        self.x = x
        self.y = y
    
    def __str__(self):
        """Return string representation of the vector."""
        return f'Vector({self.x}, {self.y})'
    
    def __add__(self, other):
        """Return the sum of two vectors."""
        return Vector(self.x + other.x, self.y + other.y)
    
    def __mul__(self, scalar):
        """Return the product of vector and a scalar."""
        return Vector(self.x * scalar, self.y * scalar)
        
    def dot(self, other):
        """Return the dot product of two vectors."""
        return self.x * other.x + self.y * other.y

# Test code
v1 = Vector(2, 3)
v2 = Vector(1, 1)

print(f"v1: {v1}")
print(f"v2: {v2}")
print(f"v1 + v2 = {v1 + v2}")
print(f"v1 * 2 = {v1 * 2}")
print(f"v1 · v2 = {v1.dot(v2)}")
