import pygame as py
import random

# Initialize pygame
py.init()

# Screen settings
WIDTH, HEIGHT = 1200, 700
screen = py.display.set_mode((WIDTH, HEIGHT))
py.display.set_caption("Mars Base Investigation")

# Load assets
player_img = py.image.load("images/astronaut-moving.png")  # Replace with actual sprite
background_img = py.image.load("images/mars-windows.png")  # Mars base environment

# Scale images
player_img = py.transform.scale(player_img, (50, 50))
background_img = py.transform.scale(background_img, (WIDTH, HEIGHT))

# Player settings
player_x, player_y = WIDTH // 2, HEIGHT // 2
player_speed = 5

# Logs (clues) for investigation
logs = [
    {"text": "Distress Call: 'They're coming... help...'", "x": 300, "y": 200, "collected": False},
    {"text": "Broken Console: 'Last transmission corrupted... signal lost...'", "x": 700, "y": 500, "collected": False}
]

# Flickering lights effect
flicker_timer = 0
flicker_state = True

# Initialize sound
py.mixer.init()
ambient_sounds = [
    "sound/PMSFX_DSGNDist_Glitch_Distortion_RAW_609GC2_2438.mp3",
    "sound/zapsplat_horror_whispers_ghosts_nightmare_002_12496.mp3",
    "sound/zapsplat_impacts_metal_tubular_hit_clang_004_111166.mp3"
]

def play_random_sound():
    sound = py.mixer.Sound(random.choice(ambient_sounds))
    sound.play()

# Game loop
running = True
clock = py.time.Clock()

while running:
    screen.fill((0, 0, 0))  # Clear screen
    screen.blit(background_img, (0, 0))

    # Flickering light effect (randomly darkens screen)
    flicker_timer += 1
    if flicker_timer > 30:
        flicker_timer = 0
        flicker_state = not flicker_state  # Toggle flicker

    if not flicker_state:
        dark_overlay = py.Surface((WIDTH, HEIGHT), py.SRCALPHA)
        dark_overlay.fill((0, 0, 0, 100))  # Semi-transparent black
        screen.blit(dark_overlay, (0, 0))

    # Player controls
    keys = py.key.get_pressed()
    if keys[py.K_LEFT]:
        player_x -= player_speed
    if keys[py.K_RIGHT]:
        player_x += player_speed
    if keys[py.K_UP]:
        player_y -= player_speed
    if keys[py.K_DOWN]:
        player_y += player_speed

    # Draw player
    screen.blit(player_img, (player_x, player_y))

    # Draw logs (clues)
    for log in logs:
        if not log["collected"]:
            py.draw.circle(screen, (255, 0, 0), (log["x"], log["y"]), 10)  # Red marker for logs

    # Check for log collection
    for log in logs:
        if not log["collected"] and abs(player_x - log["x"]) < 25 and abs(player_y - log["y"]) < 25:
            print("Found Clue:", log["text"])
            log["collected"] = True

    # Random ambient sound trigger
    if random.randint(1, 500) == 1:
        play_random_sound()

    # Event handling
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False

    py.display.flip()
    clock.tick(30)

py.quit()
