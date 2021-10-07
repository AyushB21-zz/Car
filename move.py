def move(self, road, t):
        self.acc = FRICTION

        if decodeCommand(self.commands, ACC):
            self.acc = ACC_STRENGHT
        if decodeCommand(self.commands, BRAKE):
            self.acc = -BRAKE_STREGHT
        if decodeCommand(self.commands, TURN_LEFT):
            self.rot -= TURN_VEL
        if decodeCommand(self.commands, TURN_RIGHT):
            self.rot += TURN_VEL

        timeBuffer = 500
        if MAX_VEL_REDUCTION == 1 or t >= timeBuffer:
            max_vel_local = MAX_VEL
        else:
            ratio = MAX_VEL_REDUCTION + (1 - MAX_VEL_REDUCTION)*(t/timeBuffer)
            max_vel_local = MAX_VEL *ratio

        self.vel += self.acc
        if self.vel > max_vel_local:
            self.vel = max_vel_local
        if self.vel < 0:
            self.vel = 0
        self.x = self.x + self.vel * sin(radians(self.rot))
        self.y = self.y - self.vel * cos(radians(self.rot)) #sottraggo perchè l'origine è in alto a sinistra

        #print("coord: ("+str(self.x)+", "+str(self.y)+")   vel: "+str(self.vel)+"   acc: "+str(self.acc) + "    rot: "+str(self.rot))

        return (self.x, self.y)
