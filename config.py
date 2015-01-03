# -*- coding: utf-8 -*-

# set which part of the game you want to debug, set all for maximum output
# DEBUG = ('init', 'font', 'track', 'path', 'station', 'passenger', 'random' )
DEBUG = ('init','font' )


BLACK =   (  0,   0,   0)
VERYLIGHTGREY= (220, 220, 220)
LIGHTGREY= (200, 200, 200)

WHITE =   (255, 255, 255)
BLUE =    (  0,   0, 255)
GREEN =   (  0, 255,   0)
RED =     (255,   0,   0)
MAGENTA = (255,   0, 255)
CYAN =    (  0, 255, 255)
YELLOW =  (255, 255,   0)

(MAX_X,MAX_Y) = (400,400)
STATUSHEIGHT = 20 
RIGHT_OFFSET = 100
STARTPOS = (20,MAX_Y-100)
HEROSIZE = 10

STICKSPEED = 3

FPS = 30

FONTSIZE = 18 # size of the default font used

MIN_GAP = 10   # minimal gap between towers and between towers and border
MIN_WIDTH = 10 # minimal width of tower
MAX_WIDTH = 50 # maximal width of tower
PERFECT = 5    # range of perfect match
