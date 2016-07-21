from microbit import sleep, display, accelerometer

class Droplet:
    def __init__(self, x, y):
        # Create the drop with history the same as the start
        self.x = [x, x, x]
        self.y = [y, y, y]

    def update(self):
        # Move the droplet around the board based on the accelerometer
        x_reading = accelerometer.get_x()
        if x_reading > 20:
            delta_x = 1
        elif x_reading < -20:
            delta_x = -1
        else:
            delta_x = 0

        y_reading = accelerometer.get_y()
        if y_reading > 20:
            delta_y = 1
        elif y_reading < -20:
            delta_y = -1
        else:
            delta_y = 0

        # Move the tail along
        self.x[2] = self.x[1]
        self.x[1] = self.x[0]
        self.y[2] = self.y[1]
        self.y[1] = self.y[0]

        # Update x and y and check for boundaries
        self.x[0] = self.x[0] + delta_x
        if (self.x[0] > 4):
            self.x[0] = 4
        elif (self.x[0] < 0):
            self.x[0] = 0

        self.y[0] = self.y[0] + delta_y
        if (self.y[0] > 4):
            self.y[0] = 4
        elif (self.y[0] < 0):
            self.y[0] = 0

    def draw(self):
        # Draw the droplet (with fainter tail)
        display.set_pixel(self.x[2], self.y[2], 0)
        display.set_pixel(self.x[1], self.y[1], 1)
        display.set_pixel(self.x[0], self.y[0], 9)

d = Droplet(0, 2)

while True:
    d.update()
    d.draw()
    sleep(1000)

