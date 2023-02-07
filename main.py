import pygame
import requests

lat, lon, scale_1, scale_2 = 37.5555, 55.555, 0.002, 0.002


class Button(pygame.sprite.Sprite):
    def __init__(self, image, scale_x, scale_y, x, y):
        super().__init__()
        self.image = pygame.transform.scale(image, (scale_x, scale_y))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


def search():
    global lat, lon, scale_1, scale_2
    url = f'https://static-maps.yandex.ru/1.x/?ll={lat},{lon}&spn={scale_1},{scale_2}&l=map'
    response = requests.get(url)
    with open('map.png', 'wb') as file:
        file.write(response.content)

    size = (700, 450)
    screen = pygame.display.set_mode(size)

    back_button = Button(pygame.image.load('data/back_btn.png'), 50, 50, 625, 200)

    running = True

    while running:
        screen.fill((255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if back_button.rect.collidepoint(pygame.mouse.get_pos()):
                        running = False
                        main()
        screen.blit(pygame.image.load('map.png'), (0, 0))
        screen.blit(back_button.image, (back_button.rect.x, back_button.rect.y))
        pygame.display.flip()


def settings():
    global lat, lon, scale_1, scale_2
    pass


def main():
    size = (800, 500)
    screen = pygame.display.set_mode(size)

    search_btn = Button(pygame.image.load('data/search_btn.png'), 50, 50, 700, 50)
    settings_btn = Button(pygame.image.load('data/settings_btn.png'), 50, 50, 50, 50)

    background_img = pygame.transform.scale(pygame.image.load('data/yandex_bg.webp'), size)

    running = True
    while running:
        screen.fill((255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if search_btn.rect.collidepoint(pygame.mouse.get_pos()):
                        running = False
                        search()
                    elif settings_btn.rect.collidepoint(pygame.mouse.get_pos()):
                        running = False
                        settings()
        screen.blit(background_img, (0, 0))
        screen.blit(search_btn.image, (search_btn.rect.x, search_btn.rect.y))
        screen.blit(settings_btn.image, (settings_btn.rect.x, settings_btn.rect.y))
        pygame.display.flip()


main()
