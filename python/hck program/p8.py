import pygame.camera

screen = pygame.display.set_mode([800, 400])
pygame.init()
pygame.camera.init()

mia_camera = pygame.camera.Camera('/dev/Video0', (640, 480))
mia_camera.start()
img = mia_camera.get_image()

screen.fill([0,0,0])
screen.blit([img, (100, 0)])

pygame.display.update()
pygame.image.save(img, 'dimailgay.png')