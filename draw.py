def draw(self, world):
        screen_position = world.getScreenCoords(self.x, self.y)
        rotated_img = py.transform.rotate(self.img, -self.rot)
        new_rect = rotated_img.get_rect(center = screen_position)
        world.win.blit(rotated_img, new_rect.topleft)

        if decodeCommand(self.commands, BRAKE):
            rotated_img = py.transform.rotate(self.brake_img, -self.rot)
            new_rect = rotated_img.get_rect(center = screen_position)
            world.win.blit(rotated_img, new_rect.topleft)
