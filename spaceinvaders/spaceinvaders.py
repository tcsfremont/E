import pgzrun
from random import random
game_over= False
game_start = False
player=Actor('ranger')
player.x=400
player.y = 600 - player.height * 0.5
speed = 5
cooldown = 0.5
cooled = True
def cool():
    global cooled
    cooled = True
aliens=[]
def add_alien():
    alien=Actor('slimey')
    alien.x = alien.width + (800 - alien.width) * random()
    alien.y = alien.height * 0.5
    aliens.append(alien)
def on_key_down(key):
    global game_start
    if not game_start:
        game_start = True
        clock.schedule_interval(add_alien,5)# every 5 seconds
lasers = []
def fire_laser():
    global cooled
    if cooled:
        laser = Rect((player.x, player.y), (10,50))
        lasers.append(laser)
        cooled = False
        clock.schedule_unique(cool, cooldown)
def update():
    global game_over
    if not game_over:

        if keyboard.left:
            player.x = max(player.width * 0.5,  player.x - 5)
        if keyboard.right and player.x < 800-player.width * 0.5:
            player.x=min(800 - player.width * 0.5, player.x + 5)
        if keyboard.space:
            fire_laser()
        
    for alien in aliens:
        alien.y += 3
        if alien.y >600:
            game_over= True
    for laser in lasers:
        laser.y -=10
        for alien in aliens:
            if laser.x>alien.x -alien.width *0.5:
                if laser.y > alien.y-alien.height *0.5:
                    if laser.x < alien.x + alien.width*0.5:
                        if laser.y < alien.y + alien.height *0.5:
                            aliens.remove(alien)

def draw():
    global game_over
    screen.clear()
    player.draw()
    for laser in lasers:
        screen.draw.filled_rect(laser, (227,115,131 ))
    for alien in aliens:
        alien.draw()
    if game_over:
        screen.draw.text("Game Over", (400, 300))
pgzrun.go()
