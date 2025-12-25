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

DELAY = 0.1  # seconds between movements
SLEEP_TIME = 2
jump_size = 2

while True:
    # Move left
    led.value = True
    jump_size *= -1
    mouse.move(x=jump_size, y=0)
    time.sleep(DELAY)
    led.value = False
    time.sleep(SLEEP_TIME)
