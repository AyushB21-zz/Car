def getNodeColors(self, world):

        if self.type == INPUT:
            ratio = world.bestInputs[self.index]
        elif self.type == OUTPUT:
            ratio = 1 if decodeCommand(world.bestCommands, self.index) else 0
        else:
            ratio = 0

        col = [[0,0,0], [0,0,0]]
        for i in range(3):
            col[0][i] = int(ratio * (self.color[1][i]-self.color[3][i]) + self.color[3][i])
            col[1][i] = int(ratio * (self.color[0][i]-self.color[2][i]) + self.color[2][i])
        return col
