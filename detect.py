def detectCollision(self, road):
        #get mask
        mask = py.mask.from_surface(self.img)
        (width, height) = mask.get_size()
        for v in [road.pointsLeft, road.pointsRight]:
            for p in v:
                x = p.x - self.x + width/2
                y = p.y - self.y + height/2
                try:
                    if mask.get_at((int(x),int(y))):
                        return True
                except IndexError as error:
                    continue
        return False
