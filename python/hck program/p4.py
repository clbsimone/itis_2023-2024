from pynput.mouse import Listener

def on_click(x, y, tasto, premuto):
    if premuto:
        print(f'click del mouse rilevato, tasto {tasto}')

with Listener(
    on_click=on_click
) as listener:
    listener.join()