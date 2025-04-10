class pen:
    def __init__(self, ink_colour, ink_type):
        self.ink_colour = ink_colour
        self.ink_type = ink_type

    def is_ball_pen (self):
        if self.ink_type == "ball":
            return True
        else:
            return False

reynolds = pen ("blue", "ball")
print(reynolds.is_ball_pen())

