import  pygame
import random
import os
pygame.mixer.init()

pygame.init()

#background image
# bgimg= pygame.image.load('background image.jps')
# bgimg=pygame.transform

screen_width=1200
screen_height=600

white=(255,255,255)
yellow=(66,13,244)
# yellow=(255,255,55)
blue=(0,0,255)
red=(255,0,0)
black=(0,0,0)
bbb=(0,255,0)
red=(219, 68, 55)


#create window
game_window= pygame.display.set_mode((screen_width,screen_height))

bgimg= pygame.image.load('snkbg.jpg')
bgimg=pygame.transform.scale(bgimg,(screen_width,screen_height)).convert_alpha()

pygame.display.set_caption('My_Snake_Game')
# game specific variable


#display score
font=pygame.font.SysFont(None,35)



def display_score(text,color,x,y):
    screen_score= font.render(text,True,color)
    game_window.blit(screen_score,[x,y])
    

def plot_snake(game_window, color,snake_list, snake_size ):
    # print(snake_list)
    for x,y in snake_list:
        pygame.draw.rect(game_window, color, [x,y, snake_size, snake_size])

# snake_list=[]
# snake_length=1
clock= pygame.time.Clock()
def Welcome():
    exit_game=False
    while not exit_game:
        game_window.fill(yellow)
        display_score('Welcome to my snake game',bbb,400,200)
        display_score('press space bar to play',bbb,420,250)
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key ==pygame.K_SPACE:
                    pygame.mixer.music.load('nagin Music.mp3')
                    pygame.mixer.music.play(-1)
                    #pygame.mixer.music.rewind()        
                    game_loop()
        pygame.display.update()
        clock.tick(60)

# creating a game loop
def game_loop():

    exit_game = False
    game_over= False
    snake_x=40
    snake_y=30
    snake_size=15
    velocity_x=0
    velocity_y=0
    init_velocity=2

    #check if highscore file exist
    if(not os.path.exists('highscore.txt')):
        with open('highscore.txt','w')as f:
            f.write('0')

    with open('highscore.txt','r')as f:
        highscore= f.read()

    food_x= random.randint(10,screen_width)
    food_y=random.randint(10,screen_height)
    food_size=10
    score=0
    fps=60
    clock= pygame.time.Clock()

    snake_list=[]
    snake_length=1

    

    while not exit_game:
        if game_over:

            with open('highscore.txt','w')as f:
                f.write(str(highscore))

            game_window.fill(yellow)
            display_score('game over! press enter to continue',red,screen_width/3,screen_height/3)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game=True

                if event.type== pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        Welcome()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game=True  

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x= init_velocity
                        velocity_y=0
                    if event.key == pygame.K_LEFT:
                        velocity_x=-init_velocity
                        velocity_y=0 
                    if event.key == pygame.K_UP:
                        velocity_y=-init_velocity
                        velocity_x=0 
                    if event.key == pygame.K_DOWN:
                        velocity_y=init_velocity
                        velocity_x=0
#######this is used for cheating if i want highest score then q key press then auto adding score +5 without eat food
                    # if event.key == pygame.K_q:
                    #     score+=5

            snake_x=snake_x+velocity_x
            snake_y=snake_y+velocity_y 
            if abs(snake_x-food_x)<10 and abs(snake_y-food_y)<10:
                score+=5
                #print('Score',score)
                # display_score("score:"+str(score+00),red,5,5)
                food_x= random.randint(20,screen_width/2)
                food_y=random.randint(20,screen_height/2)
                snake_length+=5
                # print(highscore)
                if score>int(highscore):
                    highscore= score

            game_window.fill(white)
            game_window.blit(bgimg,(0,0))
            display_score("score:" + str(score) + '  highscore: '+str(highscore),blue,5,5)   
            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)
            if len(snake_list)>snake_length:
                del snake_list[0]
#@ if snake touch his body
            if head in snake_list[:-1] :
               game_over= True 
               pygame.mixer.music.load('explosion.mp3')
               pygame.mixer.music.play()   

            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over=True
                pygame.mixer.music.load('explosion.mp3')
                pygame.mixer.music.play()
                # print('game over')
            plot_snake(game_window, black, snake_list, snake_size)
            #pygame.draw.rect(game_window, black, [snake_x, snake_y, snake_size, snake_size])
            pygame.draw.rect(game_window, red, [food_x, food_y, food_size, food_size])
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    quit()

Welcome()
# game_loop()