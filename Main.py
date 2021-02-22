#! python3
import API
import sys
from path_finder import PathFinder
from utils import get_direction


def log(string):
    sys.stderr.write("{}\n".format(string))
    sys.stderr.flush()


def main():
    log("Running...")
    API.setColor(0, 0, "G")
    API.setText(0, 0, "abc")
    bot_direction = 0
    path_finder = PathFinder()
    while True:
        path_finder.update_maze(API.wallFront(), API.wallRight(), API.wallLeft())
        move = path_finder.get_next_move()
        direction = get_direction(bot_direction, move)
        if direction == 'right':
            API.turnRight()
        elif direction == 'left':
            API.turnLeft()
        elif direction == 'down':
            API.turnLeft()
            API.turnLeft()
        # if direction is not None:
        #     log(str(bot_direction) + ' ' + str(move) + ' ' + direction)
        bot_direction = move
        API.moveForward()
        if path_finder.is_end():
            break
    log('Completed')
    log('Score:' + str(API.getStat('total-distance')))


if __name__ == "__main__":
    main()
