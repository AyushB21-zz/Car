def update(self, world):
        if world.getScreenCoords(0, self.ctrl_points[self.last_ctrl_point].y)[1] > -SAFE_SPACE:
            self.createSegment(self.last_ctrl_point)


    def draw(self, world):
        #draw control_points
        if(ROAD_DBG):
            #for p in self.ctrl_points:     #EEEEEEEEEEEEEEEEE
                #py.draw.circle(win, BLUE, (int(p.x), int(p.y)), 4)
            for i in range(len(self.pointsLeft)):
                py.draw.circle(world.win, BLUE, world.getScreenCoords(self.pointsLeft[i].x, self.pointsLeft[i].y), 2)
                py.draw.circle(world.win, BLUE, world.getScreenCoords(self.pointsRight[i].x, self.pointsRight[i].y), 2)
                #py.draw.lines(win, BLACK, False, [(self.pointsLeft[i].x, self.pointsLeft[i].y), (self.pointsRight[i].x, self.pointsRight[i].y)], 1)
        else:
            #draw borders
            for i in range(len(self.pointsLeft)):
                next_index = getPoint(i+1, NUM_POINTS*self.num_ctrl_points)

                p = self.pointsLeft[i]
                f = self.pointsLeft[next_index]
                if p.y >= f.y:
                    py.draw.line(world.win, BLACK, world.getScreenCoords(p.x, p.y), world.getScreenCoords(f.x, f.y), 4)

                p = self.pointsRight[i]
                f = self.pointsRight[next_index]
                if p.y >= f.y:
                    py.draw.line(world.win, BLACK, world.getScreenCoords(p.x, p.y),world.getScreenCoords(f.x, f.y), 4)


def getPoint(i, cap):
    return (i+cap)%cap
