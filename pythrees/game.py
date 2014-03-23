#!/usr/bin/python
# -*- coding: utf-8 *-*

import pygame
from pygame.locals import QUIT, KEYDOWN, K_UP, K_LEFT, K_RIGHT, K_DOWN
import pythrees
import sys

class TileSet (object):
    def __init__ (self, gameconfig):
        self.size = gameconfig['tilesize']
        self.rows = gameconfig['rows']
        self.cols = gameconfig['columns']
        self.new_values = gameconfig['posiblevalues']
        self.values = pythrees.ini_tiles(self.rows, self.cols)
        self.positions, self.labels_pos, w, h = self.calcpositions(gameconfig)
        self.base_colors = gameconfig['tilecolors']
        self.border = gameconfig['tileborder']
        self.bordercolor = gameconfig['tilebordercolor']
        self.hframes = w / gameconfig['framesanimation']
        self.vframes = h / gameconfig['framesanimation']
                
    def tilecolor (self, val):
        try:
            return self.base_colors[val]
        except:
            prev_color = self.base_colors[val-1]
            new_color = [c-10 for c in prev_color]
            self.base_colors.append(new_color)
            return new_color
        
    def calcpositions(self, gameconfig):
        margin = gameconfig['tilemargin'] 
        width = (self.size * self.cols) + (margin * (self.cols + 1))
        height = (self.size * self.rows) + (margin * (self.rows + 1))
        iwidth = (gameconfig['width'] - width) / 2
        iheight = (gameconfig['height'] - height) / 2
        lblx, lbly = gameconfig['labelposition']
        positions = []
        labels = []
        for i in xrange(self.cols*self.rows):
            row, col = self.val_position(i)
            x = (iwidth + margin) + (col * self.size) + (col * margin)
            y = (iheight + margin) + (row * self.size) + (row * margin)
            positions.append((x, y))
            labels.append((x + (self.size/2) + lblx, y + (self.size/2) + lbly))
        return positions, labels, width, height
    
    def val_position (self, idx):
        row = idx / self.cols
        col = idx % self.rows
        return row, col
    
    def new_value (self):
        pythrees.set_new_value(self.values, self.new_values)
    
class Labels (object):
    def __init__(self, name, color, size):
        self.font = pygame.font.SysFont(name, size)
        self.color = color
        self.labels = {
                       0: self.font.render('', 0, self.color)
                       }
        
    def get_label(self, value):
        try:
            lbl = self.labels[value]
        except:
            lbl = self.font.render(str(value), 1, self.color)
            self.labels[value] = lbl
        return lbl
    
class AnimationEngine (object):
    def __init__(self):
        pass

def keypress (key, tiles):
    if (key == K_UP):
        tiles.values = pythrees.move_tiles(tiles.values, pythrees.UP_MOVEMENT)
    elif (key == K_RIGHT):
        tiles.values = pythrees.move_tiles(tiles.values, pythrees.RIGHT_MOVEMENT)
    elif (key == K_DOWN):
        tiles.values = pythrees.move_tiles(tiles.values, pythrees.DOWN_MOVEMENT)
    elif (key == K_LEFT):
        tiles.values = pythrees.move_tiles(tiles.values, pythrees.LEFT_MOVEMENT)
    else:
        return
    tiles.new_value()

def draw (screen, tiles, labels):
    for idx, pos in enumerate(tiles.positions):
        r, c = tiles.val_position(idx) 
        value = tiles.values[r][c]
        tile = pygame.Rect(pos[0], pos[1], tiles.size, tiles.size)
        border = pygame.Rect(pos[0] - tiles.border, pos[1]-tiles.border, 
                             tiles.size + (tiles.border*2),
                             tiles.size + (tiles.border*2))
        pygame.draw.rect(screen, tiles.bordercolor, border)
        pygame.draw.rect(screen, tiles.tilecolor(value), tile)
        pos = tiles.labels_pos[idx]
        screen.blit(labels.get_label(value), pos)
    
def update (events, tiles):
    for event in events:
        if event.type == QUIT:
            pygame.display.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            keypress(event.key, tiles)

def play (gameconfig=None):
    if gameconfig is None:
        from gameconfig import basic_config
        gameconfig = basic_config

    size = (gameconfig['width'],gameconfig['height'])
    screen = pygame.display.set_mode(size)
    tiles = TileSet(gameconfig)
    bgcolor = gameconfig['background']
    pygame.font.init()
    labels = Labels(gameconfig['labelname'], gameconfig['labelcolor'], 
                    gameconfig['labelsize'])
    
    tiles.new_value()
     
    while True:
        update(pygame.event.get(), tiles)
        screen.fill(bgcolor)
        draw (screen, tiles, labels)
        pygame.display.flip()
        #pygame.display.update()
        
if __name__ == '__main__':
    play()