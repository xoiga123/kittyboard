import keyboard
import ctypes

print("Press your hotkey: ")
hotkey = keyboard.read_hotkey()
keyboard.stash_state()
print("Hotkey registered: " + hotkey)
while True:
    keyboard.wait(hotkey)
    ctypes.windll.user32.BlockInput(True)
    keyboard.wait(hotkey)
    ctypes.windll.user32.BlockInput(False)