import pygame
import os
pygame.init()

win = pygame.display.set_mode((450,450))
pygame.display.set_caption('McGyver')

x, y = (0, 0)

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

position_charc = mc_down.get_rect(topleft=(y, x))

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
        self.guardian = 'g'
        self.wall = 'm'
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
        for i, line in enumerate(self.Labyrinth):
            for c, column in enumerate(line):
                if column == self.begin:
                    if self.index == 0:
                        win.blit(big_img[0], ((c + self.index) * self.rect, (i + self.index) * self.rect))
                    else:
                        win.blit(small_img[0], ((c + self.index) * self.rect, (i + self.index) * self.rect))
                if column == self.wall:
                    if self.index == 0:
                        win.blit(big_img[9], ((c + self.index) * self.rect, (i + self.index) * self.rect))
                    else:
                        win.blit(small_img[9], ((c + self.index) * self.rect, (i + self.index) * self.rect))
                if column == self.guardian:
                    if self.index == 0:
                        win.blit(big_img[2], ((c + self.index) * self.rect, (i + self.index) * self.rect))
                    else:
                        win.blit(small_img[2], ((c + self.index) * self.rect, (i + self.index) * self.rect))

class Character(Level):

    def __init__(self, rect, index):
        super().__init__(rect, index)
        """self.up = mc_up
        self.down = mc_down
        self.right = mc_right
        self.left = mc_left"""

    def position_character(self, wanted):
        global x, y
        for i, line in enumerate(self.Labyrinth):
            for c, column in enumerate(line):
                if column == wanted:
                    x, y = i * 30, c * 30
        return x, y

    def check_direction(self, i, j):
        global position_charc, x ,y
        if self.Labyrinth[int((y + i) / 30)][int((x + j) / 30)] != 'm':
            print(self.Labyrinth[int((y + i) / 30)][int((x + j) / 30)])
            print(x, y)
            x , y = x + j, y + i
            print(x, y)
            position_charc = position_charc.move(j, i)





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
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_F1:
                        main_menu = False

            character = Character(20, 3.75)
            background = pygame.transform.scale(pygame.image.load(os.path.join("img", "background.jpg")), (300,300))
            win.blit(background, (75, 75))
            character.labyrinth(character.file)
            character.display_labyrinth()
            win.blit(small_img[3], (115, 95))
            win.blit(choice_level, (150, 390))
            win.blit(title, (20, 20))
            win.blit(small_img[6], (35, 75))
            win.blit(small_img[5], (395, 75))
            win.blit(small_img[3], (35, 355))
            win.blit(small_img[4], (395, 355))

            pygame.display.flip()

        global position_charc
        character = Character(30, 0)
        character.labyrinth(character.file)
        character.position_character(character.begin)
        position_charc = mc_down.get_rect(topleft=(y, x))

        game = True

        while game:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game = False
                    quit()
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        character.check_direction(30, 0)
                    if event.key == pygame.K_UP:
                        character.check_direction(-30, 0)
                    if event.key == pygame.K_RIGHT:
                        character.check_direction(0, 30)
                    if event.key == pygame.K_LEFT:
                        character.check_direction(0, -30)
                        win.blit(mc_left, position_charc)



            background = pygame.image.load(os.path.join("img", "background.jpg"))
            win.blit(background, (0, 0))
            character.labyrinth(character.file)
            character.display_labyrinth()
            win.blit(mc_down, position_charc)

            pygame.display.flip()


main()