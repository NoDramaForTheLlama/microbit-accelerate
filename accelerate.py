from microbit import *

image = Image("00000:"
              "00000:"
              "00900:"
              "00000:"
              "00000")

display.show(image)

while True:
    sleep(1000) # 1000 ms = 1 second

    # x and y will vary between around -1000 to 1000
    x = accelerometer.get_x()
    y = accelerometer.get_y()

    if x > 0 :
        image = image.shift_right(1)
    else:
        image = image.shift_left(1)

    if y > 0:
        image = image.shift_down(1)
    else:
        image = image.shift_up(1)

    display.show(image)
