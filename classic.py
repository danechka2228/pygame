import pygame

pygame.init() #запомнить
x = 100
y = 100
weight = 100
height = 70
window_size=(300, 300)#размеры окна
screen=pygame.display.set_mode(window_size)#создаем экран с размерами
pygame.display.set_caption("Моя игра")#название игры
background_color = (16, 205, 200)#cоздаем цвет фона
clock = pygame.time.Clock()
font = pygame.font.SysFont('Arial', 10)
text = font.render('somebody cover my!!!', True, 371)

while True:
    screen.fill(background_color)
    r = pygame.Rect(x, y, weight, height)
    pygame.draw.rect(screen, 123456789, r)
    screen.blit(text, (110, 125))
    clock.tick(10)# считаем фпс
    pygame.display.update() # обнова экрана
    for event in pygame.event.get(): # ходим по событиям
        if event.type == pygame.KEYDOWN: # если клавиша нажата
            if event.key == pygame.K_a: # если клавиша а
                x = x-5
            if event.key == pygame.K_w: # если клавиша а
                y = y-5
            if event.key == pygame.K_s:  # если клавиша а
                y = y + 5
            if event.key == pygame.K_d:  # если клавиша а
                x = x + 5
        if event.type == pygame.QUIT: # нажали на крестик
            pygame.QUIT() # вышли из игры

