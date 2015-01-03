# -*- coding: utf-8 -*-
from Vec2D import *
import pygame
from pygame.locals import *
import pygame.gfxdraw

from config import *
from Util import *

class Screen(object):
    """here should happen all the drawing"""
    
    def __init__(self):
        self.screen = pygame.display.set_mode((MAX_X, MAX_Y + STATUSHEIGHT))        
        
    def getfont(self):
        font = pygame.font.match_font('freesans', bold=True)
        if font:
            return font
        else:
            if 'font' in DEBUG: print "Found no font, fallback to system font." 
            return pygame.font.get_default_font()


    def draw_image(self,image,pos,size,color,angle=0):
        image = pygame.image.load(image)
        image = pygame.transform.rotate(image,360-angle)
        w,h = image.get_size()
        pos = (pos[0]-w/2,pos[1]-h/2)
        self.screen.blit(image,pos)
    

    def draw_triangle(self,pos,size,color,angle=0):
        """draws an equilateral triangle in the outer circle at pos with size in color"""
        b = size / 2
        x = (size*size - b*b) ** .5
        
        triangle = ((0,-size),(x,b),(-x,b))
        if angle:
            triangle = rotate_poly(triangle,angle)
        poly = move_poly(triangle,pos)
        pygame.draw.polygon(self.screen,color,poly,0)
            
    
    
    def draw_square(self,pos,size,color,angle=0):
        """draw square at pos with size in color"""
    
        square = ((-size,-size),(-size,size),(size,size),(size,-size))
        if angle:
            square = rotate_poly(square,angle)
        rect = move_poly(square,pos)
        
        pygame.draw.polygon(self.screen,color,rect,0)
        
        
    def draw_rhombus(self,pos,size,color,angle=0):
        """draw rhombus at pos with size in color"""
        
        self.draw_square(pos,size,color,angle+45)
        
    
    def draw_semicircle(self,pos,size,color,angle=0):
        '''draws a semicircle at pos with size in color. needs a patched pygame'''
        
        # rect = pygame.Rect(int(pos[0]-size/2),int(pos[1]-size/2),size,size)
        # pygame.draw.arc(self.screen,color,rect,0,math.pi/2,0)
        
        pygame.gfxdraw.filled_pie(self.screen,int(pos[0]),int(pos[1]),size,int(0+angle),int(180+angle),color)
        

    def center_text(self,pos,string,color=BLACK,size=FONTSIZE):
        """TODO BUGGY: prints string centered at pos"""
    
        font = pygame.font.Font(self.getfont(),size)
        text = font.render(string, True, color)
        rect = text.get_rect()
        pos = list(pos)
        pos[0] -= int(rect.width/2)
        pos[1] -= int(rect.height/2)
        self.screen.blit(text, pos)
    

    def text(self,pos,string,color=BLACK,size=FONTSIZE):
        """prints string in default font at pos"""
        
        font = pygame.font.Font(self.getfont(),size)
        text = font.render(string, True, color)
        self.screen.blit(text, pos)
    
    
    def pause(self):
        self.text((MAX_X-RIGHT_OFFSET+10,MAX_Y-60),"PAUSED")
        
    def score(self,score):
        self.text((MAX_X-RIGHT_OFFSET+10,MAX_Y-40),"$: " + str(score))
        
    def status(self,text):
        """draw a status text at the bottom line"""
        
        self.text((0,MAX_Y+4),text)
        
                                          


