import storage

# Disable USB drive on startup
# !!! CAREFUL - this will mean you can't see the source files on your device.
# You should still be able to reach the device via serial port (e.g. Thonny or Mu Code)
# but if that also fails the only option will be the flash_nuke.uf2
# That is why this is commented here in the repo, or at least it should be
# storage.disable_usb_drive()
