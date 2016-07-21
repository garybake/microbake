from microbit import display, sleep, button_a, button_b
from random import randint

# Basic scrolling game
# Use buttons to control direction
# Avoid obstacles

# TODO
# Crashing sometimes has a lot of flashes


class Car:
    """ The players Car """
    def __init__(self):
        # Start in the middle at the bottom
        self.x = 2
        self.y = 4

    def update(self):
        # Clear old pixel
        # TODO we don't need to clear if no button is pressed
        display.set_pixel(self.x, self.y, 0)
        # Move left or right
        if button_a.is_pressed() and self.x > 1:
            self.x = self.x - 1
        if button_b.is_pressed() and self.x < 3:
            self.x = self.x + 1
        # Redraw
        display.set_pixel(self.x, self.y, 9)


class Barrier:
    """ The barrier on either side of the road """
    def __init__(self):
        self.reset()

    def reset(self):
        """ Set the lights to a series of dark/light values """
        for y in [0, 2, 4]:
            display.set_pixel(0, y, 4)
            display.set_pixel(4, y, 4)
        for y in [1, 3]:
            display.set_pixel(0, y, 1)
            display.set_pixel(4, y, 1)

    def update(self):
        """ Swap the lights to give the illusion of movement """
        for y in range(5):
            swap_led(0, y)
            swap_led(4, y)


class Enemy:
    """ The enemy car on the road """
    def __init__(self):
        """ Start the enemy on a random track at the top """
        self.x = randint(1, 3)
        self.y = 0

    def update(self):
        # Move enemy down screen
        display.set_pixel(self.x, self.y, 0)
        self.y = self.y + 1
        # Move back to top once off the bottom
        # TODO we should have a delay here
        if self.y >= 5:
            self.x = randint(1, 3)
            self.y = 0
        display.set_pixel(self.x, self.y, 9)


def check_crash(car, enemy, barrier):
    """ Check for a crash between car and enemy """
    if (car.x == enemy.x) and (car.y == enemy.y):
        # Repeat crazy flashes on crash
        for _ in range(5):
            for y in range(5):
                display.set_pixel(0, y, 9)
                display.set_pixel(4, y, 9)
            sleep(100)
            for y in range(5):
                display.set_pixel(0, y, 0)
                display.set_pixel(4, y, 0)
            sleep(100)
        barrier.reset()

def swap_led(x, y):
    """ Alternate an LED between light and dark """
    if display.get_pixel(x, y) == 1:
        display.set_pixel(x, y, 4)
    else:
        display.set_pixel(x, y, 1)

#--- Initialise
barrier = Barrier()
car = Car()
enemy = Enemy()
timer = 0

#--- Main loop
while True:
    timer += 1
    # Only update the enemy and barrier every 5 ticks
    if timer == 5:
        barrier.update()
        enemy.update()
        timer = 0
    car.update()
    check_crash(car, enemy, barrier)
    sleep(200)
