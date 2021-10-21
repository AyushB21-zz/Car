def draw_node(self, world):

        colorScheme = self.getNodeColors(world)

        py.draw.circle(world.win, colorScheme[0], (self.x,self.y), NODE_RADIUS)
        py.draw.circle(world.win, colorScheme[1], (self.x,self.y), NODE_RADIUS-2)

        #draw labels
        if self.type != MIDDLE:
            text = NODE_FONT.render(self.label, 1, BLACK)
            world.win.blit(text, (self.x + (self.type-1) * ((text.get_width() if not self.type else 0) + NODE_RADIUS + 5), self.y - text.get_height()/2))
            
