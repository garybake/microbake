from microbit import display, sleep

def initialise():
    for y in [0,2,4]:
        display.set_pixel(0, y, 4)
        display.set_pixel(4, y, 4)
    for y in [1,3]:
        display.set_pixel(0, y, 1)
        display.set_pixel(4, y, 1)

def swap_led(x, y):
    if display.get_pixel(x, y) == 1:
        display.set_pixel(x, y, 4)
    else:
        display.set_pixel(x, y, 1)

def update_barrier():
    for y in range(5):
        swap_led(0, y)
        swap_led(4, y)

def update():
    update_barrier()

initialise()
while True:
    update()
    sleep(100)