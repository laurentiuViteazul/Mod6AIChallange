from typing import Union, Iterable

from numpy import Infinity

from gameobjects import GameObject
from move import Move, Direction
import numpy as np


class Node:
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.f = 0
        self.h = 0

    def __eq__(self, other):
        return self.position == other.position


class Agent:

    def __init__(self):
        self.maze = []
        self.cost = 1
        self.board_width = None
        self.board_height = None
        self.steps_done = 0
        """" Constructor of the Agent, can be used to set up variables """

    def get_move(self, board, score, turns_alive, turns_to_starve, direction, head_position, body_parts):
        # for i in range(0, 25):
        #     for j in range(0, 25):
        self.path = self.search(self.cost, self.start, self.end)
        total_steps = -2
        for i in range(0, self.board_width):
            for j in range(0, self.board_height):
                if self.path[i][j] > total_steps:
                    total_steps = self.path[i][j]
        dir = self.find_direction_from_path(direction, total_steps)
        print("path = "+str(self.path))
        #         print("i = "+str(i)+"; j = "+str(j)+"; "+str(board[i][j]))
        """This function behaves as the 'brain' of the snake. You only need to change the code in this function for
        the project. Every turn the agent needs to return a move. This move will be executed by the snake. If this
        functions fails to return a valid return (see return), the snake will die (as this confuses its tiny brain
        that much that it will explode). The starting direction of the snake will be North.

        :param board: A two dimensional array representing the current state of the board. The upper left most
        coordinate is equal to (0,0) and each coordinate (x,y) can be accessed by executing board[x][y]. At each
        coordinate a GameObject is present. This can be either GameObject.EMPTY (meaning there is nothing at the
        given coordinate), GameObject.FOOD (meaning there is food at the given coordinate), GameObject.WALL (meaning
        there is a wall at the given coordinate. TIP: do not run into them), GameObject.SNAKE_HEAD (meaning the head
        of the snake is located there) and GameObject.SNAKE_BODY (meaning there is a body part of the snake there.
        TIP: also, do not run into these). The snake will also die when it tries to escape the board (moving out of
        the boundaries of the array)

        :param score: The current score as an integer. Whenever the snake eats, the score will be increased by one.
        When the snake tragically dies (i.e. by running its head into a wall) the score will be reset. In ohter
        words, the score describes the score of the current (alive) worm.

        :param turns_alive: The number of turns (as integer) the current snake is alive.

        :param turns_to_starve: The number of turns left alive (as integer) if the snake does not eat. If this number
        reaches 1 and there is not eaten the next turn, the snake dies. If the value is equal to -1, then the option
        is not enabled and the snake can not starve.

        :param direction: The direction the snake is currently facing. This can be either Direction.NORTH,
        Direction.SOUTH, Direction.WEST, Direction.EAST. For instance, when the snake is facing east and a move
        straight is returned, the snake wil move one cell to the right.

        :param head_position: (x,y) of the head of the snake. The following should always hold: board[head_position[
        0]][head_position[1]] == GameObject.SNAKE_HEAD.

        :param body_parts: the array of the locations of the body parts of the snake. The last element of this array
        represents the tail and the first element represents the body part directly following the head of the snake.

        :return: The move of the snake. This can be either Move.LEFT (meaning going left), Move.STRAIGHT (meaning
        going straight ahead) and Move.RIGHT (meaning going right). The moves are made from the viewpoint of the
        snake. This means the snake keeps track of the direction it is facing (North, South, West and East).
        Move.LEFT and Move.RIGHT changes the direction of the snake. In example, if the snake is facing north and the
        move left is made, the snake will go one block to the left and change its direction to west.
        """


        return Move.LEFT

    def create_maze_from_board(self, board, board_width, board_height):
        self.start = []
        self.end = []
        self.board_width = board_width
        self.board_height = board_height
        for i in range(0, board_width):
            row = []
            for j in range(0, board_height):
                if(board[i][j] == GameObject.EMPTY):
                    row.append(0)
                elif(board[i][j] == GameObject.WALL or board[i][j] == GameObject.SNAKE_BODY): #or  or board[i][j] == GameObject.SNAKE_HEAD
                    row.append(1)
                elif(board[i][j] == GameObject.SNAKE_HEAD):
                    self.start = (i, j)
                elif(board[i][j] == GameObject.FOOD):
                    self.end = (i, j)
            self.maze.append(row)
        print(self.start, self.end)
        print(self.maze)

    def find_directions_from_path(self, direction, total_steps):
        current = self.steps_done




        return None

    def look_for_next_step(self, current_step):
        location = ()
        for i in range(0, self.board_width):
            for j in range(0, self.board_height):
                if self.path[i][j] == (current_step+1):
                    location = (i, j)




    def return_path(self, current_node):
        path = []
        no_rows, no_columns = (self.board_width, self.board_height)
        # here we create the initialized result maze with -1 in every position
        result = [[-1 for i in range(no_columns)] for j in range(no_rows)]
        current = current_node
        while current is not None:
            path.append(current.position)
            current = current.parent
        # Return reversed path as we need to show from start to end path
        path = path[::-1]
        start_value = 0
        # we update the path of start to end found by A-star serch with every step incremented by 1
        for i in range(len(path)):
            result[path[i][0]][path[i][1]] = start_value
            start_value += 1
        return result

    def search(self, cost, start, end):
        print("Inside search, maze = "+str(self.maze))
        # """
        #     Returns a list of tuples as a path from the given start to the given end in the given maze
        #     :param maze:
        #     :param cost
        #     :param start:
        #     :param end:
        #     :return:
        # """
        # test = [[0,0,1],
        #         [1,0,0],
        #         [1,0,0],
        #         [0,0,1]]
        # no_r = no_c = np.shape(test)
        # print("no_r = "+str(no_r)+"; no_c = "+str(no_c))
        # Create start and end node with initized values for g, h and f
        start_node = Node(None, tuple(start))
        start_node.g = start_node.h = start_node.f = 0
        end_node = Node(None, tuple(end))
        end_node.g = end_node.h = end_node.f = 0

        # Initialize both yet_to_visit and visited list
        # in this list we will put all node that are yet_to_visit for exploration.
        # From here we will find the lowest cost node to expand next
        yet_to_visit_list = []
        # in this list we will put all node those already explored so that we don't explore it again
        visited_list = []

        # Add the start node
        yet_to_visit_list.append(start_node)

        # Adding a stop condition. This is to avoid any infinite loop and stop
        # execution after some reasonable number of steps
        outer_iterations = 0
        max_iterations = (len(self.maze) // 2) ** 10

        # what squares do we search . serarch movement is left-right-top-bottom
        # (4 movements) from every positon

        move = [[-1, 0],  # go up
                [0, -1],  # go left
                [1, 0],  # go down
                [0, 1]]  # go right
        # find maze has got how many rows and columns
        no_rows, no_columns = (self.board_width, self.board_height)

        # Loop until you find the end

        while len(yet_to_visit_list) > 0:
            # Every time any node is referred from yet_to_visit list, counter of limit operation incremented
            outer_iterations += 1
            print("in while loop")
            # Get the current node
            current_node = yet_to_visit_list[0]
            current_index = 0
            for index, item in enumerate(yet_to_visit_list):
                if item.f < current_node.f:
                    current_node = item
                    current_index = index

            # if we hit this point return the path such as it may be no solution or
            # computation cost is too high
            if outer_iterations > max_iterations:
                print("giving up on pathfinding too many iterations")
                return self.return_path(current_node)

            # Pop current node out off yet_to_visit list, add to visited list
            yet_to_visit_list.pop(current_index)
            visited_list.append(current_node)

            # test if goal is reached or not, if yes then return the path
            if current_node == end_node:
                return self.return_path(current_node)

            # Generate children from all adjacent squares
            children = []

            for new_position in move:

                # Get node position
                node_position = (
                current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

                # Make sure within range (check if within maze boundary)
                if (node_position[0] > (no_rows - 1) or
                        node_position[0] < 0 or
                        node_position[1] > (no_columns - 1) or
                        node_position[1] < 0):
                    continue

                # Make sure walkable terrain
                if self.maze[node_position[0]][node_position[1]] != 0:
                    continue

                # Create new node
                new_node = Node(current_node, node_position)

                # Append
                children.append(new_node)

            # Loop through children
            for child in children:

                # Child is on the visited list (search entire visited list)
                if len([visited_child for visited_child in visited_list if visited_child == child]) > 0:
                    continue

                # Create the f, g, and h values
                child.g = current_node.g + cost
                ## Heuristic costs calculated here, this is using eucledian distance
                child.h = (((child.position[0] - end_node.position[0]) ** 2) +
                           ((child.position[1] - end_node.position[1]) ** 2))

                child.f = child.g + child.h

                # Child is already in the yet_to_visit list and g cost is already lower
                if len([i for i in yet_to_visit_list if child == i and child.g > i.g]) > 0:
                    continue

                # Add the child to the yet_to_visit list
                yet_to_visit_list.append(child)

    def should_redraw_board(self):
        """
        This function indicates whether the board should be redrawn. Not drawing to the board increases the number of
        games that can be played in a given time. This is especially useful if you want to train you agent. The
        function is called before the get_move function.

        :return: True if the board should be redrawn, False if the board should not be redrawn.
        """
        return True

    def should_grow_on_food_collision(self):
        """
        This function indicates whether the snake should grow when colliding with a food object. This function is
        called whenever the snake collides with a food block.

        :return: True if the snake should grow, False if the snake should not grow
        """
        return True

    def on_die(self, head_position, board, score, body_parts):
        """This function will be called whenever the snake dies. After its dead the snake will be reincarnated into a
        new snake and its life will start over. This means that the next time the get_move function is called,
        it will be called for a fresh snake. Use this function to clean up variables specific to the life of a single
        snake or to host a funeral.

        :param head_position: (x, y) position of the head at the moment of dying.

        :param board: two dimensional array representing the board of the game at the moment of dying. The board
        given does not include information about the snake, only the food position(s) and wall(s) are listed.

        :param score: score at the moment of dying.

        :param body_parts: the array of the locations of the body parts of the snake. The last element of this array
        represents the tail and the first element represents the body part directly following the head of the snake.
        When the snake runs in its own body the following holds: head_position in body_parts.
        """
