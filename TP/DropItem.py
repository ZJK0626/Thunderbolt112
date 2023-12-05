from cmu_graphics import *

class DropItem:
    def __init__(self, x, y, dx, dy, url):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.image = url