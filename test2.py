import pygame as py

# Initialize pygame
py.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = py.display.set_mode((WIDTH, HEIGHT))
py.display.set_caption("Credits")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Fonts
font_heading = py.font.Font(None, 50)
font_body = py.font.Font(None, 30)

# Text
heading = font_heading.render("CREDITS", True, WHITE)
body = font_body.render("Indie Game Developer: Muzna Rizwan", True, WHITE)

# Main loop
running = True
while running:
    screen.fill(BLACK)

    # Blit text
    screen.blit(heading, (WIDTH // 2 - heading.get_width() // 2, 200))
    screen.blit(body, (WIDTH // 2 - body.get_width() // 2, 300))

    for event in py.event.get():
        if event.type == py.QUIT:
            running = False

    py.display.flip()

py.quit()
