import pygame
import os
pygame.init()

win = pygame.display.set_mode((450,450))

background = pygame.image.load(os.path.join("img", "background.jpg"))
win.blit(background, (0,0))

departure = pygame.image.load(os.path.join("img", "departure.png"))
ether = pygame.transform.scale(pygame.image.load(os.path.join("img", "ether.png")), (30,30))
guardian = pygame.transform.scale(pygame.image.load(os.path.join("img", "guardian.png")), (30,30))
mc_down = pygame.image.load(os.path.join("img", "mc_down.png"))
mc_up = pygame.image.load(os.path.join("img", "mc_up.png"))
mc_left = pygame.image.load(os.path.join("img", "mc_left.png"))
mc_right = pygame.image.load(os.path.join("img", "mc_right.png"))
tube = pygame.transform.scale(pygame.image.load(os.path.join("img", "tube.png")), (30,30))
needle = pygame.transform.scale(pygame.image.load(os.path.join("img", "needle.png")), (30,30))
wall = pygame.image.load(os.path.join("img", "wall.png"))


pygame.display.flip()




class Map:
    def __init__(self):
        self.robot = 'd'
        self.guardian = 'a'
        self.Labyrinth = []
        self.wall = 'w'
        self.map = 'maps\\map1.txt'


    def labyrinth(self, carte):
        self.Labyrinth = []
        with open(carte, 'r') as a_map:
            for line in a_map:
                liste = line.strip()
                self.Labyrinth.append(list(liste))
        return self.Labyrinth

    def display_labyrinth(self):
        for line in self.Labyrinth:
            print(''.join(line))


pygame.key.set_repeat(400, 30)
clock = pygame.time.Clock()
continuer = True

while continuer:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = False
            quit()
            pygame.quit()

    m = Map()
    l = m.labyrinth(m.map)
    L = m.Labyrinth
    for index_liste, liste in enumerate(L):
        for index_column, column in enumerate(liste):
            if column == 'd':
                win.blit(departure, (index_column*30, index_liste*30))
            if column == 'm':
                win.blit(wall, (index_column*30, index_liste*30))
            if column == 'a':
                win.blit(guardian, (index_column*30, index_liste*30))
    win.blit(mc_down, (0,0))
    pygame.display.flip()