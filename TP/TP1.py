from cmu_graphics import *
from player_enemy import Player, Enemy
from Bullets import Bullet
from Obstacles import Obstacle
import random
import math

'''
Reference: 1. Art resources are created by DALL·E https://chat.openai.com
'''

def onAppStart(app):
    createPlayersPlane(app)
    #Running Status
    app.onStartPage = True
    app.onLevelSelectPage = False
    app.onAboutPage = False
    app.onGameRunning = False
    
    app.isGameOverPage = False
    app.isWinningPage = False

    app.steps = 3000
    app.stepsPerSecond = 30

    app.selectingPlane1 = False
    app.selectingPlane2 = False
    #Playing Status
    app.selectedPlane = app.plane1
    app.bulletType = 1
    app.lifePoint = app.plane1.lifePoint # Class plane.lifepoint
    app.score = 0
    app.targetX = app.width//2
    app.targetY = 800
    # app.missileNum = 0 
    app.distance = 0
    
    #Bullet Status
    app.bullets = []
    app.enemyBullet = []
    #Enemies Status
    app.enemies = []
    app.obstacles = []
    
    #Playing Progress
    app.unlockedLevel = 2
    app.unlockedPlane = 2
    app.currentLevel = 0
    
    #Outside Resources
    app.url = 'StartPage.png'
    app.imageWidth, app.imageHeight = getImageSize(app.url)

def createPlayersPlane(app):
    app.plane1 = Player('SpeedRunner', 200, 20, 100, 560, 'plane1.png')
    app.plane2 = Player('DawnBreaker', 150, 30, 100, 720, 'plane2.png')
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
            runGameLevel2(app)
        elif app.currentLevel == 3:
            runGameLevel3(app)
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
        drawRect(150 + i*150, 280, 60, 60, align = 'center', fill = 'royalBlue', border = 'yellow', borderWidth = 5)
        drawLabel(i+1, 150 + i*150, 280, size = 30, fill = 'white', bold = True)

    for i in range(3 - app.unlockedLevel):
        drawRect(450 - i*150, 280, 60, 60, align = 'center', fill = 'darkGray', border = 'lightYellow', borderWidth = 5)
        drawLabel(3-i, 450 - i*150, 280, size = 30, fill = 'white')
        # '▲'

    #drawPlaneSelectButton
    drawImage(app.plane1.image, app.plane1.x, app.plane1.y)
    drawLabel(app.plane1.name, app.plane1.x + 120, app.plane1.y + 10 ,align = 'left', fill = 'white',size = 30)
    drawLabel('Life Point: 100', app.plane1.x + 122, app.plane1.y + 50, align = 'left', fill = 'white',size = 20 )
    drawLabel('Attack Power: 20', app.plane1.x + 120, app.plane1.y + 85, align = 'left', fill = 'white',size = 20 )

    drawImage(app.plane2.image, app.plane2.x, app.plane2.y)
    drawLabel(app.plane2.name, app.plane2.x + 120, app.plane2.y + 15 ,align = 'left', fill = 'white',size = 30)
    drawLabel('Life Point: 150', app.plane2.x + 122, app.plane2.y + 55, align = 'left', fill = 'white',size = 20 )
    drawLabel('Attack Power: 30', app.plane2.x + 120, app.plane2.y + 90, align = 'left', fill = 'white',size = 20 )
    if app.unlockedPlane == 1:
        drawRect(app.width//2, 780, 450, 150, align = 'center', fill = 'darkGray', border = 'lightYellow', borderWidth = 6, opacity = 90)
        drawLabel('Pass Level 1 to Unlock', app.width//2, 780, fill = 'gold', size = 32)
    
    if app.selectingPlane1:
        drawRect(app.width//2, 600, 450, 150, align = 'center', fill = None, border = 'gold', borderWidth = 4)
    elif app.selectingPlane2:
        drawRect(app.width//2, 760, 450, 150, align = 'center', fill = None, border = 'gold', borderWidth = 4)

    if app.selectedPlane == app.plane1:
        drawRect(app.width//2, 600, 450, 150, align = 'center', fill = 'royalBlue', border = 'yellow',opacity = 30, borderWidth = 4)
    elif app.selectedPlane == app.plane2:
        drawRect(app.width//2, 760, 450, 150, align = 'center', fill = 'royalBlue', border = 'yellow',opacity = 30, borderWidth = 4)

def drawAboutPage(app):
    drawRect(app.width/2, app.height/2, 280, 180, align = 'center', fill = 'royalBlue', border = 'yellow', borderWidth = 5)

#RUN GAME HERE
#Linked to redrawAll
def runGameLevel1(app):
    if app.selectedPlane == app.plane1:
        plane = app.plane1
    else:
        plane = app.plane2
    #drawBackground
    drawRect(0, 0, app.width, app.height, fill = 'black')
    drawScrollBG(app)
    drawLabel(app.steps, 30, 30, fill = 'white')
    drawLabel('HP:', 30, 80, fill = 'white',size = 24)
    drawRect(55, 70, 150, 20, fill = None, border = 'white')
    drawRect(59, 74, (plane.lifePoint/100)*142,13, fill = 'white')
    drawLabel(f'Score: {app.score}', 530, 80, fill = 'white', size = 24)
    #drawPlayer
    drawImage(plane.image, plane.x, plane.y, align = 'center')
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
    if app.selectedPlane == app.plane1:
        plane = app.plane1
    else:
        plane = app.plane2
    #drawBackground
    drawRect(0, 0, app.width, app.height, fill = 'black')
    drawScrollBG(app)
    drawLabel(app.steps, 30, 30, fill = 'white')
    drawLabel('HP:', 30, 80, fill = 'white',size = 24)
    drawRect(55, 70, 150, 20, fill = None, border = 'white')
    drawRect(59, 74, (plane.lifePoint/100)*142,13, fill = 'white')
    drawLabel(f'Score: {app.score}', 530, 80, fill = 'white', size = 24)
    #drawPlayer
    drawImage(plane.image, plane.x, plane.y, align = 'center')

    for enemy in app.enemies:
        enemy.move()
        if enemy.image == 'enemy1.png':
            if enemy.x <= 30 or enemy.x >=570 :
                enemy.dx = -enemy.dx
            elif enemy.y >= 1000:
                app.enemies.remove(enemy)
        elif enemy.image == 'enemy2.png':
            if enemy.x <= 33 or enemy.x >=567 :
                enemy.dx = -enemy.dx
            elif enemy.y >= 1000:
                app.enemies.remove(enemy)
        elif enemy.image == 'Boss2.png':
            if enemy.x <= 30 or enemy.x >=450 :
                enemy.dx = -enemy.dx
        enemy.drawEnemy()
    
    for bullet in app.bullets:
        bullet.move()
        if bullet.y <= 0:
            app.bullets.remove(bullet) 
        bullet.drawBullet()
    
    for enemyBullet in app.enemyBullet:
        enemyBullet.move()
        if enemyBullet.image == 'enemy2Bullet.png':
            newDx = plane.x - enemyBullet.x
            d = distance(plane.x, plane.y, enemyBullet.x, enemyBullet.y)
            newDx /= d
            sinWave = math.sin(app.steps / 50 * math.pi)*3
            enemyBullet.dx = newDx * 2 + sinWave
            enemyBullet.dy = 3
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

def runGameLevel3(app):
    #drawBackground
    drawRect(0, 0, app.width, app.height, fill = 'black')
    #drawPlayer
    pass


def gameOver(app):
    #Draw BackGround
    drawImage('Page.png',0, 0, width = app.width, height = app.height)
    drawLabel('GAME OVER!', app.width//2, 360, fill = 'white', size = 40)
    drawLabel(f'Your Score: {app.score}', app.width//2, 440, fill = 'white', size = 24)
    drawRect(180, 600, 120, 60, align = 'center', fill = 'royalBlue', border = 'yellow', borderWidth = 5)
    drawLabel('Retry', 180, 600, fill = 'white',size = 24)
    drawRect(420, 600, 120, 60, align = 'center', fill = 'royalBlue', border = 'yellow', borderWidth = 5)
    drawLabel('Quit', 420, 600, fill = 'white',size = 24)

def gameWinning(app):
    #Draw BackGround
    drawImage('Page.png',0, 0, width = app.width, height = app.height)
    drawLabel('MISSION COMPLETE!', app.width//2, 360, fill = 'white', size = 40)
    drawLabel(f'Your Score: {app.score}', app.width//2, 440, fill = 'white', size = 24)
    drawLabel('Congratulations!', app.width//2, 500, fill = 'white', size = 22)
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
            
def drawScrollBG(app):
    step = app.steps % 1000
    drawImage('BG1.png', 0, step, width = 600, height = 1000)
    drawImage('BG1.png', 0, step - 1000, width = 600, height = 1000)

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
        elif 270 <= mouseX <= 330 and 250 <= mouseY <= 310 and app.unlockedLevel >= 2:
            app.currentLevel = 2
            app.onLevelSelectPage = False
            app.onGameRunning = True
        elif 420 <= mouseX <= 480 and 250 <= mouseY <= 310 and app.unlockedLevel >= 3:
            app.currentLevel = 3
            app.onLevelSelectPage = False
            app.onGameRunning = True
        
        if 75 <= mouseX <= 525 and 550 <= mouseY <= 670:
            app.selectedPlane = app.plane1
        elif 75 <= mouseX <= 525 and 705 <= mouseY <= 855 and app.unlockedPlane == 2:
            app.selectedPlane = app.plane2
            
    elif app.onAboutPage:
        pass
    elif app.onGameRunning:
        pass
    elif app.isGameOverPage:
        if 120 <= mouseX <= 240 and 570 <= mouseY <= 630:
            app.isWinningPage = False
            app.onLevelSelectPage = True
            app.score = 0
        elif 360 <= mouseX <= 480 and 570 <= mouseY <= 630:
            app.isWinningPage = False
            app.onStartPage = True
            app.score = 0
    elif app.isWinningPage:
        if 120 <= mouseX <= 240 and 570 <= mouseY <= 630:
            app.isWinningPage = False
            app.onLevelSelectPage = True
            app.score = 0
        elif 360 <= mouseX <= 480 and 570 <= mouseY <= 630:
            app.isWinningPage = False
            app.onStartPage = True
            app.score = 0

def onMouseMove(app, mouseX, mouseY):
    if app.onLevelSelectPage:
        if 75 <= mouseX <= 525 and 550 <= mouseY <= 670:
            app.selectingPlane1 = True
        elif 75 <= mouseX <= 525 and 705 <= mouseY <= 855 and app.unlockedPlane == 2:
            app.selectingPlane2 = True
        else:
            app.selectingPlane1 = False
            app.selectingPlane2 = False

    elif app.onGameRunning:
        if mouseX and mouseY:
            app.targetX = mouseX
            app.targetY = mouseY
        

def planeMove(app, targetX, targetY):
    if app.selectedPlane == app.plane1:
        plane = app.plane1
    else:
        plane = app.plane2 

    planeX, planeY = plane.x, plane.y    
    d = distance(planeX, planeY, targetX, targetY)
    
    maxSpeed = 10
    if d > 0 or not d:
        speed = min(maxSpeed, d/8)
    else:
        speed = 0
    
    angle = math.atan2(targetY - planeY, targetX - planeX)
    dx = math.cos(angle)*speed
    dy = math.sin(angle)*speed

    plane.move(dx, dy)
    
def onStep(app):
    if app.onGameRunning:
        app.steps += 1

        damageEnemy(app)
        damageObstacle(app)
        damagePlayer(app)
        planeMove(app, app.targetX, app.targetY)
            
        if app.currentLevel == 1:
            if app.steps % 15 == 0:
                playerShootingBullets(app)

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
            
            if app.enemies != []:
                for enemy in app.enemies:
                    if enemy.image == 'enemy1.png':
                        if app.steps % 50 == 0:
                            enemy1ShootingBullet(app,enemy)
                    elif enemy.image == 'Boss1.png':
                        if app.steps % 30 == 0:
                            boss1ShootingBullet(app)
        
        if app.currentLevel == 2:
            if app.steps % 15 == 0:
                playerShootingBullets(app)

            if app.steps < 1000 and app.steps % 200 == 0 and len(app.enemies) < 5:
                generateEnemy2(app)
            elif app.steps< 1000 and app.steps % 350 == 0 and len(app.enemies) < 5:
                generateEnemy1(app)
            elif app.steps == 1000:
                generateBoss2(app)

            if app.enemies != []:
                for enemy in app.enemies:
                    if enemy.image == 'enemy1.png':
                        if app.steps % 50 == 0:
                            enemy1ShootingBullet(app,enemy)
                    elif enemy.image == 'enemy2.png':
                        if app.steps % 50 == 0:
                            enemy2ShootingBullet(app,enemy)
                    elif enemy.image == 'Boss2.png':
                        if (app.steps//200)%2 == 1:
                            if app.steps % 50 == 0:
                                boss2ShootingBullet1(app, enemy)
                        else:
                            if app.steps % 10 == 0:
                                boss2ShootingBullet2(app, enemy)

    elif not app.onGameRunning:
        resetGame(app)

def resetGame(app):
    app.steps = 0
    app.plane1.lifePoint = 100
    app.plane2.lifePoint = 150

def playerShootingBullets(app):
    if app.selectedPlane == app.plane1:
        plane = app.plane1
    else:
        plane = app.plane2

    if app.bulletType == 0:
        attack = 20
        dx = 0
        dy = -3
        url = 'bullet1.png'
        newBullet1 = Bullet(attack, plane.x, plane.y-50, dx, dy, url)
        app.bullets.append(newBullet1)
    elif app.bulletType == 1:
        attack = 25
        dx = 0
        dy = -3
        url = 'bullet1.png'
        newBullet1 = Bullet(attack, plane.x - 20, plane.y-50, dx, dy, url)
        newBullet2 = Bullet(attack, plane.x + 20, plane.y-50, dx, dy, url)
        app.bullets.append(newBullet1)
        app.bullets.append(newBullet2)

def orientToPlayer(app, enemyX, enemyY, playerX, playerY):
    p = abs((playerX - enemyX)/(enemyY - playerY))
    if playerY > enemyY:
        dy = 3
    else:
        dy = -3

    if playerX > enemyX:
        dx = abs(dy*p)
    else:
        dx = -abs(dy*p)
        if dx >= 3:
            dx = 3

    return dx, dy
    
def enemy1ShootingBullet(app, enemy):
    if app.selectedPlane == app.plane1:
        plane = app.plane1
    else:
        plane = app.plane2

    attack = 10
    dx = 0
    dy = 3
    url = 'enemy1Bullet.png'
    
    if enemy.image == 'enemy1.png': 
        enemyX = enemy.x
        enemyY = enemy.y
        playerX = plane.x
        playerY = plane.y
        dx, dy = orientToPlayer(app, enemyX, enemyY, playerX, playerY)
        newEnemy1Bullet = Bullet(attack, enemy.x, enemy.y, dx, dy, url)
        app.enemyBullet.append(newEnemy1Bullet)

def boss1ShootingBullet(app):
    attack = 20
    dx1 = 0.6
    dx2 = -0.6
    dx3 = 0
    
    dy = 2.5
    url = 'boss1Bullet.png'

    for enemy in app.enemies:
        if enemy.image == 'Boss1.png':
            boss1BulletA = Bullet(attack, enemy.x-10, enemy.y, dx1, dy, url)
            boss1BulletB = Bullet(attack, enemy.x+10, enemy.y, dx2, dy, url)
            boss1BulletC = Bullet(attack, enemy.x, enemy.y, dx3, dy, url)
    app.enemyBullet.append(boss1BulletA)
    app.enemyBullet.append(boss1BulletB)
    app.enemyBullet.append(boss1BulletC)

def enemy2ShootingBullet(app, enemy):
    if app.selectedPlane == app.plane1:
        plane = app.plane1
    else:
        plane = app.plane2

    attack = 15
    url = 'enemy2Bullet.png'
    dx, dy = orientToPlayer(app, enemy.x, enemy.y, plane.x, plane.y)

    if enemy.image == 'enemy2.png': 
        enemyX = enemy.x
        enemyY = enemy.y
        playerX = plane.x
        playerY = plane.y
        dx, dy = orientToPlayer(app, enemyX, enemyY, playerX, playerY)
        newEnemy1Bullet = Bullet(attack, enemy.x, enemy.y, dx, dy, url)
        app.enemyBullet.append(newEnemy1Bullet)

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
                    if enemy.image == 'enemy2.png':
                        app.score += 1500
                    elif enemy.image == 'Boss1.png':
                        app.unlockedLevel = 2
                        app.onGameRunning = False
                        app.isWinningPage = True
                app.bullets.remove(bullet)
                
def boss2ShootingBullet1(app, enemy):
    attack = 20
    dx1 = 0.8
    dx2 = 0.4
    dx3 = 0
    dx4 = -0.4
    dx5 = -0.8
    
    dy = 2.5
    url = 'boss1Bullet.png'

    
    if enemy.image == 'Boss2.png':
        boss2BulletA = Bullet(attack, enemy.x+16, enemy.y, dx1, dy, url)
        boss2BulletB = Bullet(attack, enemy.x+8, enemy.y, dx2, dy, url)
        boss2BulletC = Bullet(attack, enemy.x, enemy.y, dx3, dy, url)
        boss2BulletD = Bullet(attack, enemy.x-8, enemy.y, dx4, dy, url)
        boss2BulletE = Bullet(attack, enemy.x-16, enemy.y, dx5, dy, url)
    app.enemyBullet.append(boss2BulletA)
    app.enemyBullet.append(boss2BulletB)
    app.enemyBullet.append(boss2BulletC)
    app.enemyBullet.append(boss2BulletD)
    app.enemyBullet.append(boss2BulletE)

def boss2ShootingBullet2(app, enemy):
    if app.selectedPlane == app.plane1:
        plane = app.plane1
    else:
        plane = app.plane2

    attack = 10
    dx = 0
    dy = 3
    url = 'boss1Bullet.png'
    
    if enemy.image == 'Boss2.png': 
        enemyX = enemy.x
        enemyY = enemy.y
        playerX = plane.x
        playerY = plane.y
        dx, dy = orientToPlayer(app, enemyX, enemyY, playerX, playerY)
        newEnemy1BulletA = Bullet(attack, enemy.x-20, enemy.y, dx, dy, url)
        newEnemy1BulletB = Bullet(attack, enemy.x+20, enemy.y, dx, dy, url)
        app.enemyBullet.append(newEnemy1BulletA)
        app.enemyBullet.append(newEnemy1BulletB)

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
    if app.selectedPlane == app.plane1:
        planeX = app.plane1.x
        planeY = app.plane1.y
    else:
        planeX = app.plane2.x
        planeY = app.plane2.y

    for enemyBullet in app.enemyBullet:
        d = distance(enemyBullet.x, enemyBullet.y, planeX, planeY)
        if d and d <= 40:
            app.plane1.takeDamage(enemyBullet.attack)
            app.enemyBullet.remove(enemyBullet)

    for obstacle in app.obstacles:
        d = distance(obstacle.x, obstacle.y, planeX, planeY)
        if d and d <= 40:
            app.plane1.takeDamage(obstacle.attack)
            app.obstacles.remove(obstacle)
    
    for enemy in app.enemies:
        d = distance(enemy.x, enemy.y, planeX, planeY)
        if d and d <= 40:
            app.plane1.takeDamage(enemy.attack)
            app.enemies.remove(enemy)

    if app.plane1.lifePoint <= 0:
        app.onGameRunning = False
        app.isGameOverPage = True

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
    lifePoint = 500
    attack = 15
    url = 'Boss1.png'

    x = app.width//2
    y = 100
    dx = 0.4
    dy = 0
    boss1 = Enemy(lifePoint, attack, url, x, y ,dx, dy)

    app.enemies.append(boss1)

def generateEnemy2(app):
    lifePoint = 100
    attack = 10
    url = 'enemy2.png'

    x = random.randint(50, app.width-50)
    y = random.randint(0, app.height // 5)
    dx = random.uniform(-1,1) 
    dy = 1.5
    newEnemy1 = Enemy(lifePoint, attack, url, x, y, dx, dy)

    app.enemies.append(newEnemy1)

def generateBoss2(app):
    lifePoint = 1200
    attack = 30
    url = 'Boss2.png'

    x = app.width//2
    y = 140
    dx = 0.4
    dy = 0
    boss2 = Enemy(lifePoint, attack, url, x, y ,dx, dy)

    app.enemies.append(boss2)


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