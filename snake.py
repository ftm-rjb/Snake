import pygame
import random

pygame.init()
screen = pygame.display.set_mode((500 , 500))

screen1 = pygame.Surface((500 , 500))
screen1 = pygame.transform.scale(screen1 , (500 , 500))
rect_screen1 = screen1.get_rect()
rect_screen1.x = 0
rect_screen1.y = 0

screen2 = pygame.Surface((500 , 500))
screen2 = pygame.transform.scale(screen2 , (500 , 500))
rect_screen2 = screen2.get_rect()
rect_screen2.x = 0
rect_screen2.y = 0

screen3 = pygame.Surface((500 , 500))
screen3 = pygame.transform.scale(screen3 , (500 , 500))
rect_screen3 = screen3.get_rect()
rect_screen3.x = 0
rect_screen3.y = 0

screen4 = pygame.Surface((500 , 500))
screen4 = pygame.transform.scale(screen4 , (500 , 500))
rect_screen4 = screen4.get_rect()
rect_screen4.x = 0
rect_screen4.y = 0

clock = pygame.time.Clock()

font1 = pygame.font.Font(None , 60)
font2 = pygame.font.Font(None , 25)
font3 = pygame.font.SysFont(None , 25)

backcolor = (255 , 255 , 255)
snakecolor1 = (139 , 0 , 0)
snakecolor2 = (0 , 0 , 139)
snake2color = (0 , 0 , 0)
apple = (0 , 100 , 0)
green = (154 , 205 , 50)
gamecol = (25 , 25 , 112)
red = (106 , 90 , 205)

def circle(r , snake , col):
    for i in range(len(snake)):
        pygame.draw.circle(screen , col , (snake[i][0] , snake[i][1]) , r , 0)

def massage(passage , color , cordinate_x , cordinate_y , font):
    text = font.render(passage , True , color)
    text_rect = text.get_rect()
    text_rect.center = cordinate_x,cordinate_y
    screen.blit(text , text_rect)

def score(score , f , k):
    text = font3.render("Score:"+str(score),True,gamecol)
    screen.blit(text,[f,k])

def game_screen_1():
    screen.fill(backcolor)
    screen.blit(screen1 ,rect_screen1)
    massage("SNAKE" , gamecol , 240 , 100 , font1)
    massage("Enter P to play" , gamecol , 130 , 350 , font2)
    massage("Enter Q to quit" , gamecol , 130 , 400 , font2)
    massage("Score 3 => Next level" , gamecol , 130 , 470 , font3)
    
    game_s = True
    while game_s:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        key = pygame.key.get_pressed()
        if key[pygame.K_p]:
            step_1()
        if key[pygame.K_q]:
            pygame.quit()
            quit()
        pygame.display.update()

def game_screen_2():
    screen.fill(backcolor)
    screen.blit(screen2 , rect_screen2)
    massage("VERY GOOD" , gamecol , 240 , 100 , font1)
    massage("Enter P to Next level" , gamecol , 240 , 350 , font2)
    massage("Enter Q to quit" , gamecol , 240 , 400 , font2)
    massage("Every one have high speed to eat apple, Win" , gamecol , 250 , 470 , font3)
    
    game_s = True
    while game_s:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        key = pygame.key.get_pressed()
        if key[pygame.K_p]:
            step_2()
        if key[pygame.K_q]:
            pygame.quit()
            quit()
        pygame.display.update()

def game_screen_3():
    screen.fill(backcolor)
    screen.blit(screen3 , rect_screen3)
    massage("GAME OVER" , gamecol , 240 , 300 , font1)
    massage("Enter P to play Again" , gamecol , 240 , 360 , font2)
    massage("Enter Q to quit" , gamecol , 240 , 400 , font2)

    game_s = True
    while game_s:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        key = pygame.key.get_pressed()
        if key[pygame.K_p]:
            step_1()
        if key[pygame.K_q]:
            pygame.quit()
            quit()
        pygame.display.update()

def game_screen_5():
    screen.fill(backcolor)
    screen.blit(screen4 , rect_screen4)
    massage("Red WINED" , snakecolor1 , 350 , 70 , font1)
    massage("Enter P to play again" , gamecol , 350 , 350 , font2)
    massage("Enter Q to quit" , gamecol , 350 , 400 , font2)
    
    game_s = True
    while game_s:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        key = pygame.key.get_pressed()
        if key[pygame.K_p]:
            step_2()
        if key[pygame.K_q]:
            pygame.quit()
            quit()
        pygame.display.update()

def game_screen_6():
    screen.fill(backcolor)
    screen.blit(screen4 , rect_screen4)
    massage("Blue WINED" , snakecolor2 , 350 , 100 , font1)
    massage("Enter P to play again" , gamecol , 350 , 350 , font2)
    massage("Enter Q to quit" , gamecol , 350 , 400 , font2)
    
    game_s = True
    while game_s:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        key = pygame.key.get_pressed()
        if key[pygame.K_p]:
            step_2()
        if key[pygame.K_q]:
            pygame.quit()
            quit()
        pygame.display.update()

def game_screen_7():
    screen.fill(backcolor)
    screen.blit(screen2 , rect_screen2)
    massage("NO WINNER" , gamecol , 240 , 350 , font1)
    massage("Enter P to play again" , gamecol , 240 , 400 , font2)
    massage("Enter Q to quit" , gamecol , 240 , 440 , font2)
    
    game_s = True
    while game_s:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        key = pygame.key.get_pressed()
        if key[pygame.K_p]:
            step_2()
        if key[pygame.K_q]:
            pygame.quit()
            quit()
        pygame.display.update()

def step_1():
    
    r = 10
    x = 300
    y = 300
    move_x = 0
    move_y = 0
    a = int(round(random.randrange(0 , 46)*10)+20)
    b = int(round(random.randrange(0 , 46)*10)+20)
    direc = 'U'
    snake = []
    length = 3
    sc = 0
    
    running = True
    while running:
        
        screen.fill(green)
        clock.tick(8)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
        key = pygame.key.get_pressed()
            
        if key[pygame.K_RIGHT]:   
            if (direc == 'U' or direc == 'D'):
                direc = 'R'
                move_x = r
                move_y = 0
                    
        if key[pygame.K_LEFT]:
            if (direc == 'U' or direc == 'D'):
                direc = 'L'
                move_x = -r
                move_y = 0
                
        if key[pygame.K_DOWN]:   
            if (direc == 'L' or direc == 'R'):
                direc = 'D'
                move_x = 0
                move_y = r
                    
        if key[pygame.K_UP]:       
            if (direc == 'L' or direc == 'R' or direc == 'U'):
                direc = 'U'
                move_x = 0
                move_y = -r
                
        x += move_x
        y += move_y
        
        head = []
        head.append(x)
        head.append(y)
        snake.append(head)
        circle(r , snake , snakecolor1)
        score(sc , 0 , 0)
        
        for i in snake[:-4]:
            if i == head:
                game_screen_3()
        
        if len(snake)>length:
            del snake[0]
        
        pygame.draw.circle(screen , apple , (a , b) , 8 , 0)
        
        if x < a+8 and x > a-8 and y < b+8 and y > b-8:      
            length += 1
            sc += 1
            a = int(round(random.randrange(0 , 46)*10)+20)
            b = int(round(random.randrange(0 , 46)*10)+20)
        
        if x <= 2 or x >= 498 or y <= 2 or y >= 498:
            pygame.time.delay(200)
            game_screen_3()
            
        if length == 6:
            pygame.time.delay(200)
            game_screen_2()
        
        pygame.display.update()

def step_2():
    
    r = 10
    x = 300
    y = 350
    x1 = 300
    y1 = 380
    x2 = 200
    y2 = 200
    move_x = 0
    move_y = 0
    move_x1 = 0
    move_y1 = 0
    move_x2 = 10
    move_y2 = 0
    a = int(round(random.randrange(0 , 46)*10)+20)
    b = int(round(random.randrange(0 , 46)*10)+20)             
    direc = 'U'
    direc1 = 'U'
    direc2 = 'R'
    snake = []
    snake1 = []
    snake2 = []
    length = 3
    length1 = 3
    sc = 0
    sc1 = 0
    
    shart = True
    running = True
    while shart:
        
        if (a>=190 and a<=230 and b>=90 and b<=130) or (a>=390 and a<=430 and b>=40 and b<=80) or (a>=90 and a<=130 and b>=290 and b<=330) or (a>=40 and a<=40 and b>=390 and b<=430):
            a = int(round(random.randrange(0 , 46)*10)+20)
            b = int(round(random.randrange(0 , 46)*10)+20)
        
        else:
            while running:
                screen.fill(green)
                clock.tick(8)
                
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    
                key = pygame.key.get_pressed()
                
                if key[pygame.K_RIGHT]:   
                    if (direc == 'U' or direc == 'D'):
                        direc = 'R'
                        move_x = r
                        move_y = 0
                            
                if key[pygame.K_LEFT]:
                    if (direc == 'U' or direc == 'D'):
                        direc = 'L'
                        move_x = -r
                        move_y = 0
                        
                if key[pygame.K_DOWN]:   
                    if (direc == 'L' or direc == 'R'):
                        direc = 'D'
                        move_x = 0
                        move_y = r
                            
                if key[pygame.K_UP]:       
                    if (direc == 'L' or direc == 'R' or direc == 'U'):
                        direc = 'U'
                        move_x = 0
                        move_y = -r
                
                x += move_x
                y += move_y
                
                if key[pygame.K_d]:   
                    if (direc1 == 'U' or direc1 == 'D'):
                        direc1 = 'R'
                        move_x1 = r
                        move_y1 = 0
                            
                if key[pygame.K_a]:
                    if (direc1 == 'U' or direc1 == 'D'):
                        direc1 = 'L'
                        move_x1 = -r
                        move_y1 = 0
                        
                if key[pygame.K_s]:   
                    if (direc1 == 'L' or direc1 == 'R'):
                        direc1 = 'D'
                        move_x1 = 0
                        move_y1 = r
                            
                if key[pygame.K_w]:       
                    if (direc1 == 'L' or direc1 == 'R' or direc1 == 'U'):
                        direc1 = 'U'
                        move_x1 = 0
                        move_y1 = -r
                
                x1 += move_x1
                y1 += move_y1
                
                if x2 == 350 and direc2 == 'R':
                    move_x2 = 0
                    move_y2 = -10
                    direc2 = 'U'
                
                if y2 == 30 and direc2 == 'U':
                    move_x2 = -10
                    move_y2 = 0
                    direc2 = 'L'
                
                if x2 == 100 and direc2 == 'L':
                    move_x2 = 0
                    move_y2 = 10
                    direc2 = 'D'
                    
                if y2 == 250 and direc2 == 'D':
                    move_x2 = 10
                    move_y2 = 0
                    direc2 = 'R'
                    
                if x2 == 200 and direc2 == 'R':
                    move_x2 = 0
                    move_y2 = 10
                    direc2 = 'D'
                
                if y2 == 450 and direc2 == 'D':
                    move_x2 = 10
                    move_y2 = 0
                    direc2 = 'R'
                    
                x2 += move_x2
                y2 += move_y2
                
                head = []
                head.append(x)
                head.append(y)
                snake.append(head)
                circle(r , snake , snakecolor1)
                
                head1 = []
                head1.append(x1)
                head1.append(y1)
                snake1.append(head1)
                circle(r , snake1 , snakecolor2)
                
                head2 = []
                head2.append(x2)
                head2.append(y2)
                snake2.append(head2)
                circle(r , snake2 , snake2color)
                
                score(sc , 0 , 0)
                score(sc1 , 0 , 480)
                
                for i in snake:
                    for j in snake2:
                        if i[0] == j[0] and i[1] == j[1]:
                            pygame.time.delay(200)
                            if sc > sc1:
                                game_screen_5()
                            elif sc < sc1:
                                game_screen_6()
                            elif sc == sc1:
                                game_screen_7()
                
                for u in snake1:
                    for j in snake2:
                        if u[0] == j[0] and u[1] == j[1]:
                            pygame.time.delay(200)
                            if sc > sc1:
                                game_screen_5()
                            elif sc < sc1:
                                game_screen_6()
                            elif sc == sc1:
                                game_screen_7()
                            
                for i in snake:
                    for u in snake1:
                        if i[0] == u[0] and i[1] == u[1]:
                            pygame.time.delay(200)
                            if sc > sc1:
                                game_screen_5()
                            elif sc < sc1:
                                game_screen_6()
                            elif sc == sc1:
                                game_screen_7()
                
                for i in snake[:-4]:
                    if i == head:
                        pygame.time.delay(200)
                        if sc > sc1:
                            game_screen_5()
                        elif sc < sc1:
                            game_screen_6()
                        elif sc == sc1:
                            game_screen_7()
                        
                for u in snake1[:-4]:
                    if u == head1:
                        pygame.time.delay(200)
                        if sc > sc1:
                            game_screen_5()
                        elif sc < sc1:
                            game_screen_6()
                        elif sc == sc1:
                            game_screen_7()
                                
                if len(snake)>length:
                    del snake[0]
                
                if len(snake1)>length:
                    del snake1[0]
                
                if len(snake2)>length:
                    del snake2[0]
                
                pygame.draw.circle(screen , apple , (a , b) , 8 , 0)
               
                pygame.draw.rect(screen , red , [200 , 100 , 20 , 20])
                pygame.draw.rect(screen , red , [400 , 50 , 20 , 20])
                pygame.draw.rect(screen , red , [100 , 300 , 20 , 20])
                pygame.draw.rect(screen , red , [50 , 400 , 20 , 20])    
                
                if x < a+8 and x > a-8 and y < b+8 and y > b-8:        
                    length += 1
                    sc += 1
                    a = int(round(random.randrange(0 , 46)*10)+20)
                    b = int(round(random.randrange(0 , 46)*10)+20)
                    
                if x1 < a+8 and x1 > a-8 and y1 < b+8 and y1 > b-8:        
                    length1 += 1
                    sc1 += 1
                    a = int(round(random.randrange(0 , 46)*10)+20)
                    b = int(round(random.randrange(0 , 46)*10)+20)
                
                if length == 8:
                    game_screen_5()
                
                if length1 == 8:
                    game_screen_6()
                
                if length == 8 and length1 == 8:
                    game_screen_7()
                
                if x <= 2 or x >= 498 or y <= 2 or y >= 498:
                    pygame.time.delay(200)
                    if sc > sc1:
                        game_screen_5()
                    elif sc < sc1:
                        game_screen_6()
                    elif sc == sc1:
                        game_screen_7()
                    
                if x1 <= 2 or x1 >= 498 or y1 <= 2 or y1 >= 498:
                    pygame.time.delay(200)
                    if sc > sc1:
                        game_screen_5()
                    elif sc < sc1:
                        game_screen_6()
                    elif sc == sc1:
                        game_screen_7()
                
                if (x <= 2 or x >= 498 or y <= 2 or y >= 498) and (x1 <= 2 or x1 >= 498 or y1 <= 2 or y1 >= 498):
                    pygame.time.delay(200)
                    if sc > sc1:
                        game_screen_5()
                    elif sc < sc1:
                        game_screen_6()
                    elif sc == sc1:
                        game_screen_7()
                    
                if (x==200 and y>90 and y<130) or (x==220 and y>90 and y<130) or (y==100 and x>190 and x<230) or (y==120 and x>190 and x<230):
                    pygame.time.delay(200)
                    if sc > sc1:
                        game_screen_5()
                    elif sc < sc1:
                        game_screen_6()
                    elif sc == sc1:
                        game_screen_7()
                
                if (x==400 and y>40 and y<80) or (x==420 and y>40 and y<80) or (y==50 and x>390 and x<430) or (y==70 and x>390 and x<430):
                    pygame.time.delay(200)
                    if sc > sc1:
                        game_screen_5()
                    elif sc < sc1:
                        game_screen_6()
                    elif sc == sc1:
                        game_screen_7()            
                    
                if (x==100 and y>290 and y<330) or (x==120 and y>290 and y<330) or (y==300 and x>90 and x<130) or (y==320 and x>90 and x<130):
                    pygame.time.delay(200)
                    if sc > sc1:
                        game_screen_5()
                    elif sc < sc1:
                        game_screen_6()
                    elif sc == sc1:
                        game_screen_7()
                
                if (x==50 and y>390 and y<430) or (x==70 and y>390 and y<430) or (y==400 and x>40 and x<80) or (y==420 and x>40 and x<80):
                    pygame.time.delay(200)
                    if sc > sc1:
                        game_screen_5()
                    elif sc < sc1:
                        game_screen_6()
                    elif sc == sc1:
                        game_screen_7()
                
                if (x1==200 and y1>90 and y1<130) or (x1==220 and y1>90 and y1<130) or (y1==100 and x1>190 and x1<230) or (y1==120 and x1>190 and x1<230):
                    pygame.time.delay(200)
                    if sc > sc1:
                        game_screen_5()
                    elif sc < sc1:
                        game_screen_6()
                    elif sc == sc1:
                        game_screen_7()
                
                if (x1==400 and y1>40 and y1<80) or (x1==420 and y1>40 and y1<80) or (y1==50 and x1>390 and x1<430) or (y1==70 and x1>390 and x1<430):
                    pygame.time.delay(200)
                    if sc > sc1:
                        game_screen_5()
                    elif sc < sc1:
                        game_screen_6()
                    elif sc == sc1:
                        game_screen_7()            
                    
                if (x1==100 and y1>290 and y1<330) or (x1==120 and y1>290 and y1<330) or (y1==300 and x1>90 and x1<130) or (y1==320 and x1>90 and x1<130):
                    pygame.time.delay(200)
                    if sc > sc1:
                        game_screen_5()
                    elif sc < sc1:
                        game_screen_6()
                    elif sc == sc1:
                        game_screen_7()
                
                if (x1==50 and y1>390 and y1<430) or (x1==70 and y1>390 and y1<430) or (y1==400 and x1>40 and x1<80) or (y1==420 and x1>40 and x1<80):
                    pygame.time.delay(200)
                    if sc > sc1:
                        game_screen_5()
                    elif sc < sc1:
                        game_screen_6()
                    elif sc == sc1:
                        game_screen_7()
                                
                pygame.display.update()
            
game_screen_1()