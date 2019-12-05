import random
import main
import math

class MoveInfomation:
    def __init__(self,pos,move,start,time):
        self.pos = pos
        self.move = move
        self.start = start
        self.time = time
        print(move)
    
class MoveObject:
    def __init__(self,size,speed):
        if size[0] <= 0:
            size[0] = 1
        if size[1] <= 0:
            size[1] = 1
        if speed <= 0:
            speed = 1
        self.size = size
        self.speed = speed
        self.moveinfo = self.SetMoveInfomation([random.randrange(0,1280),random.randrange(0,720)],[random.randrange(0,1280),random.randrange(0,720)])
        self.rect = main.pygame.Rect(self.moveinfo.pos[0],self.moveinfo.pos[1],self.size[0],self.size[1])
        self.eatCnt = 0
        self.lifeTime = 0

    def SetMoveInfomation(self,pos,move):
        info = MoveInfomation(pos,move,pos,0)

        return info

    def ReSetMoveInfomation(self,move):
        self.moveinfo.start = self.moveinfo.move
        self.moveinfo.move = move
        self.moveinfo.time = 0
    
    def draw(self):
        self.rect = pygame.Rect(self.moveinfo.pos[0],self.moveinfo.pos[1],self.size[0],self.size[1])
        main.pygame.draw.rect(main.screen,[0,0,0],self.rect,0)

    def move(self,deltaTime):
        if abs(self.moveinfo.pos[0] - self.moveinfo.move[0]) < self.speed:
            pass
        elif self.moveinfo.pos[0] >= self.moveinfo.move[0]:
            self.moveinfo.pos[0] -= self.speed
        elif self.moveinfo.pos[0] <= self.moveinfo.move[0]:
            self.moveinfo.pos[0] += self.speed  

        if abs(self.moveinfo.pos[1] - self.moveinfo.move[1]) < self.speed:
            pass
        elif self.moveinfo.pos[1] >= self.moveinfo.move[1]:
            self.moveinfo.pos[1] -= self.speed
        elif self.moveinfo.pos[1] <= self.moveinfo.move[1]:
            self.moveinfo.pos[1] += self.speed  

        if abs(self.moveinfo.pos[0] - self.moveinfo.move[0]) < self.speed and abs(self.moveinfo.pos[1] - self.moveinfo.move[1]) < self.speed:
            self.ReSetMoveInfomation([random.randrange(0,1280),random.randrange(0,720)])

    def moveKey(self,x,y):
        self.moveinfo.pos[0] = x
        self.moveinfo.pos[1] = y

    def __del__(self):
        print("del")

    

class BlackObject(MoveObject):
    def draw(self):
        main.pygame.draw.rect(main.screen,[0,0,0],[self.moveinfo.pos[0],self.moveinfo.pos[1],self.size[0],self.size[1]],0)
        self.rect = main.pygame.Rect(self.moveinfo.pos[0],self.moveinfo.pos[1],self.size[0],self.size[1])

    def Collistion(self,checklist,isDel):
        for index,c in enumerate(checklist):
            if self.rect.colliderect(c.rect):
                if isDel:
                    del checklist[index]

                return True

        return False

    def LifeTime(self,deltatime,checklist,index):
        self.lifeTime += deltatime
        if self.lifeTime >= 5:
            del checklist[index]
    
class RedObject(MoveObject):
    def draw(self):
        main.pygame.draw.rect(main.screen,[255,0,0],[self.moveinfo.pos[0],self.moveinfo.pos[1],self.size[0],self.size[1]],0)
        self.rect = main.pygame.Rect(self.moveinfo.pos[0],self.moveinfo.pos[1],self.size[0],self.size[1])

class YellowObject(MoveObject):
    def draw(self):
        main.pygame.draw.rect(main.screen,[200,200,0],[self.moveinfo.pos[0],self.moveinfo.pos[1],self.size[0],self.size[1]],0)
        self.rect = main.pygame.Rect(self.moveinfo.pos[0],self.moveinfo.pos[1],self.size[0],self.size[1])

    def __del__(self):
        print("del Yellow")
