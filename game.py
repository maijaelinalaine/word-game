import pygame

pygame.init()
pygame.font.init()

font1 = pygame.font.SysFont('freesanbold.ttf', 50)

SCREEN_WIDTH = 720
SCREEN_HEIGHT = 720

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()

letters = []
result = ['B', 'B', 'B', 'B', 'B']
max_length = 5

def check_for_matches(_letters):
    target_word = ['B', 'E', 'A', 'N', 'S']
    result = []
    for index, letter in enumerate(_letters):
        if letter == target_word[index]:
            result.append('G')
        elif letter in target_word:
            result.append('Y')
        else:
            result.append('B')
    return result

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        
        if event.type == pygame.KEYDOWN:
            if len(letters) > 0 and event.key == pygame.K_BACKSPACE:
                letters.pop(len(letters)-1)
            elif len(letters) == max_length and event.key == pygame.K_RETURN:
                result = check_for_matches(letters)
            elif event.unicode.isalpha() and len(letters) < max_length:
                letters.append(event.unicode.upper())
        
    screen.fill("pink")

    rect_width = SCREEN_WIDTH / 6
    rect_height = SCREEN_WIDTH / 6
    spacing = (SCREEN_WIDTH - rect_width * 5) // 6

    for x in range(5):
        for y in range(5):
            if(result[x] == 'G') and y == 0:
                color = 'green'
            elif(result[x] == 'Y') and y == 0:
                color = 'yellow'
            else:
                color = 'lightgrey'

            pygame.draw.rect(
                screen,
                color,
                pygame.Rect(
                    spacing + x * (rect_width + spacing),
                    spacing + y * (rect_height + spacing),
                    rect_width,
                    rect_height
                ),
                0,
                5
            )

    for index, letter in enumerate(letters):
        text1 = font1.render(letter, True, "black")
        textRect1 = text1.get_rect()
        textRect1.center = (spacing * 4 + index * (rect_width + spacing), (rect_height/2) + spacing )
        screen.blit(text1, textRect1)

    pygame.display.flip()
    clock.tick(60)