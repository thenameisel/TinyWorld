from os import walk
import pygame

def import_folder(path):
    surfice_list = []

    for _, _, image_files in walk(path):
        for image in image_files:
            full_path = path + '/' + image
            image_surf = pygame.image.load(full_path).convert_alpha()
            surfice_list.append(image_surf)

    return surfice_list