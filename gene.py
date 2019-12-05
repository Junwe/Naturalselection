import random
import objects

class gene:
    def __init__(self,parents):
        self.parents = parents

    def CreateNewGene(self,count):
        for i in range(count):
            randnum = random.randrange(0,len(self.parents)-1)
            num = random.randrange(0,10)
            if num <= 4:
                obj = objects.BlackObject([self.parents[randnum].size[0] + random.randrange(-5,5),self.parents[randnum].size[1]+ random.randrange(-5,5)],self.parents[randnum].speed + random.randrange(-1,2))
                self.parents.append(obj)
            else:
                obj = objects.BlackObject(self.parents[randnum].size,self.parents[randnum].speed)
                self.parents.append(obj)

    def CreateBaseGene(self,base,count):
        for i in range(count):
            num = random.randrange(0,10)
            if num <= 4:
                obj = objects.BlackObject([base.size[0] + random.randrange(-5,5),base.size[1]+ random.randrange(-5,5)],base.speed + random.randrange(-1,2))
                self.parents.append(obj)
            else:
                obj = objects.BlackObject(base.size,base.speed)
                self.parents.append(obj)

    def __del__(self):
        print("gene del")