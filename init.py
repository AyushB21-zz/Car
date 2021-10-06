from config_variables import *
import pygame as py
import os
from math import *
from random import random
from road import *
import numpy as np
from vect2d import vect2d


class Car:
    x = 0
    y = 0       #coordinate rispetto al sistema di riferimento globale, la posizione sullo schermo è relativa alla posizione della macchina migliore


    def __init__(self, x, y, turn):
        self.x = x
        self.y = y
        self.rot = turn
        self.rot = 0
        self.vel = MAX_VEL/2
        self.acc = 0
        self.initImgs()
        self.commands = [0,0,0,0]

    def initImgs(self):
        img_names = ["yellow_car.png", "red_car.png", "blu_car.png", "green_car.png"]
        name = img_names[floor(random()*len(img_names))%len(img_names)]                 #prendi a caso una di queste immagini

        self.img = py.transform.rotate(py.transform.scale(py.image.load(os.path.join("imgs", name)).convert_alpha(), (120,69)), -90)
        self.brake_img = py.transform.rotate(py.transform.scale(py.image.load(os.path.join("imgs", "brakes.png")).convert_alpha(), (120,69)), -90)
