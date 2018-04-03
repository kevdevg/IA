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
        self.frame = pygame.display.set_mode((500, 500))
        pygame.display.set_caption("IA")
        self.flor = pygame.image.load("images/flor.png")
        self.mario = pygame.image.load("images/mario.png")
        self.mario_flor = pygame.image.load("images/mario_flor.png")
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
                    if event.key == 49 or event.key == 257: #Tecla 1
                        self.amplitud()
                    elif event.key == 50 or event.key == 258: #Tecla 2
                        self.costos()
                    elif event.key == 51 or event.key == 259: #Tecla 3
                        self.profundidad()
                    elif event.key == 52 or event.key == 260: #Tecla 4
                        self.avaro()
                    elif event.key == 53 or event.key == 261: #Tecla 5
                        self.estrella()
                    elif event.key == 27: #Tecla ESC
                        pygame.quit()
                        quit()

            #Se Pinta la pantalla en blanco
            self.frame.fill((255, 255, 255))

            #Se crea las fuentes para el menú
            font_title_menu = pygame.font.Font(None, 50)
            font_menu = pygame.font.Font(None, 30)

            #Se crean los mensajes
            title_menu = "Mario-Smart"
            text_menu_1 = "Para algoritmos de búsqueda No Informada:"
            text_menu_2 = "- Presione 1 para 'Amplitud'"
            text_menu_3 = "- Presione 2 para 'Costo Uniforme'"
            text_menu_4 = "- Presione 3 para 'Profundidad evitando ciclos'"
            text_menu_5 = "Para algoritmos de búsqueda Informada:"
            text_menu_6 = "- Presione 4 para 'Avara'"
            text_menu_7 = "- Presione 5 para 'A*'"
            text_menu_8 = "Para salir presione 'ESC'"

            #Se aplican las fuentes
            menu_1 = font_title_menu.render(title_menu, 1, (255, 0, 0))
            menu_2 = font_menu.render(text_menu_1, 1, (0, 0, 0))
            menu_3 = font_menu.render(text_menu_2, 1, (0, 0, 0))
            menu_4 = font_menu.render(text_menu_3, 1, (0, 0, 0))
            menu_5 = font_menu.render(text_menu_4, 1, (0, 0, 0))
            menu_6 = font_menu.render(text_menu_5, 1, (0, 0, 0))
            menu_7 = font_menu.render(text_menu_6, 1, (0, 0, 0))
            menu_8 = font_menu.render(text_menu_7, 1, (0, 0, 0))
            menu_9 = font_menu.render(text_menu_8, 1, (0, 0, 0))

            #Se pintan en pantalla
            self.frame.blit(menu_1, (150, 10))
            self.frame.blit(menu_2, (15, 63))
            self.frame.blit(menu_3, (40, 100))
            self.frame.blit(menu_4, (40, 140))
            self.frame.blit(menu_5, (40, 180))
            self.frame.blit(menu_6, (15, 230))
            self.frame.blit(menu_7, (40, 270))
            self.frame.blit(menu_8, (40, 310))
            self.frame.blit(menu_9, (15, 360))
            
            pygame.display.update()

    def get_initial_positions(self):
        for i in range(10):
            for j in range(10):
                if self.data[i][j] == 2:
                    self.mario_position = (i, j)
                if self.data[i][j] == 5:
                    self.princess_position = (i, j)

    def profundidad(self):
        print("profundidad")
        start_time = time.time()

        nodes = []
        initial_node = Node(self.mario_position, None)
        nodes.append(initial_node)
        counter = 0
        while not nodes[0].check_is_goal(self.data):
        # for i in range(150):
            actual_node = nodes[0]
            nodes.pop(0)
            # con esta organización el algoritmo muere
            # if (actual_node.can_move(self.data, 'right')):
            #     nodes.insert(0, actual_node.make_child_node('right'))
            # if(actual_node.can_move(self.data, 'up')):
            #     nodes.insert(0, actual_node.make_child_node('up'))
            # if (actual_node.can_move(self.data, 'left')):
            #     nodes.insert(0, actual_node.make_child_node('left'))
            # if (actual_node.can_move(self.data, 'down')):
            #     nodes.insert(0, actual_node.make_child_node('down'))
            if (actual_node.can_move(self.data, 'up')):
                nodes.insert(0, actual_node.make_child_node('up'))
            if (actual_node.can_move(self.data, 'right')):
                nodes.insert(0, actual_node.make_child_node('right'))
            if (actual_node.can_move(self.data, 'down')):
                nodes.insert(0, actual_node.make_child_node('down'))
            if (actual_node.can_move(self.data, 'left')):
                nodes.insert(0, actual_node.make_child_node('left'))
            counter += 1
        algorithm_data = {
            'name': "Profundidad evitando ciclos",
            'nodos_expandidos': counter,
            'nodos_creados': counter + len(nodes),
            'tiempo_de_ejecucion': "%s" % (time.time() - start_time)
        }
        self.show_route(nodes[0].get_fathers(), algorithm_data)

    def amplitud(self):
        print("amplitud")
        start_time = time.time()
        nodes = []
        initial_node = Node(self.mario_position, None)
        nodes.append(initial_node)
        counter = 0
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
            counter += 1
        algorithm_data = {
            'name': "Referente por amplitud",
            'nodos_expandidos': counter,
            'nodos_creados': counter + len(nodes),
            'tiempo_de_ejecucion': "%s" % (time.time() - start_time)
        }

        self.show_route(nodes[0].get_fathers(), algorithm_data)

    def costos(self):
        print("costos")
        nodes = []
        start_time = time.time()
        initial_node = Node(self.mario_position, None)
        nodes.append(initial_node)
        counter = 0
        while not nodes[0].check_is_goal(self.data):
            if (nodes[0].can_move(self.data, 'right')):
                nodes.append(nodes[0].make_child_node_with_weight('right', self.data, False))
            if(nodes[0].can_move(self.data, 'up')):
                nodes.append(nodes[0].make_child_node_with_weight('up', self.data, False))
            if (nodes[0].can_move(self.data, 'left')):
                nodes.append(nodes[0].make_child_node_with_weight('left', self.data, False))
            if (nodes[0].can_move(self.data, 'down')):
                nodes.append(nodes[0].make_child_node_with_weight('down', self.data, False))
            nodes.pop(0)
            nodes.sort(key=lambda x: x.weight)
            counter += 1
        algorithm_data = {
            'name': 'Referente por costos',
            'nodos_expandidos': counter,
            'nodos_creados': counter + len(nodes),
            'tiempo_de_ejecucion': "%s" % (time.time() - start_time)
        }
        self.show_route(nodes[0].get_fathers(), algorithm_data)

    def avaro(self):
        print("avaro")
        nodes = []
        start_time = time.time()
        initial_node = Node(self.mario_position, None)
        nodes.append(initial_node)
        counter = 0
        while not nodes[0].check_is_goal(self.data):
            if (nodes[0].can_move(self.data, 'right')):
                nodes.append(nodes[0].make_child_node_with_weight('right', self.data, self.princess_position))
            if(nodes[0].can_move(self.data, 'up')):
                nodes.append(nodes[0].make_child_node_with_weight('up', self.data, self.princess_position))
            if (nodes[0].can_move(self.data, 'left')):
                nodes.append(nodes[0].make_child_node_with_weight('left', self.data, self.princess_position))
            if (nodes[0].can_move(self.data, 'down')):
                nodes.append(nodes[0].make_child_node_with_weight('down', self.data, self.princess_position))
            nodes.pop(0)
            nodes.sort(key=lambda x: x.heuristic)
            counter += 1
        algorithm_data = {
            'name': 'Avaro',
            'nodos_expandidos': counter,
            'nodos_creados': counter + len(nodes),
            'tiempo_de_ejecucion': "%s" % (time.time() - start_time)
        }
        self.show_route(nodes[0].get_fathers(), algorithm_data)

    def estrella(self):
        print("estrella")
        start_time = time.time()
        nodes = []
        initial_node = Node(self.mario_position, None)
        nodes.append(initial_node)
        counter = 0
        while not nodes[0].check_is_goal(self.data):
            if (nodes[0].can_move(self.data, 'right')):
                nodes.append(nodes[0].make_child_node_with_weight('right', self.data, self.princess_position))
            if(nodes[0].can_move(self.data, 'up')):
                nodes.append(nodes[0].make_child_node_with_weight('up', self.data, self.princess_position))
            if (nodes[0].can_move(self.data, 'left')):
                nodes.append(nodes[0].make_child_node_with_weight('left', self.data, self.princess_position))
            if (nodes[0].can_move(self.data, 'down')):
                nodes.append(nodes[0].make_child_node_with_weight('down', self.data, self.princess_position))
            nodes.pop(0)
            nodes.sort(key=lambda x: x.weight_and_heuristic)
            counter += 1
        algorithm_data = {
            'name': 'A*',
            'nodos_expandidos': counter,
            'nodos_creados': counter + len(nodes),
            'tiempo_de_ejecucion': "%s" % (time.time() - start_time)
        }
        self.show_route(nodes[0].get_fathers(), algorithm_data)

    def show_route(self, nodes, data):

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
            if nodes:
                if nodes[0].flor:
                    self.frame.blit(self.mario_flor, (50 * nodes[0].position[1], 50 * nodes[0].position[0]))
                else:
                    self.frame.blit(self.mario, (50 * nodes[0].position[1], 50 * nodes[0].position[0]))
                pygame.display.update()
                pygame.time.delay(1500)
                nodes.pop(0)
            else:
                break
        self.game_finish(data)

    def game_finish(self, data):
        intro = True

        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == 27:  # Tecla ESC
                        pygame.quit()
                        quit()
                    else:
                        self.game_intro()

            # Se Pinta la pantalla en blanco
            self.frame.fill((255, 255, 255))

            # Se crea las fuentes para el menú
            font_title_menu = pygame.font.Font(None, 50)
            font_menu = pygame.font.Font(None, 30)

            # Se crean los mensajes
            title_menu = "Mario-Smart"
            text_menu_1 = "{0}".format(data['name'])
            text_menu_2 = "Nodos expandidos {0}".format(str(data['nodos_expandidos']))
            text_menu_3 = "Nodos creados {0}".format(str(data['nodos_creados']))
            text_menu_4 = "Tiempo de ejecución {0}".format(str(data['tiempo_de_ejecucion']))
            text_menu_8 = "Presione cualquier tecla para continuar \n y 'ESC' para salir"

            # Se aplican las fuentes
            menu_1 = font_title_menu.render(title_menu, 1, (255, 0, 0))
            menu_2 = font_menu.render(text_menu_1, 1, (0, 0, 0))
            menu_3 = font_menu.render(text_menu_2, 1, (0, 0, 0))
            menu_4 = font_menu.render(text_menu_3, 1, (0, 0, 0))
            menu_5 = font_menu.render(text_menu_4, 1, (0, 0, 0))
            menu_9 = font_menu.render(text_menu_8, 1, (0, 0, 0))

            # Se pintan en pantalla
            self.frame.blit(menu_1, (150, 10))
            self.frame.blit(menu_2, (15, 63))
            self.frame.blit(menu_3, (40, 100))
            self.frame.blit(menu_4, (40, 140))
            self.frame.blit(menu_5, (40, 180))
            self.frame.blit(menu_9, (15, 360))

            pygame.display.update()
Main()
