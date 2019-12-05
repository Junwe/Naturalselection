from random import random
from objects import *
from gene import *
import pygame

class TimeCounter:
    def __init__(self,time):
        self.time = time
        self.count = 0

    def CountTime(self,deltaTime):
        self.count += deltaTime
        if self.count>=self.time:
            self.count = 0
            return True
        return False

pygame.init()
screen = pygame.display.set_mode([1280,720])

done = False
clock = pygame.time.Clock()
t = pygame.time.get_ticks()
getTicksLastFream = t

blockCreateTime = TimeCounter(1)
YellowCreateTime = TimeCounter(2)

playtime = 0
geneNum = 0

def PlayTimePrint(deletatime,geneNum):
    global playtime
    playtime += deletatime
    fontTime = pygame.font.Font(None,30)
    fontGene = pygame.font.Font(None,30)
    textTime = fontTime.render(u"Time : " + str(round(playtime)),True,(0,0,0))
    textGene = fontTime.render(u"Gene : " + str(geneNum),True,(0,0,0))
    screen.blit(textTime,(0,50))
    screen.blit(textGene,(0,80))

def CreateYellow():
        for i in range(100):
            objYellow.append(YellowObject([5,5],5))


if __name__ == "__main__":
    objRed = [RedObject([30,30],5)]
    objBlock = [BlackObject([30,30],5)]
    objYellow = [YellowObject([5,5],5)]

    for i in range(10):
        objBlock.append(BlackObject([30,30],5))

    for i in range(5):
        objRed.append(RedObject([30,30],5))
    
    for i in range(50):
        objYellow.append(YellowObject([5,5],5))


    blockgene = gene(objBlock)

    while not done:
        clock.tick(60)

        t = pygame.time.get_ticks()
        # deltaTime in seconds.
        deltaTime = (t - getTicksLastFream) / 1000.0
        getTicksLastFream = t

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            '''if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x,mouse_y = pygame.mouse.get_pos()
                objRed[0].moveKey(mouse_x,mouse_y)'''
    
        screen.fill([255,255,255])

        '''if blockCreateTime.CountTime(deltaTime):
            blockgene.CreateNewGene(30)
            geneNum += 1'''

        if YellowCreateTime.CountTime(deltaTime):
            CreateYellow()

        for r in objRed:
            r.move(deltaTime)
            r.draw()

        for index,b in enumerate(blockgene.parents):
            b.move(deltaTime)
            b.draw()

            if b.Collistion(objRed,False):
                del blockgene.parents[index]
            if b.Collistion(objYellow,True):
                b.eatCnt += 1
                b.lifeTime = 0
                if b.eatCnt >= 3:
                    b.eatCnt = 0
                    blockgene.CreateBaseGene(b,3)

            b.LifeTime(deltaTime,blockgene.parents,index)

        for y in objYellow:
            y.draw()
                
            

        PlayTimePrint(deltaTime,geneNum)

        pygame.display.flip()


    