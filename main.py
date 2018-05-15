import random
import sys
from timeit import Timer
from turtledemo import clock

import pygame
import time
from pygame.locals import *

from node import Node


class Main:

    def __init__(self):
        pygame.init()
        self.frame = pygame.display.set_mode((600, 600))
        self.caballo_negro = pygame.image.load("images/caballo_negro.png")
        self.caballo_blanco = pygame.image.load("images/caballo_blanco.png")
        self.manzana_sprite = pygame.image.load("images/manzana.png")

        pygame.display.set_caption("IA")
        self.humano = (random.randint(0, 5), random.randint(0, 5))
        while True:
            x = random.randint(0, 5)
            y = random.randint(0, 5)
            if x != self.humano[0] or y != self.humano[1]:
                break
        self.maquina = (0, 5)
        self.manzanas = []
        while len(self.manzanas) != 1:
            x = random.randint(0, 5)
            y = random.randint(0, 5)
            if (x != self.humano[0] or y != self.humano[1]) and (x != self.maquina[0] or y != self.maquina[1]):
                self.manzanas.append((x, y))
        self.manzanas = [(1, 3)]
        self.juega_humano()

    def paint_background(self):
        self.frame.fill((255, 255, 255))
        for i in range(6):
            for j in range(6):
                if (i % 2 == 0):
                    if (j % 2 != 0):
                        pygame.draw.rect(self.frame, (161, 161, 161), (j * 100, i * 100, 100, 100))
                else:
                    if (j % 2 == 0):
                        pygame.draw.rect(self.frame, (161, 161, 161), (j * 100, i * 100, 100, 100))

    def paint_initial(self):
        print(self.humano, self.maquina)
        self.frame.blit(self.caballo_negro, (100 * self.humano[0], 100 * self.humano[1]))
        self.frame.blit(self.caballo_blanco, (100 * self.maquina[0], 100 * self.maquina[1]))
        for manzana in self.manzanas:
            self.frame.blit(self.manzana_sprite, (100 * manzana[0], 100 * manzana[1]))
        pygame.display.update()

    def juega_maquina(self):
        init_node = Node(self.maquina, self.humano, None,  self.manzanas, True, 0, 0)
        self.maquina = init_node.play()

    def juega_humano(self):
        self.paint_background()
        self.rectangles = []
        moves = self.get_moves(self.humano)
        if (self.maquina in moves):
            moves.remove(self.maquina)
        for move in moves:
            self.rectangles.append(
                {
                    'position': move,
                    'rect': pygame.draw.rect(self.frame, (255, 102, 102), (move[0] * 100, move[1] * 100, 100, 100))
                }
            )

        self.paint_initial()

        pygame.display.update()
        wait = True
        while wait:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    for rectangle in self.rectangles:
                        if rectangle['rect'].collidepoint(pos):
                            self.humano = rectangle['position']
                            wait = False
                            break
        self.juega_maquina()

    def get_moves(self, caballo):
        moves = []
        moves.append((caballo[0]-2, caballo[1]-1))
        moves.append((caballo[0]-2, caballo[1]+1))
        moves.append((caballo[0]+2, caballo[1]-1))
        moves.append((caballo[0]+2, caballo[1]+1))
        moves.append((caballo[0]-1, caballo[1]-2))
        moves.append((caballo[0]+1, caballo[1]-2))
        moves.append((caballo[0]-1, caballo[1]+2))
        moves.append((caballo[0]+1, caballo[1]+2))
        true_moves = []
        for move in moves:
            if(move[0] >= 0 and move[0] <= 5 and move[1] >= 0 and move[1] <= 5):
                true_moves.append(move)
        return true_moves
Main()
