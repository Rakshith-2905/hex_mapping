from __future__ import division
import pygame
from pygame.locals import *
import math
import numpy as np


purple = (155,0,155)
green = (90,230,40)

n_of_rings = 50
hexagons = {}
l = 1

def draw_hexagon(ring, window):
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

def update_hexagons(cart_cords, hex_codrs, prev_hex, prev_cart):
    new_nodes_cat, new_nodes_hex = [], []
    for i in range(len(cart_cords)):
        if hex_codrs[i] in hexagons:
            continue 
        new_nodes_cat.append(cart_cords[i])
        hexagons[hex_codrs[i]] =  {'fly':False, 'cart':(cart_cords[i]),'ring':0}
        new_nodes_hex.append(hex_codrs[i])
    return new_nodes_hex, new_nodes_cat

def compute_cart_neighbors(center_of_ring_cart):
    N = [center_of_ring_cart[0],center_of_ring_cart[1]-(math.sqrt(3))*l]
    S = [center_of_ring_cart[0],center_of_ring_cart[1]+(math.sqrt(3))*l]
    NW = [center_of_ring_cart[0]-3*l/2,center_of_ring_cart[1]-((math.sqrt(3))/2)*l]
    SW = [center_of_ring_cart[0]-3*l/2,center_of_ring_cart[1]+((math.sqrt(3))/2)*l]
    NE = [center_of_ring_cart[0]+3*l/2,center_of_ring_cart[1]-((math.sqrt(3))/2)*l]
    SE = [center_of_ring_cart[0]+3*l/2,center_of_ring_cart[1]+((math.sqrt(3))/2)*l]

    return [N,S,NW,SW,NE,SE]

def compute_hex_neighbors(center_of_ring_hex):
    Qc,Rc = center_of_ring_hex[0], center_of_ring_hex[1]
    N = (Qc,Rc-1)
    S = (Qc,Rc+1)
    NW = (Qc-1,Rc)
    SW = (Qc-1,Rc+1)
    NE = (Qc+1,Rc-1)
    SE = (Qc+1,Rc)

    return [N,S,NW,SW,NE,SE]

def compute_neighbors(center_of_ring_cart, center_of_ring_hex, prev_hex, prev_cart, window):
    ring_hex = compute_hex_neighbors(center_of_ring_hex)
    ring_cart = compute_cart_neighbors(center_of_ring_cart)
    draw_hexagon(ring_cart, window)
    updated_hex, updated_cart = update_hexagons(ring_cart, ring_hex, prev_hex, prev_cart)
    return updated_hex, updated_cart 

def draw_hexagon_map(n, window_size, window):
    center_of_map = (window_size[0]/2,window_size[1]/2)
    latest_nodes_cat = []
    latest_nodes_hex = []
    hexagons[(0,0)] = {'fly':False,'cart':center_of_map,'ring':0}
    latest_nodes_cat.append(center_of_map)
    latest_nodes_hex.append((0,0))
    for i in range(n):
        next_hex, next_cart = [], []
        c = 0
        while c < len(latest_nodes_cat):
            temp_hex, temp_cart = compute_neighbors(latest_nodes_cat[c], latest_nodes_hex[c], latest_nodes_hex, latest_nodes_cat, window)
            next_hex.extend(temp_hex)
            next_cart.extend(temp_cart)
            c += 1
        latest_nodes_cat = next_cart
        latest_nodes_hex = next_hex
        pygame.display.update()


if __name__ == '__main__':
    n_of_rings = input("Enter the number of rings: ")
    pygame.init()
    window_size = (1040,1000)
    window = pygame.display.set_mode(window_size)
    draw_hexagon_map(int(n_of_rings), window_size, window)
    while True:
        pygame.display.update()
