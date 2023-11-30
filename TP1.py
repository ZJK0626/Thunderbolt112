from cmu_graphics import *
from player_enemy import Player, Enemy
from Bullets import Bullet
import random

def onAppStart(app):
    createPlayersPlane(app)
    #Running Status
    app.onStartPage = True
    app.onLevelSelectPage = False
    app.onAboutPage = False
    app.onGameRunning = False
    
    app.isGameOverPage = False
    app.isWinningPage = False

    app.steps = 0
    app.stepsPerSecond = 100
    #Playing Status
    app.selectedPlane = app.plane1
    app.lifePoint = app.plane1.lifePoint # Class plane.lifepoint
    # app.missileNum = 0 
    app.distance = 0
    
    #Bullet Status
    app.bullets = []
    app.enemyBullet = []
    #Enemies Status
    app.enemies = []
    
    #Playing Progress
    app.unlockedLevel = 1
    app.unlockedPlane = 1
    app.currentLevel = 0
    
    #Outside Resources
    app.url = 'StartPage.png'
    app.imageWidth, app.imageHeight = getImageSize(app.url)

def createPlayersPlane(app):
    app.plane1 = Player('SpeedRunner', 100, 20, 100, 560, 'plane1.png')
    # app.plane2 = Player(150, 30, 180, 600)
    # app.plane3 = Player(300, 50, 180, 660)

def createEnemiesPlane(app):
    dx = random.randint(-1,1) 
    dy = random.randint(-0,2)
    app.enemy1 = Enemy(160, 10, 'enemy1.png', None, None, dx, dy)

def createBullets(app):
    app.bullet1 = Bullet(20, None, None, 5, 0, 'bullet1.png')
    # app.bullet2 = Bullet(30, None, None, 6, 0)

def redrawAll(app):
    if app.onStartPage:
        drawStartPage(app)
    elif app.onLevelSelectPage:
        drawLevelSelectPage(app)
    elif app.onAboutPage:
        drawAboutPage(app)
    elif app.onGameRunning:
        if app.currentLevel == 1:
            runGameLevel1(app)
        elif app.currentLevel == 2:
            pass
        elif app.currentLevel == 3:
            pass
        elif app.currentLevel == 4:
            pass
  
def drawStartPage(app):
    drawImage(app.url, 0, 0,
             width = 600, height = 1000)
    drawRect(app.width/2, app.height/2 +200, 180, 60, align = 'center', fill = 'royalBlue', border = 'yellow', borderWidth = 5)
    drawRect(app.width/2 , app.height/2 + 280, 180, 60, align = 'center', fill = 'royalBlue', border = 'yellow', borderWidth = 5)
    drawLabel('Start Game', app.width/2, app.height/2 + 200, align = 'center', size = 24, fill = 'white', font='orbitron')
    drawLabel('About Game', app.width/2, app.height/2 + 280, align = 'center', size = 24, fill = 'white', font='orbitron')
    
def drawLevelSelectPage(app):
    #drawBackground
    drawRect(0, 0, app.width, app.height, fill = 'black')
    drawLabel('Level Selection', app.width/2, 200, size = 32, fill = 'white')
    drawLabel('Plane Selection', app.width/2, 480, size = 32, fill = 'white')

    drawLabel('←', 50, 50, size = 30, fill = 'white', bold = True)
    #drawLevelSelectButton
    for i in range(app.unlockedLevel):
        drawRect(150 + i*100, 280, 60, 60, align = 'center', fill = 'royalBlue', border = 'yellow', borderWidth = 5)
        drawLabel(i+1, 150 + i*100, 280, size = 30, fill = 'white', bold = True)

    for i in range(4 - app.unlockedLevel):
        drawRect(450 - i*100, 280, 60, 60, align = 'center', fill = 'darkGray', border = 'lightYellow', borderWidth = 5)
        drawLabel(4-i, 450 - i*100, 280, size = 30, fill = 'white')
        # '▲'

    #drawPlaneSelectButton
    drawImage(app.plane1.image, app.plane1.x, app.plane1.y)
    drawLabel(app.plane1.name, app.plane1.x + 120, app.plane1.y + 10 ,align = 'left', fill = 'white',size = 30)
    drawLabel('Life Point:', app.plane1.x + 122, app.plane1.y + 50, align = 'left', fill = 'white',size = 20 )
    drawLabel('Attack Power', app.plane1.x + 120, app.plane1.y + 85, align = 'left', fill = 'white',size = 20 )


def drawAboutPage(app):
    drawRect(app.width/2, app.height/2, 280, 180, align = 'center', fill = 'royalBlue', border = 'yellow', borderWidth = 5)

#RUN GAME HERE
def runGameLevel1(app):
    #drawBackground
    drawRect(0, 0, app.width, app.height, fill = 'black')
    drawLabel(app.steps, 30, 30, fill = 'white')
    drawLabel(f'HP: {app.plane1.lifePoint}', 30, 80, size = 40)
    #drawPlayer
    drawImage(app.plane1.image, app.plane1.x, app.plane1.y, align = 'center')
    #drawEnemies
    
    for enemy in app.enemies:
        enemy.move()
        if enemy.x <= 30 or enemy.x >=570:
            enemy.dx = -enemy.dx
        enemy.drawEnemy()
    
    for bullet in app.bullets:
        bullet.move()
        if bullet.y <= 0:
            app.bullets.remove(bullet) 
        bullet.drawBullet()
    
    for enemyBullet in app.enemyBullet:
        enemyBullet.move()
        if enemyBullet.y >= 1000:
            app.enemyBullet.remove(enemyBullet)
        enemyBullet.drawBullet()


    damageEnemy(app)


def runGameLevel2(app):
    #drawBackground
    drawRect(0, 0, app.width, app.height, fill = 'black')
    #drawPlayer
    pass

def runGameLevel3(app):
    #drawBackground
    drawRect(0, 0, app.width, app.height, fill = 'black')
    #drawPlayer
    pass

def runGameLevel4(app):
    #drawBackground
    drawRect(0, 0, app.width, app.height, fill = 'black')
    #drawPlayer
    pass

def onKeyPress(app,key):
    if app.onLevelSelectPage:
        if key == 'n':
            app.onStartPage == True
            app.onLevelSelectPage = False
            

def onMousePress(app, mouseX, mouseY):
    if app.onStartPage:
        if (app.width/2-90) <=  mouseX <= (app.width/2+90) and (app.height/2 + 170) <= mouseY <= (app.height/2 + 230):
            app.onStartPage = False
            app.onLevelSelectPage = True
        elif (app.width/2-90) <=  mouseX <= (app.width/2+90) and (app.height/2 + 250) <= mouseY <= (app.height/2 + 310):
            app.onStartPage = False
            app.onAboutPage = True

    elif app.onLevelSelectPage:
        if 25 <= mouseX <= 55 and 25 <= mouseY <= 55:
            app.onLevelSelectPage = False
            app.onStartPage = True
        
        if 120 <= mouseX <= 180 and 250 <= mouseY <= 310 and app.unlockedLevel >= 1:
            app.currentLevel = 1
            app.onLevelSelectPage = False
            app.onGameRunning = True
        elif 220 <= mouseX <= 280 and 250 <= mouseY <= 310 and app.unlockedLevel >= 2:
            app.currentLevel = 2
            app.onLevelSelectPage = False
            app.onGameRunning = True
        elif 320 <= mouseX <= 380 and 250 <= mouseY <= 310 and app.unlockedLevel >= 3:
            app.currentLevel = 3
            app.onLevelSelectPage = False
            app.onGameRunning = True
        elif 320 <= mouseX <= 380 and 250 <= mouseY <= 310 and app.unlockedLevel >= 4:
            app.currentLevel = 4
            app.onLevelSelectPage = False
            app.onGameRunning = True
            
    elif app.onAboutPage:
        pass
    elif app.onGameRunning:
        pass

def onMouseMove(app, mouseX, mouseY):
    if app.onStartPage or app.onLevelSelectPage or app.onAboutPage:
        pass
    elif app.onGameRunning:
        app.plane1.move(mouseX, mouseY)

def onStep(app):
    if app.onGameRunning:
        app.steps += 1
        if app.steps % 15 == 0:
            playerShootingBullets1(app)
        if app.steps % 300 == 0 and len(app.enemies) < 3:
            generateEnemy1(app)

        if app.enemies != [] and app.steps % 80 == 0:
            enemy1ShootingBullet(app)


def playerShootingBullets1(app):
    attack = 20
    dx = 0
    dy = -3
    url = 'bullet1.png'
    newBullet1 = Bullet(attack, app.plane1.x, app.plane1.y-50, dx, dy, url)
    
    app.bullets.append(newBullet1)

def enemy1ShootingBullet(app):
    attack = 10
    dx = 0
    dy = 3
    url = 'enemy1Bullet.png'
    
    for enemy in app.enemies:
        if enemy.image == 'enemy1.png': 
            newEnemy1Bullet = Bullet(attack, enemy.x, enemy.y, dx, dy, url)

    app.enemyBullet.append(newEnemy1Bullet)

def distance(x1, y1, x2, y2):
    if x1 and y1 and x2 and y2:
        return ((x1-x2)**2 + (y1-y2)**2)**0.5

def damageEnemy(app):
    for bullet in app.bullets:
        for enemy in app.enemies:
            d = distance(bullet.x, bullet.y, enemy.x, enemy.y)
            if d and d <= 30:
                enemy.takeDamage(bullet.attack)
                if enemy.lifePoint <= 0:
                    app.enemies.remove(enemy)
                app.bullets.remove(bullet)

def damagePlayer(app):
    for enemyBullet in app.enemyBullet:
        d = distance(enemyBullet.x, enemyBullet.y, enemy.x, enemy.y)

def generateEnemy1(app):
    lifePoint = 100
    attack = 10
    url = 'enemy1.png'

    x = random.randint(50, app.width-50)
    y = random.randint(0, app.height // 5)
    dx = random.randint(-2,2) 
    dy = 1
    newEnemy1 = Enemy(lifePoint, attack, url, x, y, dx, dy)

    app.enemies.append(newEnemy1)

def main():
    runApp(width = 600, height = 1000)
    

main()