import pygame

pygame.init()

SCREEN_WIDTH = 720
SCREEN_HEIGHT = 720

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()

letters = []
max_length = 5

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        
        if event.type == pygame.KEYDOWN:
            if len(letters) > 0 and event.key == pygame.K_BACKSPACE:
                letters.pop(len(letters)-1)
            elif event.unicode.isalpha() and len(letters) < max_length:
                letters.append(event.unicode.upper())
            print(letters)
        
    screen.fill("pink")

    rect_width = SCREEN_WIDTH / 6
    rect_height = SCREEN_WIDTH / 6
    spacing = (SCREEN_WIDTH - rect_width * 5) // 6

    for x in range(5):
        for y in range(5):
            pygame.draw.rect(
                screen,
                "lightgrey",
                pygame.Rect(
                    spacing + x * (rect_width + spacing),
                    spacing + y * (rect_height + spacing),
                    rect_width,
                    rect_height
                ),
                0,
                5
            )

    pygame.display.flip()
    clock.tick(60)