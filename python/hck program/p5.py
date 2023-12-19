from pynput.mouse import Listener

def on_move(x, y):
    x = str(x)
    y = str(y)

    s_cordinate = f'mouse mosso alle coordinate: x={x}, y={y}'
    print(s_cordinate)

def on_click(x, y, tasto, premuto):
    if premuto:
        print(f'click del mouse rilevato, tasto: {tasto}')

with Listener(
    on_move=on_move,
    on_click=on_click
) as listener:
    listener.join()