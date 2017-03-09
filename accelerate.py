from microbit import *

image = Image("00000:"
              "00000:"
              "00900:"
              "00000:"
              "00000")

display.show(image)

x_pos = 2 # origin top left
y_pos = 2
refresh_rate = 400

while True:
    sleep(refresh_rate)
    
    x = accelerometer.get_x()
    y = accelerometer.get_y()
            
    if x > 150 and x_pos < 4:
        image = image.shift_right(1)
        x_pos = x_pos + 1
    elif x < -150 and x_pos > 0:
        image = image.shift_left(1)
        x_pos = x_pos - 1

    if y > 150 and y_pos < 4:
        image = image.shift_down(1)
        y_pos = y_pos + 1
    elif y < -150 and y_pos > 0:
        image = image.shift_up(1)
        y_pos = y_pos - 1
        
    biggest = max(abs(x), abs(y))            
    refresh_rate = max(600 - biggest, 100)

    display.show(image)
