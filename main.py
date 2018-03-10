import sys
from turtledemo import clock

import pygame
from pygame.locals import *

from node import Node


class Main:

    def __init__(self):
        pygame.init()
        self.frame = pygame.display.set_mode((500, 500))
        pygame.display.set_caption("IA")
        self.flor = pygame.image.load("images/flor.png")
        self.mario = pygame.image.load("images/mario.png")
        self.bloque = pygame.image.load("images/bloque.png")
        self.tortuga = pygame.image.load("images/tortuga.png")
        self.princesa = pygame.image.load("images/peach.png")
        file = open("file.txt", "r")
        self.data = []

        for index, line in enumerate(file.readlines()):
            self.data.append([int(s) for s in line.split() if s.isdigit()])

        self.get_initial_positions()
        self.game_intro()

    def game_intro(self):
        intro = True

        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == 97:
                        self.profundidad()
                    elif event.key == 115:
                        self.costos()
                    elif event.key == 100:
                        self.show_route()
                    elif event.key == 102:
                        self.show_route()
                    elif event.key == 103:
                        self.show_route()

            self.frame.fill((255, 255, 255))
            pygame.display.update()

    def get_initial_positions(self):
        for i in range(10):
            for j in range(10):
                if self.data[i][j] == 2:
                    self.mario_position = (i, j)
                if self.data[i][j] == 5:
                    self.princess_position = (i, j)

    def profundidad(self):
        nodes = []
        initial_node = Node(self.mario_position, None)
        nodes.append(initial_node)
        while not nodes[0].check_is_goal(self.data):
            if (nodes[0].can_move(self.data, 'right')):
                nodes.append(nodes[0].make_child_node('right'))
            if(nodes[0].can_move(self.data, 'up')):
                nodes.append(nodes[0].make_child_node('up'))
            if (nodes[0].can_move(self.data, 'left')):
                nodes.append(nodes[0].make_child_node('left'))
            if (nodes[0].can_move(self.data, 'down')):
                nodes.append(nodes[0].make_child_node('down'))
            nodes.pop(0)
        self.show_route(nodes[0].get_fathers())

    def costos(self):
        nodes = []
        initial_node = Node(self.mario_position, None)
        nodes.append(initial_node)
        while not nodes[0].check_is_goal(self.data):
            if (nodes[0].can_move(self.data, 'right')):
                nodes.append(nodes[0].make_child_node_with_weight('right', self.data))
            if(nodes[0].can_move(self.data, 'up')):
                nodes.append(nodes[0].make_child_node_with_weight('up', self.data))
            if (nodes[0].can_move(self.data, 'left')):
                nodes.append(nodes[0].make_child_node_with_weight('left', self.data))
            if (nodes[0].can_move(self.data, 'down')):
                nodes.append(nodes[0].make_child_node_with_weight('down', self.data))
            nodes.pop(0)
            nodes.sort(key=lambda x: x.weight)
        self.show_route(nodes[0].get_fathers())

    def show_route(self, nodes):
        print([n.weight for n in nodes])
        while True:
            self.frame.fill((255, 255, 255))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            for i in range(10):
                for j in range(10):
                    val = self.data[i][j]
                    if val == 1:
                        self.frame.blit(self.bloque, (50 * j, 50 * i))
                    elif val == 3:
                        self.frame.blit(self.flor, (50 * j, 50 * i))
                    elif val == 4:
                        self.frame.blit(self.tortuga, (50 * j, 50 * i))
            self.frame.blit(self.princesa, (50*self.princess_position[1], 50*self.princess_position[0]))
            self.frame.blit(self.mario, (50 * nodes[0].position[1], 50 * nodes[0].position[0]))
            pygame.display.update()
            pygame.time.delay(1500)
            nodes.pop(0)


Main()
