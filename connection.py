class Connection:
    def __init__(self, input, output, wt):
        self.input = input
        self.output = output
        self.wt = wt

    def drawConnection(self, world):
        color = GREEN if self.wt >= 0 else RED
        width = int(abs(self.wt * CONNECTION_WIDTH))
        py.draw.line(world.win, color, (self.input.x + NODE_RADIUS, self.input.y), (self.output.x - NODE_RADIUS, self.output.y), width)
