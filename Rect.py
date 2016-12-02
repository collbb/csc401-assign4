class Rect:
    def __init__(self, le, wi):
        self.length = le
        self.width = wi

    def area (self):
        return self.length * self.width
    
class Box (Rect):
    def __init__(self, he):
        self.length = 5
        self.width = 4
        self.height = he
        

