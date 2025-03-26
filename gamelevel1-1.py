import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Prison Escape")

# Colors
WHITE = (255, 255, 255)
RED = (200, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Game Variables
player_x, player_y = 100, 300
crate_x, crate_y = 400, 450
vent_x, vent_y = 500, 200
security_panel_x, security_panel_y = 200, 250
barrier_active = True
crate_pushed = False
riot_triggered = False
riot_timer = 0
hacking_active = False
hack_sequence = [random.choice(["A", "D", "W", "S"]) for _ in range(4)]
player_input = []
clock = pygame.time.Clock()

# Font
font = pygame.font.Font(None, 36)


def display_text(text, x, y, color=WHITE):
    """ Display text on screen. """
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))


def hacking_mini_game():
    """ Handles the hacking mini-game """
    global hacking_active, barrier_active, player_input

    display_text("Hack Code: " + " ".join(hack_sequence), WIDTH // 2 - 100, HEIGHT // 2, GREEN)

    keys = pygame.key.get_pressed()
    if hacking_active:
        for key in ["a", "d", "w", "s"]:
            if keys[getattr(pygame, f"K_{key}")]:
                player_input.append(key.upper())

        if len(player_input) == len(hack_sequence):
            if player_input == hack_sequence:
                print("Hacking Successful! Barrier Disabled!")
                barrier_active = False
                hacking_active = False
            else:
                print("Hacking Failed! Try Again.")
                player_input = []  # Reset input


def check_vent_escape():
    """ Handles vent escape logic. """
    global crate_pushed

    if not crate_pushed and abs(player_x - crate_x) < 40 and abs(player_y - crate_y) < 40:
        display_text("Press E to push crate", crate_x, crate_y - 30, BLUE)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_e]:
            crate_y -= 50  # Move crate closer to vent
            crate_pushed = True
            print("Crate moved! Vent accessible.")

    if crate_pushed and abs(player_x - vent_x) < 20 and abs(player_y - vent_y) < 20:
        print("Escaping through vent...")
        return True
    return False


def trigger_riot():
    """ Triggers a riot event that temporarily disables the barrier. """
    global riot_triggered, riot_timer, barrier_active
    riot_triggered = True
    riot_timer = time.time()
    barrier_active = False
    print("🚨 PRISON RIOT! Power outage for 5 seconds! 🚨")


def check_riot_timer():
    """ Checks if the riot effect should end. """
    global riot_triggered, barrier_active
    if riot_triggered and time.time() - riot_timer > 5:  # Riot lasts for 5 seconds
        riot_triggered = False
        barrier_active = True
        print("⚡ Power Restored! Barrier is back on!")


def game_loop():
    """ Main game loop """
    global player_x, player_y, hacking_active, barrier_active

    running = True
    while running:
        screen.fill(BLACK)

        # Draw elements
        pygame.draw.rect(screen, RED, (50, 250, 100, 100))  # Holding Cell
        pygame.draw.rect(screen, BLUE, (security_panel_x, security_panel_y, 50, 50))  # Security Panel
        pygame.draw.rect(screen, GREEN, (vent_x, vent_y, 40, 40))  # Vent
        pygame.draw.rect(screen, WHITE, (crate_x, crate_y, 50, 50))  # Crate
        pygame.draw.rect(screen, WHITE, (player_x, player_y, 30, 30))  # Player

        if barrier_active:
            pygame.draw.rect(screen, RED, (150, 250, 10, 100))  # Energy Barrier

        # Check riot timer
        check_riot_timer()

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Movement controls
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_x -= 3
        if keys[pygame.K_RIGHT]:
            player_x += 3
        if keys[pygame.K_UP]:
            player_y -= 3
        if keys[pygame.K_DOWN]:
            player_y += 3

        # Interaction: Hacking
        if abs(player_x - security_panel_x) < 40 and abs(player_y - security_panel_y) < 40:
            display_text("Press E to hack", security_panel_x, security_panel_y - 30, GREEN)
            if keys[pygame.K_e]:
                hacking_active = True

        if hacking_active:
            hacking_mini_game()

        # Interaction: Vent
        if check_vent_escape():
            print("Player escaped through the vent!")
            running = False

        # Riot Event Trigger
        if not riot_triggered and random.randint(1, 1000) > 995:  # 0.5% chance every frame
            trigger_riot()

        # Escape condition
        if not barrier_active and player_x > 150:
            print("Player escaped successfully!")
            running = False

        pygame.display.flip()
        clock.tick(30)


# Run the game
game_loop()
pygame.quit()
