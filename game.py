import pygame

# Khởi tạo pygame
pygame.init()

# Tạo cửa sổ game
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Simple Game")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))  # Đặt màu nền đen
    pygame.display.update()

pygame.quit()
