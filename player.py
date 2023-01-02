import pygame
# import skel

class animation():
    #self.rect: where to place the image
    #self.frames: the images 
    #self.frameTime: the time inbetween frames
    #self.repeat: if the animation repeats
    def __init__ (self, frames, frameTime, repeat):
        self.frames = frames
        self.frameTime = frameTime
        self.index = 0
        self.count = 0
        self.repeat = repeat
    
    def update(self, screen, rect):
        screen.blit(self.frames[self.index], rect)

        if self.count == self.frameTime[self.index]:
            if self.repeat == True:
                self.index = (self.index + 1) % len(self.frames) #ensures repeatio
            else:
                self.index = self.index + 1
                if self.index >= len(self.frames):
                    self.index = len(self.frames) - 1
            self.count = 0
        self.count = self.count + 1
    
    def changeFrame(self, newTimes):
        self.frameTime = newTimes
        self.index = 0
        self.count = 0
        print(self.frameTime)
        


class Player():
    
    def __init__ (self, width):
            #Idle
        idle1 = pygame.image.load("images\\Naruto\\Idle\\px1080\\idle1.png")
        DEFAULT_IMAGE_SIZE = (idle1.get_height() /2 ,  width * 0.08)
        idle1 = pygame.transform.scale(pygame.image.load("images\\Naruto\\Idle\\px1080\\idle1.png"), DEFAULT_IMAGE_SIZE)
        idle2 = pygame.transform.scale(pygame.image.load("images\\Naruto\\Idle\\px1080\\idle2.png"), DEFAULT_IMAGE_SIZE)
        idle3 = pygame.transform.scale(pygame.image.load("images\\Naruto\\Idle\\px1080\\idle3.png"), DEFAULT_IMAGE_SIZE)
        idle4 = pygame.transform.scale(pygame.image.load("images\\Naruto\\Idle\\px1080\\idle4.png"), DEFAULT_IMAGE_SIZE)
        playerIdleFrames = [idle1, idle2, idle3, idle4]
        # Scale the image to your needed size
        playerIdleTimeFrames = [7, 7, 7, 7]
        self.idle = animation(playerIdleFrames, playerIdleTimeFrames, True)

        #Running 
        idle1 = pygame.transform.scale(pygame.image.load("images\\Naruto\\Run\\1.png"), DEFAULT_IMAGE_SIZE)
        idle2 = pygame.transform.scale(pygame.image.load("images\\Naruto\\Run\\2.png"), DEFAULT_IMAGE_SIZE)
        idle3 = pygame.transform.scale(pygame.image.load("images\\Naruto\\Run\\3.png"), DEFAULT_IMAGE_SIZE)
        idle4 = pygame.transform.scale(pygame.image.load("images\\Naruto\\Run\\4.png"), DEFAULT_IMAGE_SIZE)
        idle5 = pygame.transform.scale(pygame.image.load("images\\Naruto\\Run\\5.png"), DEFAULT_IMAGE_SIZE)
        idle6 = pygame.transform.scale(pygame.image.load("images\\Naruto\\Run\\6.png"), DEFAULT_IMAGE_SIZE)
        # Set the size for the image

        playerIdleFrames = [idle1, idle2, idle3, idle4, idle5, idle6]
        for i in range(len(playerIdleFrames)):
            playerIdleFrames[i] = pygame.transform.flip(playerIdleFrames[i], True, False)
            
        # Scale the image to your needed size 
        playerIdleTimeFrames = [4, 4, 4, 3, 4, 4]
    
        self.run = animation(playerIdleFrames, playerIdleTimeFrames, True)

        #Jumping
        idle1 = pygame.transform.scale(pygame.image.load("images\\Naruto\\jump\\1.png"), DEFAULT_IMAGE_SIZE)
        idle2 = pygame.transform.scale(pygame.image.load("images\\Naruto\\jump\\2.png"), DEFAULT_IMAGE_SIZE)
        idle1 = pygame.image.load("images\\Naruto\\jump\\1.png")
        DEFAULT_IMAGE_SIZE = (idle1.get_height() /2 ,  idle1.get_width() /2)
        idle1 = pygame.transform.scale(pygame.image.load("images\\Naruto\\jump\\1.png"), DEFAULT_IMAGE_SIZE)
        idle2 = pygame.transform.scale(pygame.image.load("images\\Naruto\\jump\\2.png"), DEFAULT_IMAGE_SIZE)
        playerIdleTimeFrames = [10, 10]
        playerIdleFrames = [idle1, idle2]
        self.jump = animation(playerIdleFrames, playerIdleTimeFrames, False)




    #determine which animation state I should be in 
    def update(self, screen, rect, animationNum):
        if (animationNum == "run"):
            self.run.update(screen, rect)
        elif (animationNum == "walk"):
            self.idle.update(screen, rect)
        elif (animationNum == "jump"):
            self.jump.update(screen, rect)


    def changeFrameTime(self, animationNum, newTimes):
        if (animationNum == "run"):
            self.run.changeFrame(newTimes)
        elif (animationNum == "walk"):
            self.idle.changeFrame(newTimes)
        elif (animationNum == "jump"):
            self.jump.changeFrame(newTimes)
        

        
