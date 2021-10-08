import math
import random

import pygame

# Init pygame
pygame.init()
# Customize screen
screensize = (800, 600)
screen = pygame.display.set_mode(screensize)
pygame.display.set_caption('Space Invader')
icon = pygame.image.load(f'images/alien-ship.png')
pygame.display.set_icon(icon)
back = pygame.image.load(f'images/background.png')
# Make player
player_x = 370
player_y = 520
player_img = pygame.image.load(f'images/battleship.png')
# Make enemy
common_mov_fac = 3
enemies = []
numberEnemies = 6
for i in range(numberEnemies):
    enemy_x = random.randint(30, 710)
    enemy_y = random.randint(50, 100)
    enemy_dict = {
        'img': pygame.image.load(f'images/enemyship.png'),
        'x': enemy_x,
        'y': enemy_y,
        'move_fac': common_mov_fac
    }
    enemies.append(enemy_dict)
# Make missile
missile_speed = 3
missile_x = 0
missile_y = 530
missile_state = 'R'
missile = pygame.image.load(f'images/missile.png')
# Scoreboard
score_value = 0
font = pygame.font.Font('images/cour.ttf', 32)

score_x = 10
score_y = 10
# Game Over
over_text = pygame.font.Font('images/cour.ttf', 64)
over_x = 250
over_y = 200


def game_over():
    over = over_text.render(f'GAME OVER', True, (255, 255, 255))
    screen.blit(over, (over_x, over_y))


def scoreboard():
    score = font.render(f'Score: {score_value}', True, (255, 255, 255))
    screen.blit(score, (score_x, score_y))


def player(x, y):
    screen.blit(player_img, (x, y))


def create_enemy(x, y, img):
    screen.blit(img, (x, y))


def fire(x, y):
    screen.blit(missile, (x, y))


def isCollision(x2, x1, y2, y1):
    d = math.sqrt((math.pow(x2 - x1, 2)) + (math.pow(y2 - y1, 2)))
    if d <= 30:
        return True
    return False


def reset_and_score(enemy):
    global missile_y, missile_state
    missile_state = 'R'
    missile_y = 530
    enemy['x'] = random.randint(30, 710)
    enemy['y'] = random.randint(50, 100)


# Game loop
running = True
while running:
    # screen.fill((0, 0, 0))
    screen.blit(back, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if 30 <= player_x:
                if event.key == pygame.K_LEFT:
                    player_x -= 20
            if player_x <= 710:
                if event.key == pygame.K_RIGHT:
                    player_x += 20
            if event.key == pygame.K_SPACE:
                if missile_state == 'R':
                    missile_sound = pygame.mixer.Sound(f'sounds/missile.mp3')
                    missile_sound.play()
                    missile_state = 'F'
                    missile_x = player_x + 16
    # Player
    player(player_x, player_y)
    # Enemy
    for enemy in enemies:
        if enemy['y'] > 482 and enemy['x'] == player_x:
            for e in enemies:
                e['y'] = 2000
            game_over()
            # running = False
            break
        else:
            enemy['x'] += enemy['move_fac']
            if 30 <= enemy['x'] <= 710:
                enemy['move_fac'] *= 1
            else:
                enemy['move_fac'] *= -1
                enemy['y'] += 40
            # Collision detection
            collision = isCollision(enemy['x'], missile_x, enemy['y'], missile_y)
            if collision:
                explosion = pygame.mixer.Sound(f'sounds/explosion.wav')
                explosion.play()
                score_value += 1
                reset_and_score(enemy)
            create_enemy(enemy['x'], enemy['y'], enemy['img'])
    # Bullet
    if missile_state == 'F':
        if missile_y >= 0:
            fire(missile_x, missile_y)
            missile_y -= missile_speed
        else:
            missile_y = 530
            missile_state = 'R'
    scoreboard()
    pygame.display.update()
# pygame.quit()
