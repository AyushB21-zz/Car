def calcBorders(self, i):
        prev_index = getPoint(i-1, self.num_ctrl_points*NUM_POINTS)
        center = self.centerPoints[i]
        prev = self.centerPoints[prev_index]
        angle = atan2(center.x-prev.x, prev.y-center.y)

        x = ROAD_WIDTH/2 * cos(angle)
        y = ROAD_WIDTH/2 * sin(angle)
        self.pointsLeft[i].x = center.x - x
        self.pointsLeft[i].y = center.y - y if not center.y - y >= self.pointsLeft[prev_index].y else self.pointsLeft[prev_index].y
        self.pointsRight[i].x = center.x + x
        self.pointsRight[i].y = center.y + y if not center.y + y >= self.pointsRight[prev_index].y else self.pointsRight[prev_index].y
