def getInputs(self, world, road):         #win serve per disegnare i sensori se DBG = True
        sensors = []
        for k in range(8):
            sensors.append(SENSOR_DISTANCE)
        sensorsEquations = getSensorEquations(self, world)

        for v in [road.pointsLeft, road.pointsRight]:
            i = road.bottomPointIndex
            while v[i].y > self.y - SENSOR_DISTANCE:
                next_index = getPoint(i+1, NUM_POINTS*road.num_ctrl_points)

                getDistance(world, self, sensors, sensorsEquations, v[i], v[next_index])
                i = next_index

        if CAR_DBG:
            for k,s in enumerate(sensors):
                omega = radians(self.rot + 45*k)
                dx = s * sin(omega)
                dy = - s * cos(omega)
                #disegna intersezioni dei sensori
                if s < SENSOR_DISTANCE:
                    py.draw.circle(world.win, RED, world.getScreenCoords(self.x+dx, self.y+dy), 6)

        #convert to value between 0 (distance = max) and 1 (distance = 0)
        for s in range(len(sensors)):
            sensors[s] = 1 - sensors[s]/SENSOR_DISTANCE

        return sensors
