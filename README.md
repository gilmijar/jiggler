Here’s a **shorter, cleaner README**, with the warnings moved up and **clear emphasis on compatible microcontrollers**:

---

# USB HID Jiggler (CircuitPython)

A minimal **CircuitPython USB HID jiggler** that periodically sends **mouse movement or keyboard input** to keep a host computer from going idle. The onboard LED blinks on each action.

## ⚠️ Warnings (Read First)

* This device **actively sends USB input events** (mouse/keyboard).
* Use **only on systems you own or control**.
* `boot.py` includes commented code to disable the USB storage drive. 
The idea is to be able to plug the board into a usb port and have it do its thing, 
and unplug without a hassle. Unplugging while storage is mounted can cause problems, 
so you may want to disable the storage mode and keep only the HID functionality. 
Enabling it can make the device difficult to recover without reflashing.

## Compatible Microcontrollers

**Must support BOTH USB device mode and USB HID in CircuitPython**, for example:

* **Raspberry Pi Pico / Pico W**
* **Adafruit QT Py (RP2040)**
* **Adafruit Feather RP2040**
* **Seeeduino XIAO RP2040**
* **Any RP2040 board with native USB + HID support**

❌ Boards *without native USB HID support will not work*.

## Files

* `code.py` – Main logic (mouse or keyboard behavior)
* `boot.py` – Optional USB storage configuration (safe by default)

## Configuration

In `code.py`:

```python
mode = 0  # 0 = mouse, 1 = keyboard
SLEEP_TIME = 2
jump_size = 5
```

* **Mouse mode**: moves cursor left/right
* **Keyboard mode**: sends Up / Down arrow keys alternately

## Usage

1. Install CircuitPython on a supported board
2. Copy `code.py` (and optionally `boot.py`) to the device
3. Plug it into a computer — it runs automatically

---

If you want, I can compress this into a **~10-line ultra-minimal README**, or tailor it to a specific board model.
