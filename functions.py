import pygame
import sys

# constants
WIDTH, HEIGHT = 1000, 800
WHITE = 255, 255, 255
BLACK = 0, 0, 0
RADIUS = 25
# fonts
pygame.font.init()
LETTER_FONT = pygame.font.SysFont('comicsans', 50)
WORD_FONT = pygame.font.SysFont('comicsans', 100)
TITLE_FONT = pygame.font.SysFont('comicsans', 70)


def draw_menu(win, HEIGHT, images):
    # draw title
    win.fill(WHITE)
    text = TITLE_FONT.render("HANGMAN", 1, BLACK)
    win.blit(text, [WIDTH / 2 - text.get_width() / 2, 25])

    # draw buttons
    choices = ["     Quit", "2 PLAYERS", "1 PLAYER"]
    for choice in choices:
        pygame.draw.rect(win, BLACK, [WIDTH / 2 - 200, HEIGHT / 1.5, 400, 45], 3)
        text = LETTER_FONT.render(choice, 1, BLACK)
        win.blit(text, [WIDTH / 2 - 100, HEIGHT / 1.5 + 10])
        HEIGHT = HEIGHT - 110
    win.blit(images[1], (300, 175))


def draw_game(win, letters, word, guessed, images, hangman_status):
    win.fill(WHITE)

    # fonts
    LETTER_FONT = pygame.font.SysFont('comicsans', 50)
    WORD_FONT = pygame.font.SysFont('comicsans', 80)
    WORD_FONTXS = pygame.font.SysFont('comicsans', 50)
    TITLE_FONT = pygame.font.SysFont('comicsans', 70)

    win.blit(images[hangman_status], (60, 200))

    # draw title
    text = TITLE_FONT.render("HANGMAN", 1, BLACK)
    win.blit(text, [WIDTH / 2 - text.get_width() / 2, 25])

    # draw word
    lord = len(word)
    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word += letter + " "
            if lord < 15:
                text = WORD_FONT.render(display_word, 1, BLACK)
            else :
                text = WORD_FONTXS.render(display_word, 1, BLACK)
            win.blit(text, (200, 375))
        else:
            display_word += "_ "
            if lord < 15:
                text = WORD_FONT.render(display_word, 1, BLACK)
            else:
                text = WORD_FONTXS.render(display_word, 1, BLACK)
            win.blit(text, (200, 375))

    # draw buttons
    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            pygame.draw.circle(win, BLACK, (x, y), RADIUS, 3)
            text = LETTER_FONT.render(ltr, 1, BLACK)
            win.blit(text, (x - text.get_width() / 2, y - text.get_height() / 2))


def won_lost(message, win, word):
    WORD_FONT = pygame.font.SysFont('comicsans', 80)
    win.fill(WHITE)
    text = WORD_FONT.render(message, 1, BLACK)
    text2 = WORD_FONT.render("Your word was: " + word, 1, BLACK)
    win.blit(text, (WIDTH / 2 - text.get_width() / 2, HEIGHT / 2 - 200))
    win.blit(text2, (WIDTH / 4 - text.get_width() / 2, HEIGHT / 1.5 - text.get_height() / 2))
