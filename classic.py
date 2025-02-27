import pygame

pygame.init() #запомнить
window_size=(300, 300)#размеры окна
screen=pygame.display.set_mode(window_size)#создаем экран с размерами
pygame.display.set_caption("Моя игра")#название игры
background_color = (16, 205, 200)#cоздаем цвет фона
screen.fill(background_color)
clock = pygame.time.Clock()
r = pygame.Rect(100, 100 , 100 , 70)
font = pygame.font.SysFont('Arial', 10)
text = font.render('Ваня', True, 0)
screen.blit(text, (100, 70))
while True:
    pygame.draw.rect(screen, 324, r)
    clock.tick(46)# считаем фпс
    pygame.display.update() # обнова экрана
    for event in pygame.event.get(): # ходим по событиям
        if event.type == pygame.QUIT: # нажали на крестик
            pygame.QUIT() # вышли из игры














