from microbit import display, sleep
from random import randint

# Simple parallax demo
#
# Stars in foreground
# - are brighter
# - move faster than those in the background

class Star():
    """ Simple star """
    def __init__(self):
        # Start in the middle at the bottom
        self.reset()
        self.x = randint(0, 4)

    def reset(self):
        self.x = 4
        self.y = randint(0, 4)
        self.bright = randint(0, 9)

    def update(self):
        display.set_pixel(self.x, self.y, 0)
        self.x = self.x - 1
        if self.x < 0:
            self.reset()
        display.set_pixel(self.x, self.y, self.bright)

stars = []
for _ in range(3):
    s = Star()
    stars.append(s)
while True:
    for s in stars:
        s.update()
    sleep(500)
