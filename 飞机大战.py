import pygame
from pygame.locals import *
import time
import random

'''pygame.mixer.init()

pygame.mixer.music.load("bg_music.ogg")
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play()'''
class heroplane:
    def __init__(self,scr_temp):
        self.x = 200
        self.y = 400
        self.scr = scr_temp
        self.image = pygame.image.load("./images/me.png")
        self.bullet_list=[]
    def play(self):
        for b in self.bullet_list:
            b.play()
            if b.move():
                self.bullet_list.remove(b)
        self.scr.blit(self.image,(self.x,self.y))
    def move_left(self):
        self.x -= 10
        if self.x <= 0:
            self.x = 0
    def move_right(self):
        self.x += 10
        if self.x >= 406:
            self.x = 406
    def move_up(self):
        self.y -= 10
        if self.y <= 0:
            self.y = 0
    def move_down(self):
        self.y += 10
        if self.y >= 492:
            self.y = 492
    def fire(self):
        self.bullet_list.append(bullet(self.scr,self.x,self.y))
    def detect_boom(self,enemy):
        image1 = pygame.image.load("./images/boom.png")
        for bo in enemy.enbullet_list:
            if bo.x>=self.x+12 and bo.x<=self.x+92 and bo.y>=self.y+20 and bo.y<=self.y+60:
                self.scr.blit(image1, (self.x, self.y))
                enemy.enbullet_list.remove(bo)
                return True
class bullet:
    def __init__(self,scr_temp,x,y):
        self.x = x+25
        self.y = y
        self.scr = scr_temp
        self.image = pygame.image.load("./images/pd.png")
    def play(self):
        self.scr.blit(self.image,(self.x,self.y))
        self.scr.blit(self.image,(self.x+55, self.y))
    def move(self):
        self.y -= 20
        if self.y <= -20:
            return True
class enemy:
    def __init__(self,scr_temp):
        self.x = random.choice(range(407))
        self.y = -75
        self.scr = scr_temp
        self.image = pygame.image.load("./images/e0.png")
        self.enbullet_list = []
    def play(self):
        for e in self.enbullet_list:
            e.play()
            if e.move():
                self.enbullet_list.remove(e)
        self.scr.blit(self.image,(self.x,self.y))
    def move(self,hero):
        self.y += 6
        image1 = pygame.image.load("./images/boom.png")
        for bo in hero.bullet_list:
            if bo.x>=self.x-18 and bo.x<=self.x+92 and bo.y>=self.y+20 and bo.y<=self.y+60:
                self.scr.blit(image1, (self.x, self.y))
                hero.bullet_list.remove(bo)
                return True

        if self.y >= 568:
            return True
    def fire(self):
        self.enbullet_list.append(en_bullet(self.scr,self.x,self.y))
class en_bullet:
    def __init__(self,scr_temp,x,y):
        self.x = x+58
        self.y = y+41
        self.scr = scr_temp
        self.image = pygame.image.load("./images/pd.png")
    def play(self):
        self.scr.blit(self.image,(self.x,self.y))
    def move(self):
        self.y += 15
        if self.y >= 600:
            return True
def key_control(hero_temp):
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    pk = pygame.key.get_pressed()
    if pk[K_LEFT]:
        hero_temp.move_left()
    elif pk[K_RIGHT]:
        hero_temp.move_right()
    elif pk[K_UP]:
        hero_temp.move_up()
    elif pk[K_DOWN]:
        hero_temp.move_down()
    if pk[K_SPACE]:
        hero_temp.fire()
def main():
    scr = pygame.display.set_mode((512,568),0,0)
    bg = pygame.image.load("./images/bg2.png")
    m = -968
    hero = heroplane(scr)
    enlist = []
    xa = 0
    kill = 0
    while True:
        scr.blit(bg, (0, m))
        m += 2
        if m >=-200:
            m = -968
        key_control(hero)
        hero.play()
        if random.choice(range(20)) == 10:
            enlist.append(enemy(scr))
        for en in enlist:
            if xa%300 == 0:
                en.fire()
            en.play()
            if hero.detect_boom(en):
                kill += 1
            if kill == 10:
                exit()
            if en.move(hero):
                enlist.remove(en)

        pygame.display.update()
        xa += 50
        time.sleep(0.04)
if __name__ == "__main__":
    main()