from pathlib import Path
import pyscreenshot as ImageGrab

def ottieni_fullscreen(percorso):
    img = ImageGrab.grab()
    img.save(percorso)
    print('screen FULLSCREEN CATTURATO!')

def ottieni_screenParziale(sx, alto, dx, basso, percorso):
    img = ImageGrab.grab(bbox=(sx, alto, dx, basso))
    img.save(percorso)
    print('screen PARZIALE CATTURATO!')

percorso_file = Path('screenFullWindow.png')
percorso_file.touch()

ottieni_fullscreen(str(percorso_file.resolve()))

percorso_file = Path('screenParziale.png')
percorso_file.touch()
ottieni_screenParziale(0, 100, 500, 500, str(percorso_file.resolve()))