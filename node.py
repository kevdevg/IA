import sys


class Node:

    def __init__(self, position, adversary, father, state, type, max_points, min_points):
        self.position = position
        self.adversary = adversary
        self.father = father
        self.state = state
        self.type = type
        if not self.type:
            self.value = sys.maxsize
        else:
            self.value = -sys.maxsize
        self.is_expand = False
        self.move = None
        self.best_move = None
        self.max_points = max_points
        self.min_points = min_points

    def play(self):
        construction = True
        tree = [self]
        best_move = None
        best_score = 0
        final_tree = []
        while construction:
            if tree[0].is_expand:
                final_tree.insert(0, tree[0])
                tree.remove(tree[0])
                if not len(tree):
                    construction = False
            else:
                if(tree[0].position in tree[0].state):
                    tree[0].state.remove(tree[0].position)
                    if(tree[0].type):
                        tree[0].max_points += 1
                    else:
                        tree[0].min_points += 1
                tree[0].is_expand = True
                if(len(tree[0].state)):
                    for node in tree[0].get_moves():
                        tree.insert(0, Node(tree[0].adversary, node, tree[0], tree[0].state, not tree[0].type))
        print(len(final_tree))

    def get_moves(self):
        moves = []
        moves.append((self.position[0] - 2, self.position[1] - 1))
        moves.append((self.position[0] - 2, self.position[1] + 1))
        moves.append((self.position[0] + 2, self.position[1] - 1))
        moves.append((self.position[0] + 2, self.position[1] + 1))
        moves.append((self.position[0] - 1, self.position[1] - 2))
        moves.append((self.position[0] + 1, self.position[1] - 2))
        moves.append((self.position[0] - 1, self.position[1] + 2))
        moves.append((self.position[0] + 1, self.position[1] + 2))
        true_moves = []
        for move in moves:
            if (move[0] >= 0 and move[0] <= 5 and move[1] >= 0 and move[1] <= 5):
                true_moves.append(move)
        if self.adversary in moves:
            true_moves.remove(self.adversary)
        if self.father and self.father.position in moves:
            true_moves.remove(self.father.position)
        return true_moves
