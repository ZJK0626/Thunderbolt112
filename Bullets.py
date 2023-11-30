from cmu_graphics import *

class Bullet:
    def __init__(self, attack, x, y, dx, dy, url):

        self.attack = attack
        # self.velocity = velocity
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.image = url

    def move(self):
        self.x += self.dx
        self.y += self.dy

    def drawBullet(self):
        drawImage(self.image, self.x, self.y)