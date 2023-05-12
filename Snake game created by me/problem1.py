##Read pygame documenetation from google url
import pygame
import random
import os
pygame.init()

white=(255,255,255)
red=(255,0,0)
colour=(100,0,200)
black=(0,0,0)

pygame.mixer.init()



screen_width=900
screen_height=600
gameWindow=pygame.display.set_mode((screen_width,screen_height))

game_image=pygame.image.load("snake.jpg.jpg")
game_image=pygame.transform.scale(game_image,(screen_width,screen_height)).convert_alpha()

pygame.display.set_caption("SnakeWithHarsh")
pygame.display.update()
clock=pygame.time.Clock()
font=pygame.font.SysFont(None,45)


def text_screen(text,color,x,y):
    screen_text=font.render(text,True,color)
    gameWindow.blit(screen_text,[x,y])


def plot_snake(gameWindow,color,snake_list,snake_size):
    for x,y in snake_list:
        pygame.draw.rect(gameWindow,color,[x,y,snake_size,snake_size])


def Welcome():
    exit_game=False
    while not exit_game:
        gameWindow.fill(colour)
        text_screen("Welcome to snake with Harsh",black,250,250)
        text_screen("Press space to play Game",black,200,300)

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit_game=True

            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    pygame.mixer.music.load('snake.mp3.mp3')
                    pygame.mixer.music.play()
                    game_loop()

        pygame.display.update()
        clock.tick(60)


def game_loop():
    exit_game = False
    game_over = False
    snake_x = 60
    snake_y = 200
    snake_size = 10
    fps = 60
    velocity_x = 0
    velocity_y = 0
    intial_velocity = 3
    score = 0
    snake_list = []
    snake_length = 1
    food_x = random.randint(20, screen_width / 1.5)
    food_y = random.randint(20, screen_height / 1.5)

    if(not os.path.exists("highscore.txt")):
        with open("highscore.txt","w") as file:
            file.write("0")

    with open("highscore.txt","r") as file:
        highscore=file.read()

    while not exit_game:

        if game_over:
            with open("highscore.txt", "w") as file:
                file.write(str(highscore))
            gameWindow.fill(white)
            text_screen("Game over! Press Enter To continue",red,100,300)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        Welcome()

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = intial_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = -intial_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = -intial_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = intial_velocity
                        velocity_x = 0

                    ##cheats
                    if event.key==pygame.K_q:
                        score+=5

                    if event.key==pygame.K_w:
                        intial_velocity+=2

                    if event.key == pygame.K_r:
                        intial_velocity -= 2



            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x) < 6 and abs(snake_y - food_y) < 6:
                score += 10
                food_x = random.randint(20, screen_width / 1.5)
                food_y = random.randint(20, screen_height / 1.5)
                snake_length += 5
                if score>int(highscore):
                    highscore=score


            gameWindow.fill(white)
            gameWindow.blit(game_image,(0,0))

            text_screen("score" + str(score) +"  Highscore"+str(highscore), red, 5, 5)
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)

        if len(snake_list) > snake_length:
            del snake_list[0]

        if head in snake_list[:-1]:
            game_over=True
            pygame.mixer.music.load('gameover.mp3.mp3')
            pygame.mixer.music.play()

        if snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_height:
            game_over = True
            pygame.mixer.music.load('gameover.mp3.mp3')
            pygame.mixer.music.play()

        plot_snake(gameWindow, black, snake_list, snake_size)

        pygame.display.update()
        clock.tick(fps)

            # pygame.draw.rect(gameWindow,black,[snake_x,snake_y,snake_size,snake_size])

    pygame.quit()
    quit()
Welcome()