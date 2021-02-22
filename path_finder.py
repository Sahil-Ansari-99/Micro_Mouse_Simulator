import API
import sys
from utils import get_visited, get_front, get_left, get_right, get_opposite_direction
from queue import Queue


class PathFinder:
    def __init__(self):
        self.maze = list()
        self.maze_weight = list()
        self.MAZE_WIDTH = API.mazeWidth()
        self.MAZE_HEIGHT = API.mazeHeight()
        self.BOT_DIRECTION = 0  # default upwards
        self.curr_x = 0
        self.curr_y = 0
        self.drs = [1, 0, -1, 0]
        self.dcs = [0, 1, 0, -1]
        self.initialize_maze()

    def initialize_maze(self):
        for i in range(self.MAZE_HEIGHT):
            temp = list()
            weight_temp = list()
            for j in range(self.MAZE_WIDTH):
                walls = list()
                weight_temp.append(0)
                for k in range(4):
                    walls.append(0)
                temp.append(walls)
            self.maze.append(temp)
            self.maze_weight.append(weight_temp)

    def log(self, string):
        sys.stderr.write("{}\n".format(string))
        sys.stderr.flush()

    def is_valid(self, x, y):
        return 0 <= x < self.MAZE_WIDTH and 0 <= y < self.MAZE_HEIGHT

    def flood_fill(self):
        q = Queue()
        # end positions
        q.put((7, 7))
        q.put((7, 8))
        q.put((8, 7))
        q.put((8, 8))
        visited = get_visited(self.MAZE_WIDTH, self.MAZE_HEIGHT)
        visited[7][7] = True
        visited[7][8] = True
        visited[8][7] = True
        visited[8][8] = True
        while not q.empty():
            size = q.qsize()
            for k in range(size):
                x, y = q.get()
                for i in range(len(self.drs)):
                    new_x = x + self.dcs[i]
                    new_y = y + self.drs[i]
                    if self.is_valid(new_x, new_y) and not visited[new_x][new_y] and self.maze[x][y][i] != 1:
                        visited[new_x][new_y] = True
                        self.maze_weight[new_x][new_y] = self.maze_weight[x][y] + 1
                        API.setText(new_x, new_y, str(self.maze_weight[new_x][new_y]))
                        q.put((new_x, new_y))

    def update_maze(self, front_wall, right_wall, left_wall):
        if front_wall:
            front = get_front(self.BOT_DIRECTION)
            self.set_wall(self.curr_x, self.curr_y, front)
            self.maze[self.curr_x][self.curr_y][front] = 1
            self.mark_opposite_wall(self.curr_x, self.curr_y, front)
        if right_wall:
            right = get_right(self.BOT_DIRECTION)
            self.set_wall(self.curr_x, self.curr_y, right)
            self.maze[self.curr_x][self.curr_y][right] = 1
            self.mark_opposite_wall(self.curr_x, self.curr_y, right)
        if left_wall:
            left = get_left(self.BOT_DIRECTION)
            self.set_wall(self.curr_x, self.curr_y, left)
            self.maze[self.curr_x][self.curr_y][left] = 1
            self.mark_opposite_wall(self.curr_x, self.curr_y, left)

    def mark_opposite_wall(self, x, y, direction):
        opposite = get_opposite_direction(direction)
        new_x = x + self.dcs[direction]
        new_y = y + self.drs[direction]
        if self.is_valid(new_x, new_y):
            self.maze[new_x][new_y][opposite] = 1

    def get_next_move(self):
        self.flood_fill()
        new_direction = self.BOT_DIRECTION
        curr_score = self.maze_weight[self.curr_x][self.curr_y]
        best_x = self.curr_x
        best_y = self.curr_y
        for i in range(len(self.drs)):
            new_x = self.curr_x + self.dcs[i]
            new_y = self.curr_y + self.drs[i]
            if self.maze[self.curr_x][self.curr_y][i] != 1 and self.maze_weight[new_x][new_y] < curr_score:
                curr_score = self.maze_weight[new_x][new_y]
                new_direction = i
                best_x = new_x
                best_y = new_y
        self.update_position(best_x, best_y, new_direction)
        return new_direction

    def update_position(self, x, y, direction):
        self.BOT_DIRECTION = direction
        # self.log('Curr X:' + str(self.curr_x) + ' ' + 'New X:' + str(x))
        self.curr_x = x
        self.curr_y = y

    def is_end(self):
        return self.maze_weight[self.curr_x][self.curr_y] == 0

    def set_wall(self, x, y, direction):
        # self.log('Setting wall:' + '(' + str(x) + ',' + str(y) + ') ' + str(direction))
        if direction == 0:
            API.setWall(x, y, 'n')
        elif direction == 1:
            API.setWall(x, y, 'e')
        elif direction == 2:
            API.setWall(x, y, 's')
        else:
            API.setWall(x, y, 'w')

    def print_maze(self):
        s = ''
        for i in range(self.MAZE_HEIGHT):
            for j in range(self.MAZE_WIDTH):
                s += str(self.maze_weight[i][j])
                s += ' '
            s += '\n'
        return s


# maze = list()
# maze_weight = list()
# MAZE_WIDTH = API.mazeWidth()
# MAZE_HEIGHT = API.mazeHeight()
# BOT_DIRECTION = 0  # default upwards
#
# for i in range(MAZE_HEIGHT):
#     temp = list()
#     weight_temp = list()
#     for j in range(MAZE_WIDTH):
#         walls = list()
#         weight_temp.append(0)
#         for k in range(4):
#             walls.append(0)
#         temp.append(walls)
#     maze.append(temp)
#     maze_weight.append(weight_temp)
#
# curr_x = 0
# curr_y = 0
#
#
# drs = [1, 0, -1, 0]
# dcs = [0, 1, 0, -1]
#
#
# def log(string):
#     sys.stderr.write("{}\n".format(string))
#     sys.stderr.flush()
#
#
# def is_valid(x, y):
#     return 0 <= x < MAZE_WIDTH and 0 <= y < MAZE_HEIGHT
#
#
# def flood_fill():
#     global maze
#     q = Queue()
#     # end positions
#     q.put((7, 7))
#     q.put((7, 8))
#     q.put((8, 7))
#     q.put((8, 8))
#     visited = get_visited(MAZE_WIDTH, MAZE_HEIGHT)
#     visited[7][7] = True
#     visited[7][8] = True
#     visited[8][7] = True
#     visited[8][8] = True
#
#     while not q.empty():
#         size = q.qsize()
#         for k in range(size):
#             x, y = q.get()
#             for i in range(len(drs)):
#                 new_x = x + dcs[i]
#                 new_y = y + drs[i]
#                 if is_valid(new_x, new_y) and not visited[new_x][new_y] and maze[x][y][i] != 1:
#                     visited[new_x][new_y] = True
#                     maze_weight[new_x][new_y] = maze_weight[x][y] + 1
#                     API.setText(new_x, new_y, str(maze_weight[new_x][new_y]))
#                     q.put((new_x, new_y))
#
#
# def update_maze():
#     global maze
#     if API.wallFront():
#         front = get_front(BOT_DIRECTION)
#         maze[curr_x][curr_y][front] = 1
#         mark_opposite_wall(curr_x, curr_y, front)
#     if API.wallRight():
#         right = get_right(BOT_DIRECTION)
#         maze[curr_x][curr_y][right] = 1
#         mark_opposite_wall(curr_x, curr_y, right)
#     if API.wallLeft():
#         left = get_left(BOT_DIRECTION)
#         maze[curr_x][curr_y][get_left(BOT_DIRECTION)] = 1
#         mark_opposite_wall(curr_x, curr_y, left)
#
#
# def mark_opposite_wall(x, y, direction):
#     opposite = get_opposite_direction(direction)
#     new_x = x + dcs[direction]
#     new_y = y + drs[direction]
#     if is_valid(new_x, new_y):
#         maze[new_x][new_y][opposite] = 1
#
#
# def get_next_move():
#     flood_fill()
#     new_direction = BOT_DIRECTION
#     curr_score = maze_weight[curr_x][curr_y]
#     best_x = 0
#     best_y = 0
#     for i in range(len(drs)):
#         new_x = curr_x + drs[i]
#         new_y = curr_y + dcs[i]
#         if maze[curr_x][curr_y][i] != 1 and maze_weight[new_x][new_y] < curr_score:
#             curr_score = maze_weight[new_x][new_y]
#             new_direction = i
#             best_x = new_x
#             best_y = new_y
#     update_position(best_x, best_y, new_direction)
#     return new_direction
#
#
# def update_position(x, y, direction):
#     global curr_x, curr_y, BOT_DIRECTION
#     BOT_DIRECTION = direction
#     curr_x = x
#     curr_y = y
#
#
# def is_end():
#     global curr_x, curr_y
#     return maze_weight[curr_x][curr_y] == 0
#
#
# def print_maze():
#     s = ''
#     for i in range(MAZE_HEIGHT):
#         for j in range(MAZE_WIDTH):
#             s += str(maze_weight[i][j])
#             s += ' '
#         s += '\n'
#     return s
