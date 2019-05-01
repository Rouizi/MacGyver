#!/usr/bin/python3
# -*- coding: Utf-8 -*

from classes import *
import pygame
import os

x, y = (0, 0)
remove_e = False
remove_n = False
remove_t = False


def main():

    pygame.key.set_repeat(400, 30)
    clock = pygame.time.Clock()

    current_part = True
    # Main loop
    while current_part:
        global position_charc, remove_e, remove_n, remove_t, x, y
        remove_e = False
        remove_n = False
        remove_t = False
        file = 'maps\\map1.txt'

        clock.tick(30)
        main_menu = True

        while main_menu:
            win = pygame.display.set_mode((height, width))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    main_menu = False
                    quit()
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    # Launch of level 1
                    if event.key == pygame.K_F1:
                        file = 'maps\\map1.txt'
                        main_menu = False
                    # Launch of level 2
                    if event.key == pygame.K_F2:
                        file = 'maps\\map2.txt'
                        main_menu = False

            character = Character(20, 3.75, 'd', 'g', 'm', 'e', 'n', 't')
            # Background loading
            background = pygame.transform.scale(pygame.image.load(os.path.join("img", "background.jpg")), (300,300))
            win.blit(background, (75, 75))
            # Generating a level from a file, by default file = 'maps\\map1.txt'
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
        print(x, y)
        x, y = character.position_character(character.begin)
        position_charc = mc_down.get_rect(topleft=(y, x))
        print(x, y)
        # Default image
        mc = mc_down
        x_e, y_e, x_n, y_n, x_t, y_t = character.random_coordinates_of_objects()

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
                        if x > 410:
                            x, y =character.check_direction(0, 0, x, y)
                        else:
                            x, y = character.check_direction(30, 0, x, y)
                    if event.key == pygame.K_UP:
                        # to display the image mc_up
                        mc = mc_up
                        if x < 30:
                            x, y = character.check_direction(0, 0, x, y)
                        else:
                            x, y = character.check_direction(-30, 0, x, y)
                    if event.key == pygame.K_RIGHT:
                        # to display the image mc_right
                        mc = mc_right
                        if y > 410:
                            x, y = character.check_direction(0, 0, x, y)
                        else:
                            x, y = character.check_direction(0, 30, x, y)
                    if event.key == pygame.K_LEFT:
                        # to display the image mc_left
                        mc = mc_left
                        if y < 30:
                            x, y = character.check_direction(0, 0, x, y)
                        else:
                            x, y = character.check_direction(0, -30, x, y)

            background = pygame.image.load(os.path.join("img", "background.jpg"))
            win.blit(background, (0, 0))
            character.labyrinth(file)
            character.display_labyrinth()
            win.blit(ether, (y_e * 30, x_e * 30))
            win.blit(needle, (y_n * 30, x_n * 30))
            win.blit(tube, (y_t * 30, x_t * 30))
            # We do that to know the location of ether in our file, same thing with tube and needle
            character.Labyrinth[x_e][y_e] = character.ether
            character.Labyrinth[x_n][y_n] = character.needle
            character.Labyrinth[x_t][y_t] = character.tube
            remove_e, remove_n, remove_t = \
                character.remove_objet(x, y, x_e, y_e, x_n, y_n, x_t, y_t, remove_e, remove_n, remove_t)
            win.blit(mc, (y, x))
            pygame.display.flip()

            # if tube, or needle, or tube is in the map and the position
            # of the character is equal to that of the guardian we lose
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

                win.blit(game_over, (0, 0))
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

                win.blit(you_win, (125, 125))
                pygame.display.flip()

main()
