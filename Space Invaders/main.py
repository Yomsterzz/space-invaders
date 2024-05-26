import pgzrun
import random

WIDTH = 1200
HEIGHT = 600

white = (255,255,255)
blue = (0,0,255)

bullets = []
enemies = []
score = 0
speed = 5

player = Actor("galaga")
player.pos = (WIDTH//2,HEIGHT-60)

bug_enemy = Actor("bug")
enemies.append(bug_enemy)
enemies[-1].x = 10
enemies[-1].y = -100

def display_score():
    screen.draw.text(str(score), (50,50), color=white)

def on_key_down(key):
    if key == keys.SPACE:
        bullets.append(Actor("bullet"))
        bullets[-1].x = player.x
        bullets[-1].y = player.y - 20
    
def update():
    global score
    if keyboard.left:
        player.x -= speed
        if player.x <= 0:
            player.x = 0
    elif keyboard.right:
        player.x += speed
        if player.x >= WIDTH:
            player.x = WIDTH
    
    #firing bullet - making it move
    if keyboard.space:
        bullets.append(Actor("bullet"))
        bullets[-1].x = player.x
        bullets[-1].y = player.y - 20
    for bullet in bullets:
        if bullet.y <= 0:
            bullets.remove(bullet)
        else: 
            bullet.y -= 7

    for enemy in enemies:
        enemy.y += speed
        if enemy.y >= HEIGHT:
            enemy.y = -100
            enemy.x = random.randint(WIDTH-200,WIDTH+200)
        
        


def draw():
    screen.clear()
    screen.blit("bg")
    player.draw()

    for enemy in enemies:
        enemy.draw()
    
    for bullet in bullets:
        bullet.draw()
    
    display_score()

pgzrun.go()