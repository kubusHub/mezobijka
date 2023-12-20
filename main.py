import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 768), (pygame.SCALED))
pygame.display.set_caption("Hello World")
keyPress = {'quit': 'K_q', 'moveLeft': 'K_a', 'moveRight': 'K_d'}
carImg=pygame.image.load('car.png')
mousePos=[]
carPos=632
def drawLine():
   pygame.draw.circle(screen, (255,0,0), pygame.mouse.get_pos(), 5)
   if len(mousePos)>1:
      pygame.draw.line(screen, (255, 255, 255), mousePos[0],  mousePos[1], 5)
      mousePos.clear()
def moveCar():
   print(keyPress['moveLeft'])
   print(key.)
   if event.key==pygame.key.key_code(keyPress['moveLeft']):
      carPos-=10
      screen.blit(carPos, carImg)
   if event.key==pygame.key.key_code(keyPress['moveRight']):
      carPos+=10
      screen.blit(carPos, carImg)
while True:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         pygame.quit()
      if event.type == pygame.KEYDOWN:
         # if pygame.key.key_code(keyPress['quit']):
         #    pygame.quit()
         moveCar()
      if event.type == pygame.KEYUP:
         key = pygame.key.name(event.key)
         print(key, "Key is released")
      # if event.type == pygame.MOUSEBUTTONDOWN:
         # mousePos.append(pygame.mouse.get_pos())
         # drawLine()

   pygame.display.update()