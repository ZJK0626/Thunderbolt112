from cmu_graphics import *
from player_enemy import Player, Enemy
from Bullets import Bullet
from Obstacles import Obstacle
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
    app.stepsPerSecond = 30
    #Playing Status
    app.selectedPlane = app.plane1
    app.lifePoint = app.plane1.lifePoint # Class plane.lifepoint
    app.score = 0
    # app.missileNum = 0 
    app.distance = 0
    
    #Bullet Status
    app.bullets = []
    app.enemyBullet = []
    #Enemies Status
    app.enemies = []
    app.obstacles = []
    
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
    elif app.isGameOverPage:
        gameOver(app)
    elif app.isWinningPage:
        gameWinning(app)
  
def drawStartPage(app):
    drawImage(app.url, 0, 0,
             width = 600, height = 1000)
    drawRect(app.width/2, app.height/2 +200, 180, 60, align = 'center', fill = 'royalBlue', border = 'yellow', borderWidth = 5)
    drawRect(app.width/2 , app.height/2 + 280, 180, 60, align = 'center', fill = 'royalBlue', border = 'yellow', borderWidth = 5)
    drawLabel('Start Game', app.width/2, app.height/2 + 200, align = 'center', size = 24, fill = 'white', font='orbitron')
    drawLabel('About Game', app.width/2, app.height/2 + 280, align = 'center', size = 24, fill = 'white', font='orbitron')
    
def drawLevelSelectPage(app):
    app.plane1.x = 100
    app.plane1.y = 560
    #drawBackground
    drawImage('LevelSelectPage.png',0, 0, width = app.width, height = app.height)
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
    drawLabel('HP:', 30, 80, fill = 'white',size = 24)
    drawRect(55, 70, 150, 20, fill = None, border = 'white')
    drawRect(59, 74, (app.plane1.lifePoint/100)*142,13, fill = 'white')
    drawLabel(f'Score: {app.score}', 530, 80, fill = 'white', size = 24)
    #drawPlayer
    drawImage(app.plane1.image, app.plane1.x, app.plane1.y, align = 'center')
    #drawEnemies
    
    for enemy in app.enemies:
        enemy.move()
        if enemy.image == 'enemy1.png':
            if enemy.x <= 30 or enemy.x >=570 :
                enemy.dx = -enemy.dx
            elif enemy.y >= 1000:
                app.enemies.remove(enemy)
        elif enemy.image == 'Boss1.png':
            if enemy.x <= 30 or enemy.x >=480 :
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

    for obstacle in app.obstacles:
        obstacle.move()
        if obstacle.y >= 1000:
            app.obstacles.remove(obstacle)
        elif obstacle.x <= 30 or obstacle.x >= 570:
            obstacle.dx = -obstacle.dx
        obstacle.drawObstacle()


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

def gameOver(app):

    drawRect(180, 600, 120, 60, align = 'center', fill = 'royalBlue', border = 'yellow', borderWidth = 5)
    drawLabel('Retry', 180, 600, fill = 'white',size = 24)
    drawRect(420, 600, 120, 60, align = 'center', fill = 'royalBlue', border = 'yellow', borderWidth = 5)
    drawLabel('Quit', 420, 600, fill = 'white',size = 24)

def gameWinning(app):
    #
    drawRect(0, 0, app.width, app.height, fill = 'black')
    drawLabel('MISSION COMPLETE!', app.width//2, 360, fill = 'white', size = 40)
    drawLabel(f'Your Score: {app.score}', app.width//2, 440, fill = 'white', size = 24)
    drawLabel('Congradulations!', app.width//2, 500, fill = 'white', size = 22)
    drawLabel('New Level Unlocked', app.width//2, 530, fill = 'white', size = 22)

    
    drawRect(180, 600, 120, 60, align = 'center', fill = 'royalBlue', border = 'yellow', borderWidth = 5)
    drawLabel('Continue', 180, 600, fill = 'white',size = 24)
    drawRect(420, 600, 120, 60, align = 'center', fill = 'royalBlue', border = 'yellow', borderWidth = 5)
    drawLabel('Quit', 420, 600, fill = 'white',size = 24)

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
    elif app.isGameOverPage:
        if 120 <= mouseX <= 240 and 570 <= mouseY <= 630:
            app.isWinningPage = False
            app.onLevelSelectPage = True
        elif 420 <= mouseX <= 540 and 570 <= mouseY <= 630:
            app.isWinningPage = False
            app.onStartPage = True
    elif app.isWinningPage:
        if 120 <= mouseX <= 240 and 570 <= mouseY <= 630:
            app.isWinningPage = False
            app.onLevelSelectPage = True
        elif 420 <= mouseX <= 540 and 570 <= mouseY <= 630:
            app.isWinningPage = False
            app.onStartPage = True

def onMouseMove(app, mouseX, mouseY):
    if app.onStartPage or app.onLevelSelectPage or app.onAboutPage:
        pass
    elif app.onGameRunning:
        app.plane1.move(mouseX, mouseY)

def onStep(app):
    if app.onGameRunning:
        app.steps += 1

        damageEnemy(app)
        damageObstacle(app)
        damagePlayer(app)

        if app.steps % 15 == 0:
            playerShootingBullets1(app)

        if app.steps < 2000 and app.steps % 200 == 0 and len(app.enemies) < 3:
            generateEnemy1(app)
        elif app.steps == 2000:
            generateBoss1(app)
        
        if app.steps % 250 == 0:
            seed = random.randint(1, 100)
            if seed % 2 == 0:
                generateBreakableObstacle(app)
            else:
                generateUnbreakableObstacle(app)
        
        if app.enemies != [] and app.steps % 80 == 0:
            for enemy in app.enemies:
                if enemy.image == 'enemy1.png':
                    enemy1ShootingBullet(app)
                elif enemy.image == 'Boss1.png':
                    boss1ShootingBullet(app)



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

def boss1ShootingBullet(app):
    attack = 20
    dx1 = 0.6
    dx2 = -0.6
    dx3 = 0
    
    dy = 1.5
    url = 'boss1Bullet.png'

    for enemy in app.enemies:
        if enemy.image == 'Boss1.png':
            boss1BulletA = Bullet(attack, enemy.x-10, enemy.y, dx1, dy, url)
            boss1BulletB = Bullet(attack, enemy.x+10, enemy.y, dx2, dy, url)
            boss1BulletC = Bullet(attack, enemy.x, enemy.y, dx3, dy, url)
    app.enemyBullet.append(boss1BulletA)
    app.enemyBullet.append(boss1BulletB)
    app.enemyBullet.append(boss1BulletC)

def distance(x1, y1, x2, y2):
    if x1 and y1 and x2 and y2:
        return ((x1-x2)**2 + (y1-y2)**2)**0.5

def damageEnemy(app):
    for bullet in app.bullets:
        for enemy in app.enemies:
            d = distance(bullet.x, bullet.y, enemy.x, enemy.y)
            size = getImageSize(enemy.image)[0]
            if d and d <= size//2:
                enemy.takeDamage(bullet.attack)
                if enemy.lifePoint <= 0:
                    app.enemies.remove(enemy)
                    if enemy.image == 'enemy1.png':
                        app.score += 1000
                    elif enemy.image == 'Boss1.png':
                        app.unlockedLevel = 2
                        app.onGameRunning = False
                        app.isWinningPage = True
                app.bullets.remove(bullet)

def damageObstacle(app):
    for bullet in app.bullets:
        for obstacle in app.obstacles:
            d = d = distance(obstacle.x, obstacle.y, bullet.x, bullet.y)
            if d and d <= (obstacle.size//2):
                obstacle.takeDamage(obstacle.attack)
                if obstacle.lifePoint <= 0:
                    app.obstacles.remove(obstacle)
                    app.score += 500

def damagePlayer(app):
    for enemyBullet in app.enemyBullet:
        d = distance(enemyBullet.x, enemyBullet.y, app.plane1.x, app.plane1.y)
        if d and d <= 40:
            app.plane1.takeDamage(enemyBullet.attack)
            if app.plane1.lifePoint <= 0:
                app.onGameRunning = False
                app.isGameOverPage = True
            app.enemyBullet.remove(enemyBullet)

    for obstacle in app.obstacles:
        d = distance(obstacle.x, obstacle.y, app.plane1.x, app.plane1.y)
        if d and d <= 40:
            app.plane1.takeDamage(obstacle.attack)
            if app.plane1.lifePoint <= 0:
                gameOver(app)
            app.obstacles.remove(obstacle)

def generateEnemy1(app):
    lifePoint = 100
    attack = 10
    url = 'enemy1.png'

    x = random.randint(50, app.width-50)
    y = random.randint(0, app.height // 5)
    dx = random.uniform(-0.8,0.8) 
    dy = 1
    newEnemy1 = Enemy(lifePoint, attack, url, x, y, dx, dy)

    app.enemies.append(newEnemy1)

def generateBoss1(app):
    lifePoint = 300
    attack = 15
    url = 'Boss1.png'

    x = app.width//2
    y = 100
    dx = 0.4
    dy = 0
    boss1 = Enemy(lifePoint, attack, url, x, y ,dx, dy)

    app.enemies.append(boss1)

def generateBreakableObstacle(app):
    lifePoint = 200
    attack = 20
    size = random.randint(60, 90)
    x = random.randint(50, app.width-50)
    y = random.randint(0, app.height // 8)
    dx = 0
    dy = 2
    url = 'Meteorite B.png'

    newObstacle1 = Obstacle(lifePoint, attack, True, size, x, y ,dx, dy ,url)

    app.obstacles.append(newObstacle1)

def generateUnbreakableObstacle(app):
    lifePoint = 200
    attack = 15
    size = random.randint(60, 90)
    x = random.randint(50, app.width-50)
    y = random.randint(0, app.height // 8)
    dx = random.randint(-1 ,1)
    dy = 1
    url = 'Meteorite A.png'

    newObstacle2 = Obstacle(lifePoint, attack, False, size, x, y ,dx, dy ,url)

    app.obstacles.append(newObstacle2)

def main():
    runApp(width = 600, height = 1000)
    
main()