#!/usr/bin/python
# -*- coding: utf-8 -*-
# (c) 2014, Benni Baermann http://bennibaermann.de/
# COPYING: See LICENSE. This program is Free Software under AGPL

import pygame
from pygame.locals import *
# import Vec2D
# from Vec2D import *
import random

# own files
from config import *
from Util import *
import Screen
# import Game

class Hero:
    
    def __init__(self,screen):
        self.screen = screen
        
        self.stick = 0
        
        # possible phases: 'waiting', 'stick', 'falling', 'running'
        self.phase = 'waiting'
        
        self.pos = STARTPOS
        
        
    def draw(self):
        scr = self.screen.screen
        
        # draw hero
        pygame.draw.circle(scr,BLACK,self.pos,HEROSIZE)

        # draw stick
        stickstart = (self.pos[0]+HEROSIZE, self.pos[1]+HEROSIZE)
        if self.phase == 'stick':
            stickend = (stickstart[0] , stickstart[1] - self.stick)
        else:
            stickend = stickstart
        pygame.draw.line(scr,BLACK,stickstart,stickend,5)

########################################################################
# main programm
########################################################################

def main():
    # Initialise stuff
    gameover = False
    count = 0
    pygame.init()
    scr = Screen.Screen()
    screen = scr.screen
    pygame.display.set_caption('Stick And Run')
    clock = pygame.time.Clock()
    stick = 0 # length of stick
    dist = random.randint(MIN_GAP , MAX_Y - MAX_WIDTH - MIN_GAP)
    width = random.randint(MIN_WIDTH , MAX_WIDTH)
    status = 'Stick And Run!'
    score = 0
    
    hero = Hero(scr)
    
    # Event loop
    while 1:
      #try:
        count += 1
        
        # event handling
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            elif ( event.type == KEYDOWN or event.type == MOUSEBUTTONDOWN ) and hero.phase == 'waiting':
                hero.phase = 'stick'
            elif (event.type == MOUSEBUTTONUP or event.type == KEYUP ) and hero.phase == 'stick':
                hero.phase = 'falling'
            # elif event.type == pygame.VIDEORESIZE:
                # (MAX_X, MAX_Y) = event.size
            #    screen = pygame.display.set_mode(event.size, RESIZABLE)

        if hero.phase == 'stick':
            hero.stick += STICKSPEED
            flush_print (str(hero.stick))
            
        flush_print(hero.phase)
            
        screen.fill(WHITE)

        scr.status(status)
        scr.score(score)

        hero.draw()
        
        
        if gameover:
            scr.center_text((int(MAX_X/2),int(MAX_Y/2)),"GAME OVER!",BLACK,52)
            scr.center_text((int(MAX_X/2),int(MAX_Y/2)),"GAME OVER!",RED,50)
            scr.center_text((int(MAX_X/2),int(MAX_Y/2)+100),"click to restart",BLACK,20)
            scr.center_text((int(MAX_X/2),int(MAX_Y/2)+150),"Score: " + str(g.score),BLACK,20)
            status = "GAME OVER. click to restart."
            gameover = True
 
        pygame.display.update()
        msElapsed = clock.tick(FPS) # TODO(?): Gamespeed should be FPS-independent
    
        
if __name__ == '__main__': main()
