import pygame
import requests

pygame.init()

lat, lon, scale_x, scale_y = 37.5555, 55.555, 1 / 500, 1 / 500

user_scale_x, user_scale_y = 1, 1


class Button(pygame.sprite.Sprite):
    def __init__(self, image, scale_1, scale_2, x, y):
        super().__init__()
        self.image = pygame.transform.scale(image, (scale_1, scale_2))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


def search():
    global lat, lon, scale_x, scale_y
    url = f'https://static-maps.yandex.ru/1.x/?ll={lat},{lon}&spn={scale_x},{scale_y}&l=map'
    response = requests.get(url)
    with open('map.png', 'wb') as file:
        file.write(response.content)

    size = (700, 450)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('YandexMaps Finder')

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
    global lon, lat, scale_x, scale_y, user_scale_x, user_scale_y

    lon, lat, user_scale_x, user_scale_y = str(lon), str(lat), str(user_scale_x), str(user_scale_y)

    size = (800, 500)
    screen = pygame.display.set_mode(size)

    font = pygame.font.Font(None, 32)
    pygame.display.set_caption('YandexMaps Finder')
    clock = pygame.time.Clock()

    # Можно было создать класс InputBox. Но с этим возникли трудности...
    input_box1 = pygame.Rect(30, 30, 132, 60)
    input_box2 = pygame.Rect(230, 30, 132, 60)
    input_box3 = pygame.Rect(430, 30, 132, 60)
    input_box4 = pygame.Rect(630, 30, 132, 60)

    color_inactive = (0, 0, 0)
    color_active = (255, 115, 0)

    color1 = color_inactive
    color2 = color_inactive
    color3 = color_inactive
    color4 = color_inactive

    active1 = False
    active2 = False
    active3 = False
    active4 = False

    text1 = lon
    text2 = lat
    text3 = user_scale_x
    text4 = user_scale_y

    lon_lbl = font.render('Lon (X)', True, (255, 255, 255))
    lat_lbl = font.render('Lat (Y)', True, (255, 255, 255))
    size_x_lbl = font.render('Size X', True, (255, 255, 255))
    size_y_lbl = font.render('Size Y', True, (255, 255, 255))

    allowed_symbols = [
        '1',
        '2',
        '3',
        '4',
        '5',
        '6',
        '7',
        '8',
        '9',
        '0',
        '.'
    ]

    background_img = pygame.transform.scale(pygame.image.load('data/settings_bg.png'), size)

    back_button = Button(pygame.image.load('data/back_btn.png'), 50, 50, 725, 415)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if back_button.rect.collidepoint(event.pos):
                        running = False
                        lon, lat = float(text1), float(text2)
                        if '.' not in text3:
                            user_scale_x = int(text3)
                            scale_x = float(text3) / 500
                        else:
                            user_scale_x = float(text3)
                            scale_x = float(text3)
                        if '.' not in text4:
                            user_scale_y = int(text4)
                            scale_y = float(text4) / 500
                        else:
                            user_scale_y = float(text4)
                            scale_y = float(text4)

                        main()

                    if input_box1.collidepoint(event.pos):
                        active1 = not active1
                    else:
                        active1 = False

                    if input_box2.collidepoint(event.pos):
                        active2 = not active2
                    else:
                        active2 = False

                    if input_box3.collidepoint(event.pos):
                        active3 = not active3
                    else:
                        active3 = False

                    if input_box4.collidepoint(event.pos):
                        active4 = not active4
                    else:
                        active4 = False

                    if active1:
                        color1 = color_active
                    else:
                        color1 = color_inactive

                    if active2:
                        color2 = color_active
                    else:
                        color2 = color_inactive

                    if active3:
                        color3 = color_active
                    else:
                        color3 = color_inactive

                    if active4:
                        color4 = color_active
                    else:
                        color4 = color_inactive

            if event.type == pygame.KEYDOWN:
                if active1:
                    if event.key == pygame.K_BACKSPACE:
                        text1 = text1[:-1]
                    else:
                        if event.unicode in allowed_symbols:
                            text1 += event.unicode

                elif active2:
                    if event.key == pygame.K_BACKSPACE:
                        text2 = text2[:-1]
                    else:
                        if event.unicode in allowed_symbols:
                            text2 += event.unicode

                elif active3:
                    if event.key == pygame.K_BACKSPACE:
                        text3 = text3[:-1]
                    else:
                        if event.unicode in allowed_symbols:
                            text3 += event.unicode

                elif active4:
                    if event.key == pygame.K_BACKSPACE:
                        text4 = text4[:-1]
                    else:
                        if event.unicode in allowed_symbols:
                            text4 += event.unicode

        screen.fill((0, 0, 0))

        screen.blit(background_img, (0, 0))

        txt_surface1 = font.render(str(text1), True, (255, 255, 255))
        txt_surface2 = font.render(str(text2), True, (255, 255, 255))
        txt_surface3 = font.render(str(text3), True, (255, 255, 255))
        txt_surface4 = font.render(str(text4), True, (255, 255, 255))

        width1 = max(60, txt_surface1.get_width() + 10)
        width2 = max(60, txt_surface2.get_width() + 10)
        width3 = max(60, txt_surface3.get_width() + 10)
        width4 = max(60, txt_surface4.get_width() + 10)

        input_box1.w = width1
        input_box2.w = width2
        input_box3.w = width3
        input_box4.w = width4

        screen.blit(txt_surface1, (input_box1.x + 5, input_box1.y + 20))
        screen.blit(txt_surface2, (input_box2.x + 5, input_box2.y + 20))
        screen.blit(txt_surface3, (input_box3.x + 5, input_box3.y + 20))
        screen.blit(txt_surface4, (input_box4.x + 5, input_box4.y + 20))

        screen.blit(lon_lbl, (input_box1.x, input_box1.y + 65))
        screen.blit(lat_lbl, (input_box2.x, input_box2.y + 65))
        screen.blit(size_x_lbl, (input_box3.x, input_box3.y + 65))
        screen.blit(size_y_lbl, (input_box4.x, input_box4.y + 65))

        screen.blit(back_button.image, (back_button.rect.x, back_button.rect.y))

        pygame.draw.rect(screen, color1, input_box1, 2)
        pygame.draw.rect(screen, color2, input_box2, 2)
        pygame.draw.rect(screen, color3, input_box3, 2)
        pygame.draw.rect(screen, color4, input_box4, 2)

        pygame.display.flip()
        clock.tick(60)


def main():
    size = (800, 500)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('YandexMaps Finder')
    search_btn = Button(pygame.image.load('data/search_btn.png'), 50, 50, 700, 50)
    settings_btn = Button(pygame.image.load('data/settings_btn.png'), 50, 50, 50, 50)

    background_img = pygame.transform.scale(pygame.image.load('data/yandex_bg.webp'), size)

    exit_button = Button(pygame.image.load('data/exit_btn.png'), 50, 50, 725, 415)

    running = True
    while running:
        screen.fill((255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if search_btn.rect.collidepoint(event.pos):
                        running = False
                        search()
                    elif settings_btn.rect.collidepoint(event.pos):
                        running = False
                        settings()
                    elif exit_button.rect.collidepoint(event.pos):
                        running = False
        screen.blit(background_img, (0, 0))
        screen.blit(search_btn.image, (search_btn.rect.x, search_btn.rect.y))
        screen.blit(settings_btn.image, (settings_btn.rect.x, settings_btn.rect.y))
        screen.blit(exit_button.image, (exit_button.rect.x, exit_button.rect.y))
        pygame.display.flip()


main()
pygame.quit()
