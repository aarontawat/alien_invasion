import sys
import pygame

class AlienInvasion:
    """Overall class to manage game assets and behavior"""

    def __init__(self):
        """init the game create game resources"""
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")


    def run_game(self):
        """start main loop for game"""
        while True:
            # watch keybord and mouse event
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                # make recently draw screen visible
                pygame.display.flip()
    
    
if __name__ == '__main__':
    # make game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()