class Node:

    def __str__(self):
        return "{0},{1}".format(self.x, self.y)

    def __init__(self, position, father):
        self.position = position
        self.father = father
        self.weight = 0
        if father and father.flor:
            self.flor = True
        else:
            self.flor = False

    def check_is_goal(self, world):
        return world[self.position[0]][self.position[1]] == 5

    def can_move(self, world, direction):
        if direction == 'up':
            if self.father and (self.position[0]-1, self.position[1]) == self.father.position:
                return False
            return self.position[0] != 0 and world[self.position[0]-1][self.position[1]] != 1
        elif direction == 'down':
            if self.father and (self.position[0]+1, self.position[1]) == self.father.position:
                return False
            return self.position[0] != 9 and world[self.position[0]+1][self.position[1]] != 1
        elif direction == 'left':
            if self.father and (self.position[0], self.position[1]-1) == self.father.position:
                return False
            return self.position[1] != 0 and world[self.position[0]][self.position[1]-1] != 1
        elif direction == 'right':
            if self.father and (self.position[0], self.position[1]+1) == self.father.position:
                return False
            return self.position[1] != 9 and world[self.position[0]][self.position[1]+1] != 1
        else:
            raise AttributeError

    def make_child_node(self, direction):
        if direction == 'up':
            node = Node((self.position[0]-1, self.position[1]), self)
        elif direction == 'down':
            node = Node((self.position[0] + 1, self.position[1]), self)
        elif direction == 'left':
            node = Node((self.position[0], self.position[1]-1), self)
        elif direction == 'right':
            node = Node((self.position[0], self.position[1]+1), self)
        else:
            raise AttributeError
        node.father = self
        return node

    def make_child_node_with_weight(self, direction, world, princess):
        if direction == 'up':
            node = Node((self.position[0]-1, self.position[1]), self)
        elif direction == 'down':
            node = Node((self.position[0] + 1, self.position[1]), self)
        elif direction == 'left':
            node = Node((self.position[0], self.position[1]-1), self)
        elif direction == 'right':
            node = Node((self.position[0], self.position[1]+1), self)
        else:
            raise AttributeError

        if world[node.position[0]][node.position[1]] == 4 and not node.flor:
            peso = 7
        elif world[node.position[0]][node.position[1]] == 3:
            node.flor = True
            peso = 1
        else:
            peso = 1

        node.weight = peso + node.father.weight
        node.heuristic_function(princess)
                
        return node

    def get_fathers(self):
        fathers = []
        actual_node = self
        fathers.insert(0, actual_node)
        while actual_node.father:
            fathers.insert(0, actual_node.father)
            actual_node = actual_node.father
        return fathers

    def heuristic_function(self, princess):
        if princess:
            self.heuristic = abs(princess[0]-self.position[0]) + abs(princess[1]-self.position[1])
            self.weight_and_heuristic = self.weight + self.heuristic
