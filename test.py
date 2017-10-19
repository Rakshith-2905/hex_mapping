
from __future__ import division
import pygame
from pygame.locals import *
import math
import numpy as np

pygame.init()

window_size = (640,600)
window = pygame.display.set_mode(window_size)

purple = (155,0,155)
green = (90,230,40)

n_of_rings = 3
map = {}
l = 50
latest_nodes_hex = []
latest_nodes_cat = []
new_nodes_hex = []
new_nodes_cat = []
#map = (Q,R) : {'fly':False,'cart':(window_size[0]/2,window_size[1]/2),'ring':0}
'''
 N = (Qc,Rc-1)
 S = (Qc,Rc+1)
 NW = (Qc-1,Rc)
 SW = (Qc-1,Rc+1)
 NE = (Qc+1,Rc-1)
 SE = (Qc+1,Rc)
'''

def draw_hexagon(ring):

        for xc,yc in ring:

            pt_1 = [(xc-(1/2*l)),(yc- ((math.sqrt(3))/2)*l)]
            pt_2 = [(xc+1/2*l),(yc- ((math.sqrt(3))/2)*l)]
            pt_3 = [(xc+l),(yc)]
            pt_4 = [(xc+1/2*l),(yc+ ((math.sqrt(3))/2)*l)]
            pt_5 = [(xc-1/2*l),(yc+ ((math.sqrt(3))/2)*l)]
            pt_6 = [(xc-l),(yc)]
            vertices = [pt_1,pt_2,pt_3,pt_4,pt_5,pt_6]
            pygame.draw.polygon(window, (purple),vertices)
            pygame.draw.lines(window, pygame.Color("black"), 1, vertices, 1)

def update_map(ring,parent):

    Qc,Rc = parent[0][0],parent[0][1]

    N = (Qc,Rc-1)
    S = (Qc,Rc+1)
    NW = (Qc-1,Rc)
    SW = (Qc-1,Rc+1)
    NE = (Qc+1,Rc-1)
    SE = (Qc+1,Rc)

    hex_codrs = [N,S,NW,SW,NE,SE]

    co_ordinates = (ring,hex_codrs)

    for r,cord in co_ordinates:

        if r not in map.values():
            new_nodes_cat.append(r)
            
        if cord not in map:
            map[cord] =  {'fly':False,'cart':(r),'ring':0}
            new_nodes_hex.append(cord)
    #print (len(new_nodes_hex),len(new_nodes_cat))

def Compute_neighbors(center_of_ring):

    global latest_nodes_cat
    global new_nodes_cat
    global latest_nodes_hex
    global new_nodes_hex

    N = [center_of_ring[0],center_of_ring[1]-(math.sqrt(3))*l]
    S = [center_of_ring[0],center_of_ring[1]+(math.sqrt(3))*l]
    NW = [center_of_ring[0]-3*l/2,center_of_ring[1]-((math.sqrt(3))/2)*l]
    SW = [center_of_ring[0]-3*l/2,center_of_ring[1]+((math.sqrt(3))/2)*l]
    NE = [center_of_ring[0]+3*l/2,center_of_ring[1]-((math.sqrt(3))/2)*l]
    SE = [center_of_ring[0]+3*l/2,center_of_ring[1]+((math.sqrt(3))/2)*l]

    ring = [N,S,NW,SW,NE,SE]

    draw_hexagon(ring)

    update_map(ring,latest_nodes_hex)

    latest_nodes_cat = new_nodes_cat
    #print latest_nodes_cat

    latest_nodes_hex = new_nodes_hex
    new_nodes_cat = []
    new_nodes_hex = []



""" Probablly the first function """
def draw_map(n):

    center_of_map = (window_size[0]/2,window_size[1]/2)
    print center_of_map
    map[(0,0)] = {'fly':False,'cart':center_of_map,'ring':0}
    latest_nodes_cat.append(center_of_map)
    latest_nodes_hex.append((0,0))
    for i in range(1):

        for center in (latest_nodes_cat):
            #print center
            Compute_neighbors(center)
            #new_nodes_hex = []



# #
draw_map(n_of_rings)
while True:


    pygame.display.update()
