from config_variables import *
import pygame as py
import numpy as np
from scipy import interpolate
from math import *
from vect2d import *
from random import random, seed

class Road:
    def __init__(self, world):
        self.num_ctrl_points = (int)((world.win_height+SAFE_SPACE)/SPACING)+2

        self.last_ctrl_point = 0
        self.ctrl_points = []
        self.centerPoints = []
        self.pointsLeft = []
        self.pointsRight = []

        for i in range(self.num_ctrl_points):
             self.ctrl_points.append(vect2d())

        for i in range(NUM_POINTS*self.num_ctrl_points):        #riempi i vettori pointsLeft e pointsRight
            self.pointsLeft.append(vect2d(1000,1000))
            self.pointsRight.append(vect2d(1000,1000))
            self.centerPoints.append(vect2d(1000,1000))

        self.ctrl_points[0].co(0, SPACING)              #inizializza i primi due control_point in modo che siano dritti
        self.ctrl_points[1].co(0, 0)
        for i in range(NUM_POINTS):
            x = self.ctrl_points[0].x
            y = self.ctrl_points[0].y - SPACING/NUM_POINTS*i
            self.centerPoints[i].co(x, y)
            self.pointsLeft[i].co(x - ROAD_WIDTH/2, y)
            self.pointsRight[i].co(x + ROAD_WIDTH/2, y)
        self.next_point = NUM_POINTS

        for i in range(self.num_ctrl_points-2):
            self.createSegment(i+1)

        self.last_ctrl_point = self.num_ctrl_points-1
        self.bottomPointIndex = 0
