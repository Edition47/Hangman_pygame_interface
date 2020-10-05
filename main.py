import sys
import pygame
import math
import random
import functions as func
import pygame_textinput as pytin

# User text input
textinput = pytin.TextInput(font_family="comicsans", font_size=50)
# load images
images = []
for i in range(7):
    image = pygame.image.load("img/hangman" + str(i) + ".png")
    images.append(image)

# setup display
WIDTH, HEIGHT = 1000, 800
WHITE = 255, 255, 255
BLACK = 0, 0, 0
TITLE_FONT = pygame.font.SysFont('comicsans', 70)
FPS = 60
clock = pygame.time.Clock()

# setup buttons
RADIUS = 25
GAP = 20
letters = []
startx = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2)
starty = 650
A = 65
for i in range(26):
    x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
    y = starty + ((i // 13) * (GAP + RADIUS * 2))
    letters.append([x, y, chr(A + i), True])

# ----------------------------------The Game's Body-----------------------------
Phase = 0
# game variables
hangman_state = 0
words = ["IDE", "PYTHON", "PYGAME",]
word = random.choice(words)
guessed = [" "]
pygame.init()
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman Game!")
while True:
    clock.tick(FPS)
    events = pygame.event.get()
    if Phase is 0:
        func.draw_menu(win, HEIGHT, images)
    if Phase is 1:
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit()
        win.fill(WHITE)
        text = TITLE_FONT.render("INPUT THE WORD", 1, BLACK)
        win.blit(text, [WIDTH / 2 - text.get_width() / 2, 25])
        win.blit(textinput.get_surface(), [WIDTH / 2-150,150])
        if textinput.update(events):
            word = textinput.get_text()
            word = word.strip()
            word = word.upper()
            Phase = 2

    if Phase is 2:
        func.draw_game(win, letters, word, guessed, images, hangman_state)
    for event in events:
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            m_x, m_y = pygame.mouse.get_pos()
            if Phase is 0:
                if 300 < m_x < 700:
                    if 460 < m_y < 500:
                        Phase = 1
                    if 390 < m_y < 430:
                        Phase = 2
                    if 530 < m_y < 575:
                        sys.exit()
            if Phase is 2:
                for letter in letters:
                    x, y, ltr, visible = letter
                    if visible:
                        dis = math.sqrt((x - m_x) ** 2 + (y - m_y) ** 2)
                        if dis < RADIUS:
                            letter[3] = False
                            guessed.append(ltr)
                            if ltr not in word:
                                hangman_state += 1
    for letter in word:
        if letter not in guessed:
            won = False
            break

        else:
            won = True

    if won:
        func.won_lost("You WON!", win, word)
        pygame.display.update()
        pygame.time.delay(2000)
        break

    if hangman_state == 6:
        func.won_lost("You LOST!", win, word)
        pygame.display.update()
        pygame.time.delay(2000)
        break
    pygame.display.update()
