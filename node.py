import pygame as py
from car import decodeCommand
from config_variables import *

class Node:
    def __init__(self, id, x, y, type, color, label = "", index=0):
        self.id = id
        self.x = x
        self.y = y
        self.type = type
        self.color = color
        self.label = label
        self.index = index
