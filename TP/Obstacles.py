from cmu_graphics import *
import random

class Obstacle:
    def __init__(self, lifePoint, attack, breakability, size, x, y, dx, dy, url):
        self.lifePoint = lifePoint
        self.attack = attack
        self.breakability = breakability
        self.size = size
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.image = url

    def takeDamage(self, amount):
        if self.breakability:
            self.lifePoint -= amount

    def move(self):
        self.x += self.dx
        self.y += self.dy
    
    def drawObstacle(self):
        drawImage(self.image, self.x, self.y, width = self.size, height = self.size, align = 'center')

