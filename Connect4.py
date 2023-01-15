import pygame as pg
pg.init()

#colours
darkb = (0,0,40)
black=(0,0,0)
lightb = (0,204,255)
lav = (204, 153, 255)
blue=(51,102,255)
white=(255,255,255)
brown=(153,51,0)
red=(255,0,0)
yellow=(255,255,0)
b2=(0,0,150)
#defining font
font = pg.font.SysFont("Times New Roman", 50)
newfont=pg.font.SysFont("Cooper Black", 50)
font4=pg.font.SysFont("Cooper Black", 70)
font2=pg.font.SysFont("Times New Roman", 30)
font3=pg.font.SysFont("Cooper Black", 24)
#Player 1: Red (1 in list, True), Player 2: Yellow (2 in list, False)
def InitList():
    L=[]
    for i in range(6):
        l2=[]
        for j in range(7):
            l2.append(0)
        L.append(l2)
    return L

def drawCircles(ScreenW,ScreenH,L,screen,game_play,pos):
    col=pos[0]
    x=ScreenW/8
    col_index=-1
    for i in range(1,8):
        if col>(i*x-x/2) and col<(i*x+x/2):
            col_index=i-1    #checking which column the mouse is positioned over
            
    if game_play:
        blank_circle=(0,0,66) #darkblue
    else:
        blank_circle=(0,0,0) #black
    Hdivision,Wdivision=ScreenH/7, ScreenW/8
    for i in range(6):
        for j in range(7):
            if L[i][j]==0:
                if j==col_index and game_play:
                    c=b2
                else:
                    c=blank_circle
            elif L[i][j]==1:
                c=(255,0,0) #red
            elif L[i][j]==2:
                c=(255,255,0) #yellow
            pg.draw.circle(screen,c,(Wdivision*(j+1),Hdivision*(i+1)+50),32)

def update_List(column,L,which_player):
    for i in range(5,-1,-1):
        if L[i][column]==0:
            if which_player==True:
                L[i][column]=1
            else:
                L[i][column]=2
            break
    return L

def adding_coin(ScreenW,pos, which_player,L):
    col=pos[0]
    x=ScreenW/8
    for i in range(1,8):
        if col>(i*x-x/2) and col<(i*x+x/2):    #checking which column the mouse is positioned over
            L=update_List(i-1,L,which_player)
    return L        

def check_win(L):
    #checking rows:
    for x in (1,2):
        for i in range(6):           
            for j in range(4):
                templ=[]
                for k in range(4):
                    templ.append(L[i][j+k])
                if templ==[x,x,x,x]:
                    return x
    #checking columnns:
        for i in range(7):
                for j in range(3):
                    templ=[]
                    for k in range(4):
                        templ.append(L[j+k][i])  
                    if templ==[x,x,x,x]:
                        return x

    #checking diagonals (//):
        for i in range(5,2,-1):
            for j in range(4):
                templ=[]
                for k in range (4):
                    templ.append(L[i-k][j+k])
                if templ==[x,x,x,x]:
                    return x
    #checking diagonals (\\):
        for i in range(5,2,-1):
                for j in range(6,2,-1):
                    templ=[]
                    for k in range (4):
                        templ.append(L[i-k][j-k])
                    if templ==[x,x,x,x]:
                        return x

    return (0)   

def welcome():
    exit_game = False
    #instruction=False

    pg.mixer.music.load('beat.mp3')
    pg.mixer.music.play()
    
    #rendering a text written in this font
    text1 = font.render('Play' , True , white)
    text2 = font.render('Instructions' , True , white)
    while not exit_game:
        screen.fill((233,210,229))
        screen.blit(bgimg, (0, 0))
        screen.blit(img, (0, 0))
        pos = pg.mouse.get_pos()
        # if mouse is hovered on a button it
        # changes to lighter shade 
        if 485 <= pos[0] <= 585 and 175 <= pos[1] <= 225:
            pg.draw.rect(screen, blue, [485, 175, 100 , 50])
            pg.draw.rect(screen, darkb, [420, 300, 240 , 50]) 
        
        elif 420 <= pos[0] <= 660 and 300 <= pos[1] <= 350:
            pg.draw.rect(screen, blue, [420, 300, 240 , 50]) 
            pg.draw.rect(screen, darkb, [485, 175, 100 , 50]) 
        else:
             pg.draw.rect(screen, darkb, [485, 175, 100 , 50])
             pg.draw.rect(screen, darkb, [420, 300, 240 , 50])  
        
        screen.blit(text1 , (490 , 170))
        screen.blit(text2 , (420 , 290))

        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit_game = True
                pg.quit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if 485 <= pos[0] <= 585 and 175 <= pos[1] <= 225:
                    pg.mixer.music.load('bell.mp3')
                    pg.mixer.music.play()
                    exit_game = True
                #    pg.mixer.music.load('soft-beat-115017.mp3')
                #    pg.mixer.music.play()
                    main_game()
                elif 420 <= pos[0] <= 660 and 300 <= pos[1] <= 350:
                    exit_game = True
                    instr()
                
        pg.display.update()
    
def end_text(x,bgcolor,recordList):
    if x==1: 
        Text='Player 1 Won'
        c=red
    elif x==2:
        Text='Player 2 Won'
        c=yellow
    elif x==0:
        Text='Draw'
        c=white
    text = newfont.render(Text, True, c)
    textRect = text.get_rect()
    textRect.center=(screenW/2,50)
    screen.blit(text,textRect)

def player_text(which_player):
    if which_player:
        c1=red
        c2=white
    else:
        c1=white
        c2=yellow
    Text1='Player 1'
    Text2='Player 2'
    font = pg.font.SysFont('Cooper Black', 40)
    text1 = font.render(Text1, True, c1)
    text2 = font.render(Text2, True, c2)
    textRect1 = text1.get_rect()
    textRect1.center=(60,540)
    textRect2 = text2.get_rect()
    textRect2.center=(500,540)
    
    screen.blit(text1,textRect1.center)
    screen.blit(text2,textRect2.center)

def moving_circle(which_player):
    if which_player:
        c=red
    else:
        c=yellow
    pos=pg.mouse.get_pos()
   
    Wdivision=screenW/7
    pg.draw.circle(screen,c,(pos[0],50),32)
 
def main_game():
    check2=True
    game_play=True
    bgcolor=[0,0,0]
    recordList=InitList()
    which_player=True 
    global running
    running=True

    #coordinates for back button:
    l,w=100,50
    x3,y=600,80

    while running:
        for event in pg.event.get():
            if event.type==pg.QUIT:
                running=False
                pg.quit()
            #adding coins
            if event.type == pg.MOUSEBUTTONDOWN and game_play:
                pos = pg.mouse.get_pos()
                recordList=adding_coin(screenW,pos,which_player,recordList)
                pg.mixer.music.load('coins.mp3')
                pg.mixer.music.play()
                which_player=not which_player
                if  x3<= pos[0] <= x3+l and y <= pos[1] <= y+w: 
                        welcome()


       #Displaying Player:
       
            
        pg.display.update()
            
        #filling screen
        screen.fill(bgcolor)
    
        #Draw Circles
        drawCircles(screenW,screenH,recordList,screen,game_play,pg.mouse.get_pos())

        #Deciding winner
        x=check_win(recordList)
        if x!=0:
             #1 for player 1, 2 for player 2
            #bgcolor=[0,0,0]
            #running=False
            end_text(x,bgcolor,recordList)
            game_play=False

        else:
            y=check_draw(recordList)
            if y:
                #bgcolor=[0,0,0]
                game_play=False
                #running=False
                end_text(x,bgcolor,recordList)
        if x!=0:
            while check2:
                pg.mixer.music.load('mario.mp3')
                pg.mixer.music.play()
                check2=not check2
                
            

        if game_play:
            player_text(which_player)
            moving_circle(which_player)
            pos = pg.mouse.get_pos()
            # if mouse is hovered on a button it
            # changes to lighter shade 
            
            if  x3<= pos[0] <= x3+l and y <= pos[1] <= y+w:
                text1 = font3.render('<<Back' , True , lav,black)
                screen.blit(text1,(x3,y))
            
            else:
                text1 = font3.render('<<Back' , True , white)
                screen.blit(text1,(x3,y))
            
 
        if not game_play:
            text1 = font2.render('Play Again' , True , white)
            text2 = font2.render('Quit' , True , white)
            text3 = font2.render('Menu', True, white)
            pos = pg.mouse.get_pos()
            # if mouse is hovered on a button it
            # changes to lighter shade 
            #(200,520) (500,520)
            l1,l2,w=170,80,50
            x3,x2,x1,y=90,510,265,515
            if  x1<= pos[0] <= x1+l1 and y <= pos[1] <= y+w:
                pg.draw.rect(screen, blue, [x1, y, l1 , w])
                pg.draw.rect(screen, darkb, [x2, y, l2 , w]) 
                pg.draw.rect(screen, darkb, [x3, y, 90, w])
            
            elif x2 <= pos[0] <= x2+l2 and y <= pos[1] <= y+w:
                pg.draw.rect(screen, darkb, [x1, y, l1 , w])
                pg.draw.rect(screen, blue, [x2, y, l2 , w]) 
                pg.draw.rect(screen, darkb, [x3, y, 90, w])
            elif x3 <= pos[0] <= x3+90 and y <= pos[1] <= y+w:
                pg.draw.rect(screen, darkb, [x1, y, l1 , w])
                pg.draw.rect(screen, darkb, [x2, y, l2 , w]) 
                pg.draw.rect(screen, blue, [x3, y, 90, w])
            else:
                pg.draw.rect(screen, darkb, [x1, y, l1 , w])
                pg.draw.rect(screen, darkb, [x2, y, l2 , w]) 
                pg.draw.rect(screen, darkb, [x3, y, 90, w])
            
            screen.blit(text1 , (x1 +17 , y+10))
            screen.blit(text2 , (x2+12, y+10))
            screen.blit(text3, (x3+10, y+10))

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    exit_game = True
                    pg.quit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    #clicking Play again
                    if  x1<= pos[0] <= x1+l1 and y <= pos[1] <= y+w: 
                        pg.mixer.music.load('bell.mp3')
                        pg.mixer.music.play()
                        main_game() 

                    elif x3 <= pos[0] <= x3+90 and y <= pos[1] <= y+w:
                        pg.mixer.music.load('bell.mp3')
                        pg.mixer.music.play()
                        welcome()    
                    
                    elif x2 <= pos[0] <= x2+l2 and y <= pos[1] <= y+w:
                        pg.mixer.music.load('bell.mp3')
                        pg.mixer.music.play()
                        pg.quit()

def instr():
    exit_game = False
    text3 = newfont.render('<<Back' , True , black)
    text4 = newfont.render('<<Back' , True , white)
    text5 = font4.render('Instructions...',True, black)
    text6 = font3.render('• Connect Four is a 2-player game. Players ',True, black)
    text7 = font3.render( ' alternate taking turns. There is one colour', True, black)
    text8 = font3.render(' for each player.', True, black)
    text9 = font3.render('• When it is your turn, click on any of the ',True, black)
    text10 = font3.render(' columns. This will change the colour of ',True, black)
    text11 = font3.render(' the lowest black circle in that column.',True,black)
    text12 = font3.render('• The goal of Connect Four is to get 4',True, black)
    text13 = font3.render(' of your colour circles in a row —',True, black)
    text14 = font3.render(' horizontally, vertically, or diagonally ',True,black)
    text15 = font3.render(' before your opponent does.', True, black)
    text16 = font3.render('• Alright, let\'s play now!',True, black)


    while not exit_game:
        screen.fill((0, 0, 0))
        screen.blit(img1, (0,0))
        screen.blit(text3 , (260 , 480))
        screen.blit(text5,(120,30))
        screen.blit(text6,(10,120))
        screen.blit(text7,(25,140))
        screen.blit(text8,(25,160))
        screen.blit(text9,(10,210))
        screen.blit(text10,(25,230))
        screen.blit(text11,(25,250))
        screen.blit(text12,(10,300))
        screen.blit(text13,(25,320))
        screen.blit(text14,(25,340))
        screen.blit(text15,(25,360))
        screen.blit(text16,(10,410))
        pos = pg.mouse.get_pos()
        if 240 <= pos[0] <= 440 and 440 <= pos[1] <= 580:
            screen.blit(text4 , (260 , 480))


        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit_game = True
                pg.quit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if 240 <= pos[0] <= 440 and 440 <= pos[1] <= 580:
                    welcome()
        
        pg.display.update()

def check_draw(L):
    for i in range(6):
        if 0 in L[i]:
            return False
            break
    else:
        return True

#creating display
# 500,500 gives size of window
screenH, screenW=500,700
screen = pg.display.set_mode([screenW, screenH+100])

bgimg = pg.image.load("7182008.jpg")
bgimg = pg.transform.scale(bgimg, (screenW, screenH+100)).convert_alpha()

img = pg.image.load("app.jpg")
img = pg.transform.scale(img, (350, screenH+100)).convert_alpha()

img1 = pg.image.load("bg.jpg")
img1= pg.transform.scale(img1, (screenW, screenH+100)).convert_alpha()

pg.display.set_caption("Connect4")
welcome()
pg.quit()

