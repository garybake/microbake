from microbit import *
import music

# Plays a different note when pressing different fruits

# Put a buzzer between pin0 and Gnd
# Attach a fruit to Pin1 and Pin2
# Have a loose wire from Gnd

# Hold the Gnd wire
# Press your other hand on the fruits to hear notes

note_low = ["C4:4"]
note_high = ["C5:4"]

while True:
    if pin1.is_touched():
        music.play(note_low)
        display.show(Image.HAPPY)
    elif pin2.is_touched():
        music.play(note_high)
        display.show(Image.SURPRISED)
    else:
        display.show(Image.SAD)