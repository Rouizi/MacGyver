import pygame
import os
from random import randrange

pygame.init()

# Opening the Pygame window
height = 450
width = 450
win = pygame.display.set_mode((height,width))

# Title
pygame.display.set_caption('McGyver')

# We load all the images
departure = pygame.image.load(os.path.join("img", "departure.png"))
ether = pygame.transform.scale(pygame.image.load(os.path.join("img", "ether.png")), (30, 30))
guardian = pygame.transform.scale(pygame.image.load(os.path.join("img", "guardian.png")), (30, 30))
mc_down = pygame.image.load(os.path.join("img", "mc_down.png"))
mc_up = pygame.image.load(os.path.join("img", "mc_up.png"))
mc_left = pygame.image.load(os.path.join("img", "mc_left.png"))
mc_right = pygame.image.load(os.path.join("img", "mc_right.png"))
tube = pygame.transform.scale(pygame.image.load(os.path.join("img", "tube.png")), (30, 30))
needle = pygame.image.load(os.path.join("img", "needle.png"))
wall = pygame.image.load(os.path.join("img", "wall.png"))
choice_level = pygame.image.load(os.path.join("img", "choice_level.png")).convert_alpha()
text = pygame.image.load(os.path.join("img", "text.png")).convert_alpha()
game_over = pygame.transform.scale(pygame.image.load(os.path.join("img", "game_over.jpg")), (height, width))
you_win = pygame.image.load(os.path.join("img", "you_win.png"))


liste_img = [departure, ether, guardian, mc_down, mc_up, mc_left, mc_right, tube, needle, wall]

small_img = []
big_img = []

# Small picture for the home screen
for img in liste_img:
    small_img.append(pygame.transform.scale(img, (20, 20)))
    big_img.append(pygame.transform.scale(img, (30, 30)))

pygame.display.flip()


class Level:
    """Class to create a level"""
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

    def labyrinth(self, file):
        """Function to generate the level according to the file and we puts it in 'self.Labyrinth'"""
        self.Labyrinth = []
        # We open the file
        with open(file, 'r') as a_map:
            # We go through the lines of the file
            for line in a_map:
                # We ignore the end of line \ n
                liste = line.strip()
                # We convert 'liste' into list and we put it into self.Labyrinth
                self.Labyrinth.append(list(liste))
        return self.Labyrinth

    def display_labyrinth(self):
        """Method for displaying the level according to the structure list returned by labyrinth()"""
        # We go through the lines of the file
        for l, line in enumerate(self.Labyrinth):
            for c, column in enumerate(line):
                if column == self.begin:# self.begin = 'd' ==> departure
                    if self.index == 0:
                        win.blit(big_img[0], ((c + self.index) * self.rect, (l + self.index) * self.rect))
                    else:
                        win.blit(small_img[0], ((c + self.index) * self.rect, (l + self.index) * self.rect))
                if column == self.wall:# self.wall = 'm' ==> wall
                    if self.index == 0:
                        win.blit(big_img[9], ((c + self.index) * self.rect, (l + self.index) * self.rect))
                    else:
                        win.blit(small_img[9], ((c + self.index) * self.rect, (l + self.index) * self.rect))
                if column == self.guardian:# self.guardian = 'g' ==> guardian
                    if self.index == 0:
                        win.blit(big_img[2], ((c + self.index) * self.rect, (l + self.index) * self.rect))
                    else:
                        win.blit(small_img[2], ((c + self.index) * self.rect, (l + self.index) * self.rect))
                if column == self.ether:# self.ether = 'e' ==> ether
                    win.blit(ether, ((c + self.index) * self.rect, (l + self.index) * self.rect))
                if column == self.needle:# self.needle = 'n' ==> needle
                    win.blit(needle, ((c + self.index) * self.rect, (l + self.index) * self.rect))
                if column == self.tube:# self.tube = 't' ==> tube
                    win.blit(tube, ((c + self.index) * self.rect, (l + self.index) * self.rect))

class Character(Level):
    """Class to create a character"""
    def __init__(self, rect, index, begin, guardian, wall, ether, neddle, tube):
        super().__init__(rect, index, begin, guardian, wall, ether, neddle, tube)

    def position_character(self, wanted):
        """Method to know the position of the character"""
        for l, line in enumerate(self.Labyrinth):
            for c, column in enumerate(line):
                if column == wanted:
                    x, y = l * 30, c * 30
        return x, y

    def check_direction(self, i, j, x, y):
        """Method to check the next direction, if it is not a wall we can move"""
        if self.Labyrinth[int((x + i) / 30)][int((y + j) / 30)] != 'm':
            x, y = x + i, y + j
        return x, y

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
        # all these conditions are necessary so that the coordinates are not equal
        # and the object does not fall on wall or departure or guardian
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
        """Method that checks if ether or tube or needle is in the map"""
        for l, line in enumerate(self.Labyrinth):
            for c, column in enumerate(line):
                if column == self.ether or column == self.tube or column == self.needle:
                    return True

    def remove_objet(self,x, y, x_ether, y_ether, x_needle, y_needle, x_tube, y_tube, remove_e, remove_n, remove_t):
        """Method to delete ether or needle or tube if the character passes over"""
        # if the character's coordinates are equal to those of the object
        # we redisplay the screen without this object
        if (x / 30, y / 30) == (x_ether, y_ether):
            remove_e = True
        if remove_e:
            background = pygame.image.load(os.path.join("img", "background.jpg"))
            win.blit(background, (0, 0))
            self.Labyrinth[x_ether][y_ether] = '0'
            self.display_labyrinth()
        if (x / 30, y / 30) == (x_needle, y_needle):
            remove_n = True
        if remove_n:
            background = pygame.image.load(os.path.join("img", "background.jpg"))
            win.blit(background, (0, 0))
            self.Labyrinth[x_needle][y_needle] = '0'
            self.display_labyrinth()
        if (x / 30, y / 30) == (x_tube, y_tube):
            remove_t = True
        if remove_t :
            background = pygame.image.load(os.path.join("img", "background.jpg"))
            win.blit(background, (0, 0))
            self.Labyrinth[x_tube][y_tube] = '0'
            self.display_labyrinth()
        return remove_e, remove_n, remove_t