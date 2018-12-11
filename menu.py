def menu(data):
    while True: # Main loop
        for event in pygame.event.get():
            if event.type is QUIT:
                pygame.quit()
                sys.exit()
            for action in data["actions"]:
                if event.type == action["type"]

