import time
import board
import digitalio
import usb_hid
from adafruit_hid.mouse import Mouse
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

# Set up a keyboard device.
kbd = Keyboard(usb_hid.devices)

# Setup mouse
mouse = Mouse(usb_hid.devices)

# Setup onboard LED (GPIO 25)
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

DELAY = 0.1  # time to turn on LED (in seconds)
SLEEP_TIME = 2  # seconds between movements
jump_size = 5  # how many pixeld to move left or right
codes = (Keycode.UP_ARROW, Keycode.DOWN_ARROW)  # which keys to send
code_index = 0

mode = 0  # mode 0 for mouse, mode 1 for key presses

while True:
    # Move left
    led.value = True
    if mode:
        kbd.send(codes[code_index])
        code_index = (code_index + 1) % len(codes)
    else:
        jump_size *= -1
        mouse.move(x=jump_size, y=0)
    time.sleep(DELAY)
    led.value = False
    time.sleep(SLEEP_TIME)

