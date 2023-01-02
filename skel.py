# skeleton code for project 2
# vis 142 fall 2022 
# This can take 20 minutes to hours to run.

# imports, don't change these but you can add imports you need
import pygame
from pygame.locals import *
from sys import exit
import random
import time
import player
# record the start time
start_time = time.time()

#####################################################################
# We will be producing 4K video from an image sequence
# Important: you might want to work at lower resolution that fits, 
# your screens! Such as 1920 x 1080.
# And then change these back to 4096 × 2160 for production.
# On the other hand, you will have to deal with scaling issues if you do.
#####################################################################
# width = 1920
# height = 1080

width = 4096 
height = 2160 

#####################################################################
# Name and title, update to your name and title
#####################################################################
name = "Jack Wagner"
title = "Microtransactions Mario" 

#####################################################################
# IMPORTANT - you will get your start sequence number from your TA
# If you use the default number 1000000 below, your work will not 
# be part of the class reel, as in every student must have different
# start sequence numbers.
#####################################################################
start_sequence_num = 1480000 # CHANGE HERE1480000

# Do not change these variables
# normal pygame stuff
clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('generate 4K animation pngs')
frame_num = start_sequence_num
titles_font = pygame.font.SysFont(None, int(width/12)) # if name or title run off screen, try setting the literal to 16 instead of 12
name_f = titles_font.render(name, True, (255,255,255))
title_f = titles_font.render(title, True, (255,255,255))

# print resolution warning
if (width != 4096 and height != 2160):
    print("Warning: dimensions not 4K, be sure width and height are set to 4096 and 2160.")
    Xscale = 1
    Yscale = 1
else:
    Xscale = 2
    screenScale = 2.13
    Yscale = 2

# this function makes one second of black frames
def make_black():
    global frame_num
    screen.fill((0,0,0))
    pygame.display.update()
    for i in range(0, 60):
    #    pygame.image.save(screen, "./frames/" + str(frame_num) + ".png")
       frame_num = frame_num + 1
       clock.tick(60)
        

# this is the credits loop, which puts the title of your work
# and your name on the screen
# make_black() # one second black
# # produce title sequence
screen.fill((0,0,0))
screen.blit(name_f, (int(width/8), int(width/8)))
screen.blit(title_f, (int(width/8), int(width/4))) 
for i in range(0, 3*60):
    pygame.display.update()
    # pygame.image.save(screen, "./frames/" + str(frame_num) + ".png")
    frame_num = frame_num + 1
    clock.tick(60)
make_black() # one second black
make_black() # one second black

# create a surface object, image is drawn on it.
background = pygame.image.load("images\world4KTrans.png").convert_alpha()
# Using blit to copy content from one surface to other
screen.blit(background, (0, 0))
pole1 = pygame.image.load("images\pole1.png")
pole1Rect = pygame.Rect(2702 * Xscale, 487 * Yscale, pole1.get_width(), pole1.get_height())
pole2 = pygame.image.load("images\pole2.png")
pole2Rect = pygame.Rect(18202 * Xscale, 0 * Yscale, pole2.get_width(), pole2.get_height())


# Using blit to copy content from one surface to other

x = 800
y = 770

camX = 0

walkSpeed = 1 #animation 1 
runSpeed = 1 #animation 2
dashSpeed = 1

cameraSpeedwalk = 7
cameraSpeedrun = 14
cameraSpeedDash= 20 #19.32
cameraSpeed = 0

startingSeq = 180 #the intro scene will occupy the first 3 seconds of play time

frame_num_neg_3 = frame_num + 60
frame_num_neg_2 = frame_num_neg_3 + 60
frame_num_neg_1 = frame_num_neg_2 + 60
frame_num_1 = frame_num_neg_1 + 60
frame_num_2 = frame_num_1 + 60
frame_num_3 = frame_num_2 + 60
frame_num_4 = frame_num_3 + 60
frame_num_5 = frame_num_4 + 60
frame_num_6 = frame_num_5 + 60
frame_num_7 = frame_num_6 + 60
frame_num_8 = frame_num_7 + 60
frame_num_9 = frame_num_8 + 60
frame_num_10 = frame_num_9 + 60
frame_num_11 = frame_num_10 + 60
frame_num_12 = frame_num_11 + 60
frame_num_13 = frame_num_12 + 60
frame_num_14 = frame_num_13 + 60
frame_num_15 = frame_num_14 + 60
frame_num_16 = frame_num_15 + 60
frame_num_17 = frame_num_16 + 60
frame_num_18 = frame_num_17 + 60
frame_num_19 = frame_num_18 + 60
frame_num_20 = frame_num_19 + 60

pc = player.Player(width)
animationNum = "walk"
jumping = False
Falling = False
jumpAmt = 220
landAmt = 770
jumper = 10
lander = 10
willFall = True
wait = 0 #frames
#time line 
#1st frame of movement 
#frame 18 is where the camera catches up
#around 34 frames the camera is on par with mario

#Chun Li
idle1 = pygame.image.load("images\\ChunLi\\idle\\1.png")
DEFAULT_IMAGE_SIZE = (idle1.get_height() / 3,  width * 0.08)
idle1 = pygame.transform.scale(pygame.image.load("images\\ChunLi\\idle\\1.png"), DEFAULT_IMAGE_SIZE)
idle2 = pygame.transform.scale(pygame.image.load("images\\ChunLi\\idle\\2.png"), DEFAULT_IMAGE_SIZE)
idle3 = pygame.transform.scale(pygame.image.load("images\\ChunLi\\idle\\3.png"), DEFAULT_IMAGE_SIZE)

chunIdleFrames = [idle1, idle2, idle3]
# Scale the image to your needed size
chunIdleTimeFrames = [12, 9, 12]
idleChun = player.animation(chunIdleFrames, chunIdleTimeFrames, True)
idleChunRect = pygame.Rect((640 * screenScale) ,height/2, idle1.get_height(), idle1.get_width())


#---------------
#Mario
idle1 = pygame.image.load("images\Mario\idle.png")
DEFAULT_IMAGE_SIZE = (idle1.get_height(),  width * 0.08)
idle1 = pygame.transform.scale(pygame.image.load("images\Mario\idle.png"), DEFAULT_IMAGE_SIZE)

marioIdleFrames = [idle1]
# Scale the image to your needed size
marioIdleTimeFrames = [12]
idleMario = player.animation(marioIdleFrames, marioIdleTimeFrames, True)
idleMarioRect = pygame.Rect((960 * screenScale) - idle1.get_width(),height/2, idle1.get_height(), idle1.get_width())

#-------------------------------
idle1 = pygame.image.load("images\\Naruto\\Idle\\px1080\\idle1.png")
DEFAULT_IMAGE_SIZE = (idle1.get_height() /2 ,  width * 0.08)
idle1 = pygame.transform.scale(pygame.image.load("images\\Naruto\\Idle\\px1080\\idle1.png"), DEFAULT_IMAGE_SIZE)
idle2 = pygame.transform.scale(pygame.image.load("images\\Naruto\\Idle\\px1080\\idle2.png"), DEFAULT_IMAGE_SIZE)
idle3 = pygame.transform.scale(pygame.image.load("images\\Naruto\\Idle\\px1080\\idle3.png"), DEFAULT_IMAGE_SIZE)
idle4 = pygame.transform.scale(pygame.image.load("images\\Naruto\\Idle\\px1080\\idle4.png"), DEFAULT_IMAGE_SIZE)
playerIdleFrames = [idle1, idle2, idle3, idle4]
# Scale the image to your needed size
playerIdleTimeFrames = [7, 7, 7, 7]
idleNaruto = player.animation(playerIdleFrames, playerIdleTimeFrames, True)
idleNarutoRect = pygame.Rect((1700 * screenScale),height/2, idle1.get_height(), idle1.get_width())

#-------------------------------
#Spider
# 200 * Xscale, 180 * Xscale
idle1 = pygame.image.load("images\\Spiderman\\1.png")
DEFAULT_IMAGE_SIZE = (idle1.get_height() / 2,  width * 0.08)
idle1 = pygame.transform.scale(pygame.image.load("images\\Spiderman\\1.png"), DEFAULT_IMAGE_SIZE)
idle2 = pygame.transform.scale(pygame.image.load("images\\Spiderman\\2.png"), DEFAULT_IMAGE_SIZE)
idle3 = pygame.transform.scale(pygame.image.load("images\\Spiderman\\3.png"), DEFAULT_IMAGE_SIZE)

spiderIdleFrames = [idle1, idle2, idle3]
# Scale the image to your needed size
spiderIdleTimeFrames = [12, 9, 12]
idleSpider = player.animation(spiderIdleFrames, spiderIdleTimeFrames, True)
idleSpiderRect = pygame.Rect((width - (1800 * screenScale))/2,height/2, idle1.get_height(), idle1.get_width())

xChar = 11
spiderX = (320 * screenScale) - ((width * 0.08) / 2)
narutoX = (1600 * screenScale) - ((width * 0.08) / 2)
marioX = (960 * screenScale) - ((width * 0.08) / 2)
chunX = ((1600  + 640) * screenScale) - ((width * 0.08) / 2)
font = pygame.font.Font("GameBoy.ttf", 72 * Xscale)
text = font.render("Skin Selection", True, (255, 255, 255))
buttoncolor = (0,255,255)


idle1 = pygame.image.load("images\\Objects\\Lucky\\1.png")
DEFAULT_IMAGE_SIZE = (idle1.get_width(), idle1.get_height())
idle1 = pygame.transform.scale(pygame.image.load("images\\Objects\\Lucky\\1.png"), DEFAULT_IMAGE_SIZE)
idle2 = pygame.transform.scale(pygame.image.load("images\\Objects\\Lucky\\2.png"), DEFAULT_IMAGE_SIZE)
idle3 = pygame.transform.scale(pygame.image.load("images\\Objects\\Lucky\\3.png"), DEFAULT_IMAGE_SIZE)
idle4 = pygame.transform.scale(pygame.image.load("images\\Objects\\Lucky\\4.png"), DEFAULT_IMAGE_SIZE)
playerIdleFrames = [idle1, idle2, idle3, idle4]
# Scale the image to your needed size
playerIdleTimeFrames = [20, 20, 20, 20]
lucky = player.animation(playerIdleFrames, playerIdleTimeFrames, True)


luckyBlockRects = [pygame.Rect((4650 * Xscale), 590 * Yscale, idle1.get_height(), idle1.get_width()), 
                   pygame.Rect((4750 * Xscale), 590 * Yscale, idle1.get_height(), idle1.get_width()),
                   pygame.Rect((4850 * Xscale), 590 * Yscale, idle1.get_height(), idle1.get_width())]

idle1 = pygame.image.load("images\\Objects\\Lucky\\1.png")
DEFAULT_IMAGE_SIZE = (idle1.get_width(), idle1.get_height())
idle1 = pygame.transform.scale(pygame.image.load("images\\Objects\\Coin\\1.png"), DEFAULT_IMAGE_SIZE)
idle2 = pygame.transform.scale(pygame.image.load("images\\Objects\\Coin\\2.png"), DEFAULT_IMAGE_SIZE)
idle3 = pygame.transform.scale(pygame.image.load("images\\Objects\\Coin\\3.png"), DEFAULT_IMAGE_SIZE)
idle4 = pygame.transform.scale(pygame.image.load("images\\Objects\\Coin\\4.png"), DEFAULT_IMAGE_SIZE)
playerIdleFrames = [idle1, idle2, idle3, idle4]
# Scale the image to your needed size
playerIdleTimeFrames = [128, 128, 128, 128]
coin = player.animation(playerIdleFrames, playerIdleTimeFrames, True)



coinRects = [pygame.Rect((650 * Xscale), 45 * Yscale, idle1.get_height(), idle1.get_width()), 
                   pygame.Rect((775 * Xscale), -56 * Yscale, idle1.get_height(), idle1.get_width()),
                   pygame.Rect((900 * Xscale), -56 * Yscale, idle1.get_height(), idle1.get_width()), #end of first three coins
                   pygame.Rect((8700 * Xscale), -56 * Yscale, idle1.get_height(), idle1.get_width()), 
                   pygame.Rect((8825 * Xscale), -56 * Yscale, idle1.get_height(), idle1.get_width()),
                   pygame.Rect((8950 * Xscale), -56 * Yscale, idle1.get_height(), idle1.get_width()), #end of second three coins
                    #Start of the ending 13
                   pygame.Rect((16290 * Xscale), 590 * Yscale, idle1.get_height(), idle1.get_width()), 
                   pygame.Rect((16415 * Xscale), 490 * Yscale, idle1.get_height(), idle1.get_width()),
                   pygame.Rect((16540 * Xscale), 390 * Yscale, idle1.get_height(), idle1.get_width()), 
                   pygame.Rect((16665 * Xscale), 290 * Yscale, idle1.get_height(), idle1.get_width()), 
                   pygame.Rect((16790 * Xscale), 290 * Yscale, idle1.get_height(), idle1.get_width()),
                   pygame.Rect((16915 * Xscale), 290 * Yscale, idle1.get_height(), idle1.get_width()),
                   pygame.Rect((17040 * Xscale), 290 * Yscale, idle1.get_height(), idle1.get_width()),
                   pygame.Rect((17165 * Xscale), 290 * Yscale, idle1.get_height(), idle1.get_width()), 
                   pygame.Rect((17290 * Xscale), 290 * Yscale, idle1.get_height(), idle1.get_width()), 
                   pygame.Rect((17415 * Xscale), 290 * Yscale, idle1.get_height(), idle1.get_width()),
                   pygame.Rect((17540 * Xscale), 290 * Yscale, idle1.get_height(), idle1.get_width()),
                   pygame.Rect((17665 * Xscale), 290 * Yscale, idle1.get_height(), idle1.get_width()), 
                   pygame.Rect((17790 * Xscale), 290 * Yscale, idle1.get_height(), idle1.get_width())]

idle1 = pygame.image.load("images\\Objects\\YoshiCoin\\1.png")
DEFAULT_IMAGE_SIZE = (idle1.get_width(),  idle1.get_height())
idle1 = pygame.transform.scale(pygame.image.load("images\\Objects\\YoshiCoin\\1.png"), DEFAULT_IMAGE_SIZE)
idle2 = pygame.transform.scale(pygame.image.load("images\\Objects\\YoshiCoin\\2.png"), DEFAULT_IMAGE_SIZE)
playerIdleFrames = [idle1, idle2]
# Scale the image to your needed size
playerIdleTimeFrames = [32, 32]
yoshi = player.animation(playerIdleFrames, playerIdleTimeFrames, True)
yoshiRect = [pygame.Rect((1025 * Xscale), -140 * Yscale, idle1.get_width(), idle1.get_height()),
             pygame.Rect((9200 * Xscale), -140 * Yscale, idle1.get_width(), idle1.get_height())]

idle1 = pygame.image.load("images\\Objects\\Apple\\1.png")
DEFAULT_IMAGE_SIZE = (idle1.get_width(),  idle1.get_height())
idle1 = pygame.transform.scale(pygame.image.load("images\\Objects\\Apple\\1.png"), DEFAULT_IMAGE_SIZE)
idle2 = pygame.transform.scale(pygame.image.load("images\\Objects\\Apple\\2.png"), DEFAULT_IMAGE_SIZE)
idle3 = pygame.transform.scale(pygame.image.load("images\\Objects\\Apple\\3.png"), DEFAULT_IMAGE_SIZE)
idle4 = pygame.transform.scale(pygame.image.load("images\\Objects\\Apple\\4.png"), DEFAULT_IMAGE_SIZE)

playerIdleFrames = [idle1, idle2, idle1, idle3, idle4]
# Scale the image to your needed size
playerIdleTimeFrames = [64, 64, 64, 64, 64]
apple = player.animation(playerIdleFrames, playerIdleTimeFrames, True)
appleRect = [pygame.Rect((10 * Xscale), 172 * Yscale, idle1.get_width(), idle1.get_height()),
             pygame.Rect((5080 * Xscale), 700 * Yscale, idle1.get_width(), idle1.get_height()),
             pygame.Rect((7800 * Xscale), 700 * Yscale, idle1.get_width(), idle1.get_height()),
             pygame.Rect((10500 * Xscale), 700 * Yscale, idle1.get_width(), idle1.get_height()),
             pygame.Rect((11000 * Xscale), 600 * Yscale, idle1.get_width(), idle1.get_height()),
             pygame.Rect((12100 * Xscale), 600 * Yscale, idle1.get_width(), idle1.get_height()),
             pygame.Rect((13400 * Xscale), 700 * Yscale, idle1.get_width(), idle1.get_height()),]

idle1 = pygame.image.load("images\Objects\Bar.png")
DEFAULT_IMAGE_SIZE = (idle1.get_width(),  idle1.get_height())
bar = pygame.transform.scale(pygame.image.load("images\Objects\Bar.png"), DEFAULT_IMAGE_SIZE)
barRect = pygame.Rect((18036 * Xscale), 800 * Yscale, idle1.get_width(), idle1.get_height())
barDirection = 3


idle1 = pygame.image.load("images\subTitleImage.png")
DEFAULT_IMAGE_SIZE = (idle1.get_width(),  idle1.get_height())
titleImage = pygame.transform.scale(pygame.image.load("images\TitleImage.png"), DEFAULT_IMAGE_SIZE)
idle1 = pygame.image.load("images\TitleImage.png")
DEFAULT_IMAGE_SIZE = (idle1.get_width(),  idle1.get_height())
subTitleImage = pygame.transform.scale(pygame.image.load("images\subtitleImage.png"), DEFAULT_IMAGE_SIZE)



idle1 = pygame.transform.scale(pygame.image.load("images\\Naruto\\jump\\1.png"), DEFAULT_IMAGE_SIZE)
idle2 = pygame.transform.scale(pygame.image.load("images\\Naruto\\jump\\2.png"), DEFAULT_IMAGE_SIZE)
idle1 = pygame.image.load("images\\Naruto\\jump\\1.png")
DEFAULT_IMAGE_SIZE = (idle1.get_height() / 2,  width * 0.08)
idle1 = pygame.transform.scale(pygame.image.load("images\\Naruto\\jump\\1.png"), DEFAULT_IMAGE_SIZE)
idle2 = pygame.transform.scale(pygame.image.load("images\\Naruto\\jump\\2.png"), DEFAULT_IMAGE_SIZE)
playerIdleTimeFrames = [10, 10]
playerIdleFrames = [idle1, idle2]


name = font.render("Mario", True, (255, 255, 255))
name1 = font.render("Naruto", True, (255, 216, 0))
rarity = font.render("Default", True, (255, 255, 255))
rarity1 = font.render("Legendary", True, (255, 216, 0))

currName = name
currRarity = rarity
narutoStart = font.render("Naruto Start", True, (255,165,0))

loot = font.render("", True, (255,165,0))



lootY = -50
fadex = 0

camY = 0
cameraYSpeed = 0
camYMoving = False
alpha=120
ended = False
titleY = -200 * Yscale
subTitleY = -100 * Yscale   
intro = True
# here is the main animation loop
for i in range(0, 20*60): # 20*60 frames is 20 seconds
    #########################################################
    # in the skeleton, your animation goes from here ########
    #########################################################
    
    if frame_num > frame_num_neg_1: #frame_num_1 should be 180
        pygame.draw.rect(screen, pygame.Color("#cceff5"), (0,0,1920*screenScale,1500*Yscale))
        screen.blit(background, (camX * Xscale, camY * Yscale))
        #screen.blit(imp2, (x * Xscale, 300 * Yscale))
    
        if jumping: 
            wait = wait - 1 #subtracts frames how long you want to be in the air
            y = y - (jumper)
            
            if y <= jumpAmt:
                jumper = 0
                if wait == 0:
                    jumping = False 
                    if willFall == True:
                        Falling = True
        if Falling == True:
            y = y + (lander)
            if y >= landAmt:
                Falling = False

        player1 = pygame.Rect(x * Xscale, y * Yscale, height * 0.07, width * 0.08)
      
        #process Lucky Blocks
        for i in range(len(luckyBlockRects)):
            
            luckyBlockRects[i][0] = luckyBlockRects[i][0] - cameraSpeed * Xscale
            luckyBlockRects[i][1] = luckyBlockRects[i][1] + (cameraYSpeed * Yscale)
            lucky.update(screen, luckyBlockRects[i])
        
        #process Coins
        for i in range(len(coinRects)):
            coinRects[i][0] = coinRects[i][0] - cameraSpeed * Xscale
            coinRects[i][1] = coinRects[i][1] + (cameraYSpeed * Yscale)
            coin.update(screen, coinRects[i])
        
        for i in range(len(yoshiRect)):
            yoshiRect[i][0] = yoshiRect[i][0] - cameraSpeed * Xscale
            yoshiRect[i][1] = yoshiRect[i][1] + (cameraYSpeed * Yscale)
            yoshi.update(screen, yoshiRect[i])

        for i in range(len(appleRect)):
            appleRect[i][0] = appleRect[i][0] - cameraSpeed * Xscale
            appleRect[i][1] = appleRect[i][1] + (cameraYSpeed * Yscale)
            apple.update(screen, appleRect[i])

        barRect[0] =  barRect[0] - cameraSpeed * Xscale
        barRect[1] =  barRect[1] + (cameraYSpeed * Yscale)

        barRect[1] = barRect[1] + (barDirection * Yscale)
        if (barRect[1] < 50 * Yscale):
            barDirection = 3
        elif (barRect[1] > 798 * Yscale):
            barDirection = -3
        screen.blit(bar, barRect)

        pc.update(screen, player1, animationNum)
        collided = pygame.Rect.collidelist(player1, coinRects)
        if (collided != -1):
            coinRects.pop(collided)

        collided = pygame.Rect.collidelist(player1, yoshiRect)
        if (collided != -1):
            yoshiRect.pop(collided)
        
        #end of animation
        collided = pygame.Rect.colliderect(player1, barRect)
        if (collided):
            barRect = pygame.Rect(-1000,-1000,0,0)
            ended = True
            alpha = 0
            print(cameraSpeed)
            

        pole1Rect[0] =  pole1Rect[0] - (cameraSpeed * Xscale)
        pole1Rect[1] =  pole1Rect[1] + (cameraYSpeed * Yscale)
        screen.blit(pole1, pole1Rect)
        pole2Rect[0] =  pole2Rect[0] - (cameraSpeed * Xscale)
        pole2Rect[1] =  pole2Rect[1] + (cameraYSpeed * Yscale)
        screen.blit(pole2, pole2Rect)

        # luckyx = luckyx - cameraSpeed * Xscale
        # lucky.update(screen, luckyRect)
        # pygame.draw.rect(screen, (0,0,0), pygame.Rect(x * Xscale, y * Yscale, height * 0.07, width * 0.08))
        
        #begin
        if frame_num < frame_num_1 - 30:
            walkSpeed = 0
            cameraSpeed = 0
        elif frame_num < frame_num_1: 
            cameraSpeed = 0
            walkSpeed = 10
            animationNum = "run"
        
        else: 
            if ended == False:
                cameraSpeed = cameraSpeedDash
                if x != 500:
                    walkSpeed = -10
                    print("wowza")
                else: 
                    walkSpeed = 0
            else:
                cameraSpeed = cameraSpeed - (0.5)
                
                if cameraSpeed <= 0:
                    cameraSpeed = 0
                    animationNum = "walk"
                s = pygame.Surface((width,height))  # the size of your rect
                s.set_alpha(alpha)
                alpha = alpha + 4            # alpha level
                lootY = lootY + 3
                if (lootY >= 30):
                    lootY = 30
                s.fill((0,0,0))           # this fills the entire surface
                screen.blit(s, (0,0)) 
                screen.blit(loot, (int(width/2) - (loot.get_width() / 2), lootY))


        #first pipe jump
        if frame_num == frame_num_3 + 20:
            animationNum = "jump"
            jumping = True
            jumpAmt = 200
            jumper = 50
            lander = 30
            wait = 27
            newTimes = [20,20]
            pc.changeFrameTime(animationNum, newTimes)
            cameraYSpeed = 9

        if frame_num > frame_num_3+40 and frame_num < frame_num_4:
             cameraYSpeed = -7
             

            # y = 200 * Yscale
        if frame_num == frame_num_4 + 8:
            animationNum = "run"
            cameraYSpeed = 0
           
            # y = 770 * Yscale

        #jump to platform
        if frame_num == frame_num_8 - 40:
            animationNum = "jump"
            
            jumping = True
            jumpAmt = 319
            jumper = 50
            lander = 30
            wait = 35
            willFall = False
            newTimes = [5, 0]
            pc.changeFrameTime(animationNum, newTimes)
            cameraYSpeed = 10

        if frame_num > frame_num_8 - 37 and frame_num < frame_num_8 - 5:
             cameraYSpeed = 0
             animationNum = "run"


        #jump and camera moves
        if frame_num == frame_num_8 - 5:
            cameraYSpeed = 29
            animationNum = "jump"
            # jumping = True
            # jumpAmt = -100 * Yscale
            # jumper = 50 * Yscale
            # lander = 30 * Yscale
            wait = 35
            willFall = True
            newTimes = [25, 10]
            pc.changeFrameTime(animationNum, newTimes)

        if frame_num > frame_num_8+11 and frame_num < frame_num_9+10:
             cameraYSpeed = -9
             if frame_num > frame_num_8+35:
                y = y + (15)

        
        if frame_num == frame_num_9+10:
            cameraYSpeed = 0
            animationNum = "run"
            # y = 770 * Yscale

        #small pipe
        if frame_num == frame_num_10:
            animationNum = "jump"
            
            jumping = True
            jumpAmt = 400
            jumper = 60
            lander = 30
            wait = 17
            willFall = True
            newTimes = [15, 15]
            pc.changeFrameTime(animationNum, newTimes)

        if frame_num == frame_num_10+35:
            animationNum = "run"
            # y = 770 * Yscale

        #BIG PIPe
        if frame_num == frame_num_11:
            animationNum = "jump"
            jumping = True
            jumpAmt = 300
            jumper = 50
            lander = 30
            wait = 20
            willFall = True
            newTimes = [15, 10]
            pc.changeFrameTime(animationNum, newTimes)
        if frame_num == frame_num_11+40:
            animationNum = "run"
            # y = 770 * Yscale


        if frame_num == frame_num_12+20:
            animationNum = "jump"
            jumping = True
            jumpAmt = 200
            jumper = 50
            lander = 25
            wait = 40
            willFall = True
            newTimes = [30, 10]
            pc.changeFrameTime(animationNum, newTimes)
        
        if frame_num == frame_num_13+20:
            animationNum = "run"
            #y = 770 * Yscale

        if frame_num == frame_num_14+5:
            animationNum = "jump"
            jumping = True
            jumpAmt = 200
            jumper = 50
            lander = 29
            wait = 35
            willFall = True
            newTimes = [25, 15]
            pc.changeFrameTime(animationNum, newTimes)
            
        if frame_num == frame_num_15:
            animationNum = "run"
            # y = 770 * Yscale
        camX = camX - (cameraSpeed)
        camY = camY + (cameraYSpeed)
        x = x + (walkSpeed) 
    else:
    
        screen.fill((0,0,0))


    
        
        screen.blit(text, (int(width/2) - (text.get_width() / 2), int(width/8)))
        # screen.blit(name, ((width + 200)/2) - (text.get_width() / 2), int(height/2))
        # screen.blit(rarity, ((width + 200)/2) - (text.get_width() / 2), int(height/2))
        pygame.draw.polygon(screen, buttoncolor, (
                                                ((width/2) + (200 * screenScale), (height/2) + (200 * Yscale)),
                                                ((width/2) + (325 * screenScale), (height/2) + (300 * Yscale)),
                                                ((width/2) + (200 * screenScale), (height/2) + (400 * Yscale))))
        
        pygame.draw.polygon(screen, (0, 255, 255), (
                                                    (width/2 - (200 * screenScale), (height/2) + (200 * Yscale)),
                                                    (width/2 - (325 * screenScale), (height/2) + (300 * Yscale)),
                                                    (width/2 - (200 * screenScale), (height/2) + (400 * Yscale))))
        # idleChun.update(screen, idleChunRect)
        pygame.draw.rect(screen, (255,255,255), ((width/2) - (100*screenScale),(height/2) - (15*Yscale), 200 * screenScale, 180 * Yscale))
        idleMario.update(screen, idleMarioRect)
        idleNaruto.update(screen, idleNarutoRect)
        idleSpider.update(screen, idleSpiderRect)
        idleChun.update(screen, idleChunRect)

        idleSpiderRect = pygame.Rect(spiderX, height/2, idle1.get_height(), idle1.get_width())
        idleNarutoRect = pygame.Rect(narutoX, height/2, idle1.get_height(), idle1.get_width())
        idleMarioRect = pygame.Rect(marioX, height/2, idle1.get_height(), idle1.get_width())
        idleChunRect = pygame.Rect(chunX, height/2, idle1.get_height(), idle1.get_width())

        screen.blit(currName, ((width/2) - (currName.get_width() / 2),(height/2) - (150 * Yscale)))
        screen.blit(currRarity, ((width/2) - (currRarity.get_width() / 2),(height/2) + (450 * Yscale)))

        if frame_num > frame_num_neg_3+12 and frame_num < frame_num_neg_2+12:
            buttoncolor = (0, 100, 100)
            spiderX -= xChar * screenScale
            narutoX -= xChar * screenScale
            marioX -= xChar * screenScale
            chunX -= xChar * screenScale
        else:
            buttoncolor = (0, 255, 255)
        
        if frame_num > frame_num_neg_2 + 5:
            currName = name1
            currRarity = rarity1
        if frame_num > frame_num_neg_2 + 20:
            
            idleNaruto = player.animation(playerIdleFrames, playerIdleTimeFrames, True)
        
        titleY = titleY + (10 * Yscale)
        subTitleY = subTitleY + (10 * Yscale)
        if titleY >= 0:
            titleY = 0
        if subTitleY >= 100 * Yscale:
            subTitleY = 100 * Yscale
            intro = False
            # alpha = 0
        screen.blit(titleImage, ((width/2) - (titleImage.get_width() / 2), titleY))
        screen.blit(subTitleImage, ((width/2) - (subTitleImage.get_width() / 2), subTitleY))
        if frame_num > frame_num_neg_2 + 25:
            #fade to black
            s = pygame.Surface((width,height))  # the size of your rect
            s.set_alpha(alpha)
            alpha = alpha + 20               # alpha level
            s.fill((0,0,0))           # this fills the entire surface
            screen.blit(s, (0,0)) 
        if frame_num > frame_num_neg_2 + 40:
            #blit text that says naruto starts
            fadex = fadex + 200 * screenScale
            
            screen.blit(narutoStart, (int(width/2) - (text.get_width()/ 2), int(height/2)))
            pygame.draw.rect(screen, (0,0,0), (fadex, 0, width, height))
    
   
    
        
   
        

        
    
        





    #########################################################
    # to here ###############################################
    #########################################################
    # print out stats
   
    # The next line can be commented out to speed up testing frame rate
    # by not writing the file. But for output to final frames,
    # you will need to ucomment it.
    # pygame.image.save(screen, "./frames/" + str(frame_num) + ".png")
    frame_num = frame_num + 1
    pygame.display.update()
    clock.tick(60)

# print out stats
print("seconds:", int(time.time() - start_time))
print("~minutes: ", int((time.time() - start_time)/60))
print(frame_num)
# we just quit here
pygame.display.quit()
pygame.quit()
exit()

# you can make your files into a movie with ffmpeg:
# ffmpeg -r 60 -start_number 1000000 -s 4096x2160 -i %d.png -vcodec libx264 -crf 5 -pix_fmt yuv420p final.mp4
# with a few changes such as to start number, but this is just extra info here
