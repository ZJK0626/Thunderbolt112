from cmu_graphics import *
import random

class Player:
    def __init__(self, name, lifePoint, attack, x, y, url):
        self.name = name
        self.lifePoint = lifePoint
        self.attack = attack
        self.x = x
        self.y = y
        self.image = url
        self.size = 100

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def shoot(self):
        pass

    def takeDamage(self, amount):
        self.lifePoint -= amount
    


class Enemy:
    def __init__(self, lifePoint, attack, url, x, y, dx, dy):
        self.lifePoint = lifePoint
        self.attack = attack
        self.x = x
        self. y = y
        self.dx = dx
        self.dy = dy
        self.image = url
     
    def drawEnemy(self):
        drawImage(self.image, self.x, self.y, align = 'center')

    def takeDamage(self,amount):
        self.lifePoint -= amount
        
    def move(self):
        self.x += self.dx
        self.y += self.dy

