from cmu_graphics import *
import math

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
        drawImage(self.image, self.x, self.y, align = 'center')

class Bullet2:
    def __init__(self, attack, x, y, angle, speed, amplitude, frequency, url):
        self.attack = attack
        self.x = x
        self.y = y
        self.angle = angle
        self.speed = speed
        self.amplitude = amplitude
        self.frequency = frequency
        self.time = 0
        self.image = url

    def move(self):
        self.time += 1
        self.x += math.cos(self.angle) * self.speed
        self.y += math.sin(self.angle) * self.speed + self.amplitude * math.sin(self.frequency * self.time)

    def drawBullet(self):
        drawImage(self.image, self.x, self.y, align ='center')