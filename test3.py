import pygame
import random

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 1200, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mars Base Investigation")

# Load assets
player_img = pygame.image.load("astronaut-moving.png")  # Replace with your actual sprite
background_img = pygame.image.load("mars-windows.png")  # Mars base environment

# Scale images
player_img = pygame.transform.scale(player_img, (50, 50))
background_img = pygame.transform.scale(background_img, (WIDTH, HEIGHT))

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

# Sounds (For atmosphere, replace with actual files)
pygame.mixer.init()
ambient_sounds = ["PMSFX_DSGNDist_Glitch_Distortion_RAW_609GC2_2438.mp3", "zapsplat_horror_whispers_ghosts_nightmare_002_12496.mp3", "zapsplat_impacts_metal_tubular_hit_clang_004_111166.mp3"]  # Add creepy background sounds

def play_random_sound():
    sound = pygame.mixer.Sound(random.choice(ambient_sounds))
    sound.play()

# Game loop
running = True
while running:
    screen.fill((0, 0, 0))  # Clear screen

    # Draw background
    screen.blit(background_img, (0, 0))

    # Flickering light effect (randomly darkens screen)
    flicker_timer += 1
    if flicker_timer > 30:  
        flicker_timer = 0
        flicker_state = not flicker_state  # Toggle flicker
    
    if not flicker_state:
        dark_overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        dark_overlay.fill((0, 0, 0, 100))  # Semi-transparent black
        screen.blit(dark_overlay, (0, 0))

    # Player controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]: player_x -= player_speed
    if keys[pygame.K_RIGHT]: player_x += player_speed
    if keys[pygame.K_UP]: player_y -= player_speed
    if keys[pygame.K_DOWN]: player_y += player_speed

    # Draw player
    screen.blit(player_img, (player_x, player_y))

    # Draw logs
    for log in logs:
        if not log["collected"]:
            pygame.draw.circle(screen, (255, 0, 0), (log["x"], log["y"]), 10)  # Red marker for logs

    # Check for log collection
    for log in logs:
        if not log["collected"] and abs(player_x - log["x"]) < 20 and abs(player_y - log["y"]) < 20:
            print("Found Clue:", log["text"])
            log["collected"] = True

    # Random ambient sound trigger
    if random.randint(1, 500) == 1:  
        play_random_sound()

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()
