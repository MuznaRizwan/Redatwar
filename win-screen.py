import pygame as py
import random
import time

# Initialize pygame
py.init()

# Screen settings
WIDTH, HEIGHT = 1200, 700
screen = py.display.set_mode((WIDTH, HEIGHT))
py.display.set_caption("Mars Base Investigation")

# Load assets
player_img = py.image.load("images/astronaut-moving.png")  # Replace with actual sprite
background_img = py.image.load("images/mars-windows.png")  # Mars base environment
game_over_bg = py.image.load("images/game_over.png")  # Game Over screen background
win_screen_bg = py.image.load("images/win-screen.png")  # Win screen background

# Scale images
player_img = py.transform.scale(player_img, (50, 50))
background_img = py.transform.scale(background_img, (WIDTH, HEIGHT))
game_over_bg = py.transform.scale(game_over_bg, (WIDTH, HEIGHT))
win_screen_bg = py.transform.scale(win_screen_bg, (WIDTH, HEIGHT))

# Load pixelated font
pixel_font = py.font.Font("fonts/pixel_font.ttf", 60)  # Ensure you have a pixelated font
body_font = py.font.Font("fonts/pixel_font.ttf", 40)

# Player settings
player_x, player_y = WIDTH // 2, HEIGHT // 2
player_speed = 5

# Logs (clues) for investigation
logs = [
    {"text": "Distress Call: 'They're coming... help...'", "x": 300, "y": 200, "collected": False},
    {"text": "Broken Console: 'Last transmission corrupted... signal lost...'", "x": 700, "y": 500, "collected": False}
]

# Initialize time & points
start_time = time.time()
points = 0
game_over = False
win = False

# Game loop
running = True
clock = py.time.Clock()

while running:
    if not game_over and not win:
        screen.fill((0, 0, 0))  # Clear screen
        screen.blit(background_img, (0, 0))

        # Player controls
        keys = py.key.get_pressed()
        if keys[py.K_LEFT]: player_x -= player_speed
        if keys[py.K_RIGHT]: player_x += player_speed
        if keys[py.K_UP]: player_y -= player_speed
        if keys[py.K_DOWN]: player_y += player_speed

        # Draw player
        screen.blit(player_img, (player_x, player_y))

        # Draw logs (clues)
        for log in logs:
            if not log["collected"]:
                py.draw.circle(screen, (255, 0, 0), (log["x"], log["y"]), 10)

        # Check for log collection
        collected_all_logs = True
        for log in logs:
            if not log["collected"] and abs(player_x - log["x"]) < 25 and abs(player_y - log["y"]) < 25:
                print("Found Clue:", log["text"])
                log["collected"] = True
                points += 10  # Increase points for collecting clues
            if not log["collected"]:
                collected_all_logs = False

        # Lose condition (example: time runs out)
        elapsed_time = int(time.time() - start_time)
        if elapsed_time > 60:  # Example: player loses after 60 seconds
            game_over = True
        
        # Win condition (all logs collected)
        if collected_all_logs:
            win = True

        # Event handling
        for event in py.event.get():
            if event.type == py.QUIT:
                running = False

        py.display.flip()
        clock.tick(30)
    
    elif game_over:
        # Game Over Screen
        screen.blit(game_over_bg, (0, 0))
        game_over_text = pixel_font.render("GAME OVER", True, (255, 0, 0))
        screen.blit(game_over_text, (WIDTH // 2 - 150, HEIGHT // 4))
        
        # Display stats
        score_text = body_font.render(f"Points: {points}", True, (255, 255, 255))
        time_text = body_font.render(f"Time Survived: {elapsed_time} sec", True, (255, 255, 255))
        screen.blit(score_text, (WIDTH // 2 - 100, HEIGHT // 2))
        screen.blit(time_text, (WIDTH // 2 - 180, HEIGHT // 2 + 50))
        
        restart_text = body_font.render("Press R to Restart or Q to Quit", True, (255, 255, 255))
        screen.blit(restart_text, (WIDTH // 2 - 250, HEIGHT // 2 + 120))
        
        py.display.flip()
        for event in py.event.get():
            if event.type == py.QUIT:
                running = False
            if event.type == py.KEYDOWN:
                if event.key == py.K_r:
                    game_over = False
                    player_x, player_y = WIDTH // 2, HEIGHT // 2
                    start_time = time.time()
                    points = 0
                    for log in logs:
                        log["collected"] = False
                if event.key == py.K_q:
                    running = False
    
    elif win:
        # Win Screen
        screen.blit(win_screen_bg, (0, 0))
        win_text = pixel_font.render("YOU WIN!", True, (0, 255, 0))
        screen.blit(win_text, (WIDTH // 2 - 100, HEIGHT // 4))
        
        score_text = body_font.render(f"Points: {points}", True, (255, 255, 255))
        time_text = body_font.render(f"Time Taken: {elapsed_time} sec", True, (255, 255, 255))
        screen.blit(score_text, (WIDTH // 2 - 100, HEIGHT // 2))
        screen.blit(time_text, (WIDTH // 2 - 180, HEIGHT // 2 + 50))
        
        restart_text = body_font.render("Press R to Restart or Q to Quit", True, (255, 255, 255))
        screen.blit(restart_text, (WIDTH // 2 - 250, HEIGHT // 2 + 120))
        
        py.display.flip()
        for event in py.event.get():
            if event.type == py.QUIT:
                running = False
            if event.type == py.KEYDOWN:
                if event.key == py.K_r:
                    win = False
                    player_x, player_y = WIDTH // 2, HEIGHT // 2
                    start_time = time.time()
                    points = 0
                    for log in logs:
                        log["collected"] = False
                if event.key == py.K_q:
                    running = False

py.quit()


