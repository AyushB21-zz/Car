def getSensorEquations(self, world):       #restituisce le equazioni delle rette (in variabile y) della macchina in ordine [verticale, diagonale crescente, orizzontale, diagonale decrescente]
    eq = []
    for i in range(4):
        omega = radians(self.rot + 45*i)
        dx = SENSOR_DISTANCE * sin(omega)
        dy = - SENSOR_DISTANCE * cos(omega)

        if CAR_DBG:             #disegna linee dei sensori
            py.draw.lines(world.win, GREEN, False, [world.getScreenCoords(self.x+dx, self.y+dy), world.getScreenCoords(self.x-dx, self.y-dy)], 2)

        coef = getSegmentEquation(self, vect2d(x = self.x+dx, y = self.y+dy))
        eq.append(coef)
    return eq
