import pygame as py

# Initialize Pygame
py.init()
py.font.init()

# Screen Class
class Screen():
    def __init__(self, title, width=440, height=445, fill=(0, 0, 0)):
        self.title = title
        self.width = width
        self.height = height
        self.fill = fill
        self.CurrentState = False
        self.screen = None  # Initialize screen as None

    def makeCurrentScreen(self):
        py.display.set_caption(self.title)
        self.CurrentState = True
        self.screen = py.display.set_mode((self.width, self.height))

    def endCurrentScreen(self):
        self.CurrentState = False

    def checkUpdate(self, fill):
        self.fill = fill
        return self.CurrentState

    def screenUpdate(self):
        if self.CurrentState:
            self.screen.fill(self.fill)
            py.display.update()

    def returnTitle(self):
        return self.title

# Button Class
class Button():
    def __init__(self, x, y, sx, sy, bcolour, fbcolour, font, fcolour, text):
        self.x = x
        self.y = y
        self.sx = sx
        self.sy = sy
        self.bcolour = bcolour
        self.fbcolour = fbcolour
        self.fcolour = fcolour
        self.text = text
        self.CurrentState = False
        self.fontsize = 25
        self.buttonf = py.font.SysFont(font, self.fontsize)

    def showButton(self, display):
        py.draw.rect(display, self.fbcolour, (self.x, self.y, self.sx, self.sy))
        textsurface = self.buttonf.render(self.text, False, self.fcolour)
        display.blit(textsurface, (self.x + (self.sx // 2) - (self.fontsize // 2) * (len(self.text) // 2) - 5,
                                   self.y + (self.sy // 2) - (self.fontsize // 2) - 4))

    def focusCheck(self, mousepos, mouseclick):
        if self.x <= mousepos[0] <= self.x + self.sx and self.y <= mousepos[1] <= self.y + self.sy:
            self.CurrentState = True
            return mouseclick[0]  # Returns True if left-clicked
        else:
            self.CurrentState = False
            return False

# Create Screens
trailer_screen_1 = Screen("Trailer Screen 1")
splash_screen = Screen("Splash Screen")

# Make the first screen active
trailer_screen_1.makeCurrentScreen()

# Create Buttons
SPLASH_BUTTON_1 = Button(150, 150, 150, 50, (255, 250, 250), (255, 0, 0), "TimesNewRoman", (255, 255, 255), "Play Game")
SPLASH_BUTTON_2 = Button(150, 210, 150, 50, (0, 0, 0), (0, 0, 255), "TimesNewRoman", (255, 255, 255), "Settings")
SPLASH_BUTTON_3 = Button(150, 270, 150, 50, (0, 0, 0), (0, 0, 255), "TimesNewRoman", (255, 255, 255), "Credits")
SPLASH_BUTTON_4 = Button(150, 330, 150, 50, (0, 0, 0), (255, 0, 0), "TimesNewRoman", (255, 255, 255), "Quit")

# Main Loop
done = False

while not done:
    trailer_screen_1.screenUpdate()

    # Get mouse position and click events
    mouse_pos = py.mouse.get_pos()
    mouse_click = py.mouse.get_pressed()

    # Draw Buttons
    SPLASH_BUTTON_1.showButton(trailer_screen_1.screen)
    SPLASH_BUTTON_2.showButton(trailer_screen_1.screen)
    SPLASH_BUTTON_3.showButton(trailer_screen_1.screen)
    SPLASH_BUTTON_4.showButton(trailer_screen_1.screen)

    # Handle Button Clicks
    if SPLASH_BUTTON_1.focusCheck(mouse_pos, mouse_click):
        print("Play Game Clicked!")  
        trailer_screen_1.endCurrentScreen()
        splash_screen.makeCurrentScreen()

    if SPLASH_BUTTON_2.focusCheck(mouse_pos, mouse_click):
        print("Settings Clicked!")

    if SPLASH_BUTTON_3.focusCheck(mouse_pos, mouse_click):
        print("Credits Clicked!")

    if SPLASH_BUTTON_4.focusCheck(mouse_pos, mouse_click):
        print("Quit Clicked!")
        done = True  # Exit the game loop

    # Event Handling
    for event in py.event.get():
        if event.type == py.QUIT:
            done = True

py.quit()
