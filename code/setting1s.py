

import pygame as py
# Initialize pygame
py.init()

# Constants
WIDTH, HEIGHT = 500, 500

settings_image = py.image.load("images/settings screen.png")

# Load images
sound_on_img = py.image.load("images/speaker_on.png")
sound_off_img = py.image.load("images/speaker_off.png")
music_on_img = py.image.load("images/music_on.png")
music_off_img = py.image.load("images/music_off.png")

# Resize images
sound_on_img = py.transform.scale(sound_on_img, (100, 100))
sound_off_img = py.transform.scale(sound_off_img, (100, 100))
music_on_img = py.transform.scale(music_on_img, (100, 100))
music_off_img = py.transform.scale(music_off_img, (100, 100))

# Initialize mixer for sound
py.mixer.init()
sound = py.mixer.Sound("sound/button-click.mp3")  # Replace with actual sound file
py.mixer.music.load("sound/settings_bg_music.mp3")  # Replace with actual music file
py.mixer.music.play(-1)  # Loop music

# Screen class
class Screen:
    def __init__(self, title, width=WIDTH, height=HEIGHT, fill=(0, 0, 0)):
        self.title = title
        self.width = width
        self.height = height
        self.fill = fill
        self.active = False
        self.screen = None

    def makeCurrentScreen(self):
        py.display.set_caption(self.title)
        self.active = True
        self.screen = py.display.set_mode((self.width, self.height))

    def endCurrentScreen(self):
        self.active = False

    def update(self):
        if self.active and self.screen:
            self.screen.fill(self.fill)

# Button class
class Button:
    def __init__(self, x, y, w, h, image_on, image_off, toggle_state=True):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.image_on = image_on
        self.image_off = image_off
        self.toggle_state = toggle_state
        self.image = self.image_on if self.toggle_state else self.image_off
        self.rect = self.image.get_rect(topleft=(x, y))

    def showButton(self, display):
        display.blit(self.image, (self.x, self.y))

    # def checkClick(self, mouse_pos, mouse_click):
    #     if self.rect.collidepoint(mouse_pos) and mouse_click[0]:
    #         clock = py.time.Clock()
    #         self.toggle_state = not self.toggle_state
    #         self.image = self.image_on if self.toggle_state else self.image_off
    #         clock.tick(500)
    #         return True
    #     return False
    
    def checkClick(self, event):
        if event.type == py.MOUSEBUTTONDOWN:  # Detects the press event only once
            if self.rect.collidepoint(event.pos):
                self.toggle_state = not self.toggle_state
                self.image = self.image_on if self.toggle_state else self.image_off
                return True
        return False

    def focusCheck(self, mousepos, mouseclick):
        if self.x <= mousepos[0] <= self.x + self.w and self.y <= mousepos[1] <= self.y + self.h:
            self.CurrentState = True
            return mouseclick[0]
        else:
            self.CurrentState = False
            return False

# Create Settings Screen
settings_screen = Screen(title = "settings screen")
settings_screen.makeCurrentScreen()

# Buttons
sound = Button(100, 200, 100, 100, sound_on_img, sound_off_img)
music = Button(250, 200, 100, 100, music_on_img, music_off_img)

done = False
clock = py.time.Clock()
while not done:
    settings_screen.screen.blit(settings_image, (0, 0))
    mouse_pos = py.mouse.get_pos()
    mouse_click = py.mouse.get_pressed()

    sound.showButton(settings_screen.screen)
    music.showButton(settings_screen.screen)
    # quit_button.showButton(settings_screen.screen)
    # credits_button.showButton(settings_screen.screen)

    
    # if quit_button.focusCheck(mouse_pos, mouse_click):
    #     done = True

    # if credits_button.focusCheck(mouse_pos, mouse_click):
    #     credits_screen = Screen("Credits")
    #     credits_screen.makeCurrentScreen()

    for event in py.event.get():
        if event.type == py.QUIT:
            done = True
        if sound.checkClick(event):
        #     level1_screen = Screen("Level 1")
        #     level1_screen.makeCurrentScreen()
            print('a')

        if music.checkClick(event):
        #     settings_screen = Screen("Settings")
        #     settings_screen.makeCurrentScreen()
            print('b')

    py.display.update()
    clock.tick(500)