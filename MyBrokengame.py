import pygame 
import random
from pygame import *
pygame.init()

WIDTH, HEIGHT= 961,961
#32*32 pix is a block so the full game is 32 blocks of 32*32 for a row/ colomn


screen =pygame.display.set_mode((WIDTH,HEIGHT))

pygame.display.set_caption("This is a platformer, get the coins avoid the enemies")


# SOme color codes:


WHITE=(255, 255, 255)
GREEN=(0,255,0)

# images converted to surfaces

player_image =pygame.image.load("player.png")
player_image =pygame.transform.scale(player_image, (32,64))



coin_image=pygame.image.load("coin.png ")
coin_image=pygame.transform.scale(coin_image, (32,32))
coin_image_rect=coin_image.get_rect()


set_coin_drop_positions= [
    (500,500),
    (450,300),
    (200,200),
    (100,100),
    (150,100),
]

backround=pygame.image.load("background.png")
backround=pygame.transform.scale(backround,(961,961))

Walk_right_1=pygame.image.load("Walking Right 1.png")
Walk_right_2=pygame.image.load("Walking Right 2.png")
Walk_Left_1=pygame.image.load("Walking_Left 1.png")
Walk_Left_2=pygame.image.load("Walking_Left 2.png")

def animation_right():
    screen.blit(Walk_right_1, (player_x, player_y))

def animation_left():
    screen.blit(Walk_Left_1, (player_x, player_y))



player_width, player_height=32, 64

player_x=500

player_y=500

score=0

gravity=0.5

player_speed=15
jump_power=-10

player_alive=True

is_on_ground=False

level_1=pygame.Rect(500,200,50,300)
level_2=pygame.Rect(700,200,100,300)
level_3=pygame.Rect(300,200,100,500)
level_4=pygame.Rect(200,200,45, 200)


#########################################


coins =[]   #the set of all coins posted 

def spawn_coin():
    spawn_point=random.choice(set_coin_drop_positions)
    coin_x=spawn_point[0]
    coin_y=spawn_point[1]
    coin_rect=pygame.Rect(coin_x, coin_y, 32, 32)
    coins.append(coin_rect)          #chooses the positons for the coins           
    
    

player_score=0

font=pygame.font.Font(None, 36)   #renders the score 
end_scene=pygame.image.load("Game over.png")

def end_animation():
    font = pygame.font.Font(None, 50)
    text = font.render(f"Game Over! Your score: {score}", True, (255, 0, 0))
    screen.blit(text, (100, 100))



for i in range(1, 4):
        spawn_coin()    #places down the coins 






running=True # game loop
clock = pygame.time.Clock() # sets the frame rate
while running: 
    # Quits the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen
    # key controlls for the player 
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
        animation_left()

    if keys[pygame.K_RIGHT]:
        player_x += player_speed
        animation_right()

    if keys[pygame.K_UP] and is_on_ground:  # Jump only if on the ground
        player_y+= jump_power
        is_on_ground = False             #when jumping you cant jump again because not on ground
    

    if player_y+64> HEIGHT:
        player_alive=False #when the player falls off the map
        end_animation()

    

    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)  # Get player's rectangle

    for i in coins:
        if player_rect.colliderect(i):  # Use player_rect instead of player_image
            coins.remove(i)
            score += 1
            spawn_coin()

    for coin in coins:
        screen.blit(coin_image, (coin.x,coin.y))



    screen.blit(player_image, (player_x,player_y))

    font=pygame.font.Font(None, 36)   #renders the score 
    score_text= font.render(f"Score: {score}", True , "black")


    
    pygame.display.flip() # updates the display
    clock.tick(60) # limits the fps to 60



pygame.quit()
