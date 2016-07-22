from microbit import *
import music

# Plays the close encounters theme along with flashing lights
# Add a small piezo speaker between Pin 0 and  GND

tune_slow = ['D4:4', 'E', 'C', 'C3', 'E3:6']
tune_fast = ['D4:2', 'E', 'C', 'C3', 'E3:3']
lights = [(0,1), (1,0), (2,2), (3,4), (4,3)]

while True:
    for light, note in enumerate(tune_slow):
        x, y = lights[light]
        display.set_pixel(x, y, 9)
        music.play([note])
        display.set_pixel(x, y, 2)
    
    for light, note in enumerate(tune_fast):
        x, y = lights[light]
        display.set_pixel(x, y, 9)
        music.play([note])
        display.set_pixel(x, y, 2)
