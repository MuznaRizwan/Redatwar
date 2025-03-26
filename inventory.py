import pygame as py

# Initialize Pygame
py.init()

# Screen Settings
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = py.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
font = py.font.Font(None, 36)

# Base Item Class
class Item:
    def _init_(self, name, image, item_type):
        self.name = name
        self.image = image
        self.item_type = item_type  # "weapon", "power-up"

# Weapon Class
class Weapon(Item):
    def _init_(self, name, image, damage, fire_rate, accuracy, mobility, range_stat, ammo):
        super()._init_(name, image, "weapon")
        self.damage = damage
        self.fire_rate = fire_rate
        self.accuracy = accuracy
        self.mobility = mobility
        self.range_stat = range_stat
        self.ammo = ammo  # Ammo count

# Power-up Class
class PowerUp(Item):
    def _init_(self, name, image, effect):
        super()._init_(name, image, "power-up")
        self.effect = effect  # Example: "Increase Speed"

# Inventory Class
class Inventory:
    items = []
    equipped_weapon = None
    
    def _init_(self):
        self.items = []  
        self.equipped_weapon = None  

    def add_item(self, item):
        # self.items.append(item)
        print('x')

    def equip_weapon(self, weapon):
        # if weapon in self.items and weapon.item_type == "weapon":
        #    self.equipped_weapon = weapon
        print('x')

    def get_total_ammo(self):
        return sum(item.ammo for item in self.items if isinstance(item, Weapon))

# Load Example Images
#sword_img = py.Surface((50, 50))  # Placeholder image
sword_img = py.image.load("..\images\plasma-blade.png")  # Make sure "sword.png" is in the same folder
#sword_img.fill((255, 0, 0))  # Red color
# sword = Weapon("Plasma Blade", sword_img, 50, 5, 80, 70, 10, 0)
gun_img = py.image.load("..\images\plasma-riftle.png") 
#gun_img = py.Surface((50, 50))
#gun_img.fill((0, 255, 0))  # Green color
shield_img = py.image.load("..\images\guardian-shield.png") 
#shield_img = py.Surface((50, 50))
#shield_img.fill((0, 0, 255))  # Blue color

# Create Weapons & Power-ups
sword = Weapon() # "Plasma Blade", sword_img, 50, 5, 80, 70, 10, 0)  # Mele (No ammo)
gun = Weapon() # "Energy Rifle", gun_img, 70, 10, 60, 50, 30, 50)  # 50 ammo
shield = PowerUp() #"Guardian Shield", shield_img, "Blocks Damage")

# Initialize Inventory
player_inventory = Inventory()
player_inventory.add_item(sword)
player_inventory.add_item(gun)
player_inventory.add_item(shield)

# Equip a weapon
player_inventory.equip_weapon(gun)

# Main Game Loop
running = True
while running:
    screen.fill((30, 30, 30))  # Background

    # Draw Inventory Slots
    # for index, item in enumerate(player_inventory.items):
    #     screen.blit(item.image, (100 + index * 60, 200))

    # Display Equipped Weapon
    if player_inventory.equipped_weapon:
        screen.blit(player_inventory.equipped_weapon.image, (350, 50))

    # Show Ammo Counter (Top Right)
    total_ammo = player_inventory.get_total_ammo()
    ammo_text = font.render(f"Ammo: {total_ammo}", True, (255, 255, 255))
    screen.blit(ammo_text, (SCREEN_WIDTH - 150, 20))

    # Event Handling
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False

    py.display.flip()

py.quit()