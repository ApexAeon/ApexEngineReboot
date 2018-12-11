from pygame.locals import *
import json, pygame, sys, os

info = json.load("info.json")

if not os.path.isfile("options.json"):
    json.dump(info["default_options"], open("options.json","w+"))

options = json.load("options.json")

final_display = pygame.display.set_mode((options["window_width"], options["window_height"]))

# INITIALIZE MENU

while True: # Main loop
    for event in pygame.event.get():
        if event.type is QUIT:
            pygame.quit()
            sys.exit()

