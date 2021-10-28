def createSegment(self, index):
        p1 = self.ctrl_points[getPoint(index, self.num_ctrl_points)]
        p2 = self.ctrl_points[getPoint(index+1, self.num_ctrl_points)]

        #define p2
        seed()
        p2.co(p1.x + (random()-0.5)*MAX_DEVIATION, p1.y-SPACING)
        p2.angle = MAX_ANGLE*(random()-0.5)

        y_tmp = []
        for i in range(NUM_POINTS):
            y_tmp.append(p2.y+SPACING/NUM_POINTS*i)

        #get cubic spline of the center line of the road
        ny = np.array([p2.y, p1.y]) #invertiti perchè scify vuole le x crescenti (in questo caso le y)
        nx = np.array([p2.x, p1.x])
        cs = interpolate.CubicSpline(ny, nx, axis=0, bc_type=((1,p2.angle),(1,p1.angle)))
        res = cs(y_tmp)

        #create the actual borders
        for i in range(NUM_POINTS):
            self.centerPoints[self.next_point].x = res[NUM_POINTS-i-1]
            self.centerPoints[self.next_point].y = y_tmp[NUM_POINTS-i-1]
            self.calcBorders(self.next_point)

            self.next_point = getPoint(self.next_point+1, NUM_POINTS*self.num_ctrl_points)

        self.last_ctrl_point = getPoint(self.last_ctrl_point+1, self.num_ctrl_points)
        self.bottomPointIndex = self.next_point
