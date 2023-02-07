import pygame


def main():
    screen = pygame.display.set_mode((640, 480))

    font = pygame.font.Font(None, 32)
    title = pygame.display.set_caption('Search')
    clock = pygame.time.Clock()
    input_box = pygame.Rect(200, 200, 140, 32)
    input_box1 = pygame.Rect(150, 150, 140, 32)
    input_box2 = pygame.Rect(100, 100, 140, 32)
    input_box3 = pygame.Rect(250, 250, 140, 32)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    active1 = False
    active2 = False
    active3 = False
    text = ''
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
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
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        print(text)
                        text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode
            if event.type == pygame.KEYDOWN:
                if active1:
                    if event.key == pygame.K_RETURN:
                        print(text)
                        text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode
            if event.type == pygame.KEYDOWN:
                if active2:
                    if event.key == pygame.K_RETURN:
                        print(text)
                        text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode
            if event.type == pygame.KEYDOWN:
                if active3:
                    if event.key == pygame.K_RETURN:
                        print(text)
                        text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode
        screen.fill((150, 150, 150))
        txt_surface = font.render(text, True, color)
        width = max(200, txt_surface.get_width() + 10)
        input_box.w = width
        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        pygame.draw.rect(screen, color, input_box, 2)

        input_box1.w = width
        screen.blit(txt_surface, (input_box1.x + 5, input_box1.y + 5))
        pygame.draw.rect(screen, color, input_box1, 2)

        input_box2.w = width
        screen.blit(txt_surface, (input_box2.x + 5, input_box2.y + 5))
        pygame.draw.rect(screen, color, input_box2, 2)

        input_box3.w = width
        screen.blit(txt_surface, (input_box3.x + 5, input_box3.y + 5))
        pygame.draw.rect(screen, color, input_box3, 2)
        pygame.display.flip()
        clock.tick(30)


if __name__ == '__main__':
    pygame.init()
    main()
    pygame.quit()
