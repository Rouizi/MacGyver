import pygame
import os
pygame.init()

win = pygame.display.set_mode((450,450))



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
choice_level = pygame.image.load(os.path.join("img", "choice_level.png")).convert_alpha()
title = pygame.image.load(os.path.join("img", "title.png")).convert_alpha()

liste_img = [departure, ether, guardian, mc_down, mc_up, mc_left, mc_right, tube, needle, wall]

small_img = []
big_img = []

for img in liste_img:
    small_img.append(pygame.transform.scale(img, (20, 20)))
    big_img.append(pygame.transform.scale(img, (30, 30)))

pygame.display.flip()




class Level:


    def __init__(self, rect, index):
        self.rect = rect
        self.index = index
        self.begin = 'd'
        self.guardian = 'a'
        self.wall = 'w'
        self.Labyrinth = []
        self.file = 'maps\\map1.txt'



    def labyrinth(self, file):
        self.Labyrinth = []
        with open(file, 'r') as a_map:
            for line in a_map:
                liste = line.strip()
                self.Labyrinth.append(list(liste))
        return self.Labyrinth

    def display_labyrinth(self):
        for i_liste, liste in enumerate(self.Labyrinth):
            for i_column, column in enumerate(liste):
                if column == 'd':
                    if self.index == 0:
                        win.blit(big_img[0], ((i_column + self.index) * self.rect, (i_liste + self.index) * self.rect))
                    else:
                        win.blit(small_img[0], ((i_column + self.index) * self.rect, (i_liste + self.index) * self.rect))
                if column == 'm':
                    if self.index == 0:
                        win.blit(big_img[-1], ((i_column + self.index) * self.rect, (i_liste + self.index) * self.rect))
                    else:
                        win.blit(small_img[-1], ((i_column + self.index) * self.rect, (i_liste + self.index) * self.rect))
                if column == 'a':
                    if self.index == 0:
                        win.blit(big_img[2], ((i_column + self.index) * self.rect, (i_liste + self.index) * self.rect))
                    else:
                        win.blit(small_img[2], ((i_column + self.index) * self.rect, (i_liste + self.index) * self.rect))



def main():
    pygame.key.set_repeat(400, 30)
    clock = pygame.time.Clock()

    current_part = True

    while current_part:
        clock.tick(30)
        main_menu = True

        while main_menu:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    main_menu = False
                    quit()
                    pygame.quit()


            level = Level(20, 3.75)
            background = pygame.transform.scale(pygame.image.load(os.path.join("img", "background.jpg")), (300,300))
            win.blit(background, (75, 75))
            level.labyrinth(level.file)
            level.display_labyrinth()
            win.blit(small_img[3], (115, 95))
            win.blit(choice_level, (150, 390))
            win.blit(title, (20, 20))
            win.blit(small_img[6], (35, 75))
            win.blit(small_img[5], (395, 75))
            win.blit(small_img[3], (35, 355))
            win.blit(small_img[4], (395, 355))



            pygame.display.flip()
        game = True

        while game:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game = False
                    quit()
                    pygame.quit()
            level = Level(30, 0)
            background = pygame.image.load(os.path.join("img", "background.jpg"))
            win.blit(background, (0, 0))
            level.labyrinth(level.file)
            level.display_labyrinth()

            win.blit(mc_down, (0,0))
            pygame.display.flip()


main()