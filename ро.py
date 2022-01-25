import pygame


class Game_over:
    def __init__(self):
        self.game_over = pygame.image.load('gameover.jpg')
        self.running = True
        pygame.init()
        pygame.display.set_caption('Game over')
        size = width, height = 600, 300

        self.screen = pygame.display.set_mode(size)
        self.x = -600
        self.y = 1

    def sickl(self):
        clock = pygame.time.Clock()
        while self.running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            if self.x == 0:
                self.x += 0
            else:
                self.x += 5
            self.screen.fill('blue')
            self.screen.blit(self.game_over, (self.x, self.y))
            clock.tick(60)
            pygame.display.update()
        pygame.quit()

g = Game_over()
g.sickl()