import pygame
import os
from random import randrange
pygame.init()

win = pygame.display.set_mode((450,450))
pygame.display.set_caption('McGyver')

x, y = (0, 0)
remove_ether = False
remove_needle = False
remove_tube = False

departure = pygame.image.load(os.path.join("img", "departure.png"))
ether = pygame.transform.scale(pygame.image.load(os.path.join("img", "ether.png")), (30,30))
guardian = pygame.transform.scale(pygame.image.load(os.path.join("img", "guardian.png")), (30,30))
mc_down = pygame.image.load(os.path.join("img", "mc_down.png"))
mc_up = pygame.image.load(os.path.join("img", "mc_up.png"))
mc_left = pygame.image.load(os.path.join("img", "mc_left.png"))
mc_right = pygame.image.load(os.path.join("img", "mc_right.png"))
tube = pygame.transform.scale(pygame.image.load(os.path.join("img", "tube.png")), (30,30))
needle = pygame.image.load(os.path.join("img", "needle.png"))
wall = pygame.image.load(os.path.join("img", "wall.png"))
choice_level = pygame.image.load(os.path.join("img", "choice_level.png")).convert_alpha()
text = pygame.image.load(os.path.join("img", "text.png")).convert_alpha()
game_over = pygame.transform.scale(pygame.image.load(os.path.join("img", "game_over.jpg")), (450,450))
you_win = pygame.transform.scale(pygame.image.load(os.path.join("img", "you_win.png")), (450,450))

position_charc = mc_down.get_rect(topleft=(y, x))

liste_img = [departure, ether, guardian, mc_down, mc_up, mc_left, mc_right, tube, needle, wall]

small_img = []
big_img = []

for img in liste_img:
    small_img.append(pygame.transform.scale(img, (20, 20)))
    big_img.append(pygame.transform.scale(img, (30, 30)))



pygame.display.flip()


class Level:
    def __init__(self, rect, index, begin, guardian, wall, ether, neddle, tube):
        self.rect = rect
        self.index = index
        self.begin = begin
        self.guardian = guardian
        self.wall = wall
        self.ether = ether
        self.needle = neddle
        self.tube = tube
        self.Labyrinth = []
        #self.file = 'maps\\map1.txt'

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
                if column == self.ether:
                    win.blit(ether, ((c + self.index) * self.rect, (i + self.index) * self.rect))
                if column == self.needle:
                    win.blit(needle, ((c + self.index) * self.rect, (i + self.index) * self.rect))
                if column == self.tube:
                    win.blit(tube, ((c + self.index) * self.rect, (i + self.index) * self.rect))

class Character(Level):

    def __init__(self, rect, index, begin, guardian, wall, ether, neddle, tube):
        super().__init__(rect, index, begin, guardian, wall, ether, neddle, tube)
        self.winner = False

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
            x, y = x + j, y + i
            position_charc = position_charc.move(j, i)

    def random_coordinates_of_objects(self):
        """this function is responsible for giving random coordinates to put
        ether, tube and needle objects in the map and in the file
        """
        x_ether = randrange(15)
        y_ether = randrange(15)
        x_needle = randrange(15)
        y_needle = randrange(15)
        x_tube = randrange(15)
        y_tube = randrange(15)
        if (self.Labyrinth[x_ether][y_ether] != self.wall and
            self.Labyrinth[x_ether][y_ether] != self.begin and
            self.Labyrinth[x_ether][y_ether] != self.guardian and
            self.Labyrinth[x_needle][y_needle] != self.wall and
            self.Labyrinth[x_needle][y_needle] != self.begin and
            self.Labyrinth[x_needle][y_needle] != self.guardian and
            self.Labyrinth[x_tube][y_tube] != self.wall and
            self.Labyrinth[x_tube][y_tube] != self.begin and
            self.Labyrinth[x_tube][y_tube] != self.guardian and
            (x_ether, y_ether) != (x_needle, y_needle) and
            (x_ether, y_ether) != (x_tube, y_tube) and
            (x_tube, y_tube) != (x_needle, y_needle)):

            return x_ether, y_ether, x_needle, y_needle, x_tube, y_tube
        else:
            return self.random_coordinates_of_objects()

    def object_in_map(self):
        for i, line in enumerate(self.Labyrinth):
            for c, column in enumerate(line):
                if column == self.ether or column == self.tube or column == self.needle:
                    return True

    def remove_objet(self, x_ether, y_ether, x_needle, y_needle, x_tube, y_tube):
        global remove_ether, remove_needle, remove_tube
        if (x / 30, y / 30) == (y_ether, x_ether):
            remove_ether = True
        if remove_ether:
            background = pygame.image.load(os.path.join("img", "background.jpg"))
            win.blit(background, (0, 0))
            self.Labyrinth[x_ether][y_ether] = '0'
            self.display_labyrinth()
        if (x / 30, y / 30) == (y_needle, x_needle):
            remove_needle = True
        if remove_needle:
            background = pygame.image.load(os.path.join("img", "background.jpg"))
            win.blit(background, (0, 0))
            self.Labyrinth[x_needle][y_needle] = '0'
            self.display_labyrinth()
        if (x / 30, y / 30) == (y_tube, x_tube):
            remove_tube = True
        if remove_tube :
            background = pygame.image.load(os.path.join("img", "background.jpg"))
            win.blit(background, (0, 0))
            self.Labyrinth[x_tube][y_tube] = '0'
            self.display_labyrinth()


def main():
    pygame.key.set_repeat(400, 30)
    clock = pygame.time.Clock()

    current_part = True

    while current_part:
        global position_charc, remove_ether, remove_needle, remove_tube
        remove_ether = False
        remove_needle = False
        remove_tube = False

        clock.tick(30)
        main_menu = True

        while main_menu:
            win = pygame.display.set_mode((450, 450))
            file = 'maps\\map1.txt'

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    main_menu = False
                    quit()
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_F1:
                        file = 'maps\\map1.txt'
                        main_menu = False
                    if event.key == pygame.K_F2:
                        file = 'maps\\map2.txt'
                        main_menu = False

            character = Character(20, 3.75, 'd', 'g', 'm', 'e', 'n', 't')
            background = pygame.transform.scale(pygame.image.load(os.path.join("img", "background.jpg")), (300,300))
            win.blit(background, (75, 75))
            character.labyrinth(file)
            character.display_labyrinth()
            win.blit(small_img[3], (115, 95))
            win.blit(choice_level, (150, 390))
            win.blit(text, (20, 20))
            win.blit(small_img[6], (35, 75))
            win.blit(small_img[5], (395, 75))
            win.blit(small_img[3], (35, 355))
            win.blit(small_img[4], (395, 355))

            pygame.display.flip()

        character = Character(30, 0, 'd', 'g', 'm', 'e', 'n', 't')
        character.labyrinth(file)
        character.position_character(character.begin)
        position_charc = mc_down.get_rect(topleft=(y, x))
        mc = mc_down
        x_ether, y_ether, x_needle, y_needle, x_tube, y_tube = character.random_coordinates_of_objects()

        end_game = False

        while not end_game:
            gameover = False
            victory = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    end_game = True
                    quit()
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        end_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        mc = mc_down
                        if y > 410:
                            character.check_direction(0, 0)
                        else:
                            character.check_direction(30, 0)
                    if event.key == pygame.K_UP:
                        mc = mc_up
                        if y < 30:
                            character.check_direction(0, 0)
                        else:
                            character.check_direction(-30, 0)
                    if event.key == pygame.K_RIGHT:
                        mc = mc_right
                        if x > 410:
                            character.check_direction(0, 0)
                        else:
                            character.check_direction(0, 30)
                    if event.key == pygame.K_LEFT:
                        mc = mc_left
                        if x < 30:
                            character.check_direction(0, 0)
                        else:
                            character.check_direction(0, -30)

            background = pygame.image.load(os.path.join("img", "background.jpg"))
            win.blit(background, (0, 0))
            character.labyrinth(file)
            character.display_labyrinth()
            win.blit(ether, (y_ether * 30, x_ether * 30))
            win.blit(needle, (y_needle * 30, x_needle * 30))
            win.blit(tube, (y_tube * 30, x_tube * 30))


            character.Labyrinth[x_ether][y_ether] = character.ether# we do that to know the location of ether
            character.Labyrinth[x_needle][y_needle] = character.needle#in our file, same thing with tube and needle
            character.Labyrinth[x_tube][y_tube] = character.tube
            character.remove_objet(x_ether, y_ether, x_needle, y_needle, x_tube, y_tube)
            win.blit(mc, position_charc)
            pygame.display.flip()
            if (character.object_in_map() and
               character.Labyrinth[int(x / 30)][int(y / 30)] == character.guardian):
                end_game = True
                gameover = True
            if (not character.object_in_map() and
               character.Labyrinth[int(x / 30)][int(y / 30)] == character.guardian):
                    end_game = True
                    victory = True

            while gameover:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        gameover = False
                        quit()
                        pygame.quit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            gameover = False
                            end_game = True

                win = pygame.display.set_mode((450, 450))
                win.blit(game_over, (0, 0))
                pygame.display.flip()

                pygame.display.flip()

            while victory:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        victory = False
                        quit()
                        pygame.quit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            victory = False
                            gameover = False
                            end_game = True

                win = pygame.display.set_mode((450, 450))
                win.blit(you_win, (0, 0))
                pygame.display.flip()


main()
