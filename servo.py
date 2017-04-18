#!/usr/bin/python3
import time
import sys
import keyboard
from enum import Enum

servo_x_position = 50
position_x_changed = False
servo_y_position = 50
position_y_changed = False

speed = 3

def move_servo_up():
    global speed
    global position_y_changed
    global servo_y_position
    global wait_next_cycle
    servo_y_position += speed
    print("up:y="+str(servo_y_position))
    position_y_changed = True
    return

def move_servo_down():
    global speed
    global position_y_changed
    global servo_y_position
    global wait_next_cycle
    servo_y_position -= speed
    print("down:y="+str(servo_y_position))
    position_y_changed = True
    return

def move_servo_left():
    global speed
    global position_x_changed
    global servo_x_position
    servo_x_position += speed
    position_x_changed = True
    print("left:x="+str(servo_x_position))
    return

def move_servo_right():
    global speed
    global position_x_changed
    global servo_x_position
    servo_x_position -= speed
    position_x_changed = True
    print("right:x="+str(servo_x_position))
    return

def callback(kb_event):
    switcher = {
            'up': move_servo_up,
            'left': move_servo_left,
            'right': move_servo_right,
            'down': move_servo_down,
            }
    func = switcher.get(kb_event.name)
    return func()


def refresh_servos():
    global position_x_changed
    global position_y_changed
    global servo_x_position
    global servo_y_position
    sb = open('/dev/servoblaster', 'w')
    if position_x_changed:
        print("P1-12="+str(servo_x_position), file=sb)
        position_x_changed = False
    if position_y_changed:
        print("P1-18="+str(servo_y_position), file=sb)
        position_y_changed = False
    return


kh = keyboard.hook(callback)

def main(argv=None):
    while True:
        time.sleep(0.05) # 50 ms
        refresh_servos()

if __name__ == "__main__":
    sys.exit(main())
