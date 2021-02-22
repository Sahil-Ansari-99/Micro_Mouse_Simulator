

def get_visited(width, height):
    visited = list()
    for i in range(width):
        temp = list()
        for j in range(height):
            temp.append(False)
        visited.append(temp)
    return visited


def get_front(direction):
    if direction == 0:  # bot pointing upwards
        return 0
    elif direction == 1:  # bot pointing rightwards
        return 1
    elif direction == 2:  # bot pointing downwards
        return 2
    return 3  # bot pointing leftwards


def get_right(direction):
    if direction == 0:
        return 1
    elif direction == 1:
        return 2
    elif direction == 2:
        return 3
    return 0


def get_left(direction):
    if direction == 0:
        return 3
    elif direction == 1:
        return 0
    elif direction == 2:
        return 1
    return 2


def get_direction(curr_direction, new_direction):
    if curr_direction == new_direction:
        return None
    if curr_direction == 0:
        if new_direction == 1:
            return 'right'
        elif new_direction == 2:
            return 'down'
        else:
            return 'left'
    elif curr_direction == 1:
        if new_direction == 2:
            return 'right'
        elif new_direction == 3:
            return 'down'
        else:
            return 'left'
    elif curr_direction == 2:
        if new_direction == 3:
            return 'right'
        elif new_direction == 0:
            return 'down'
        else:
            return 'left'
    else:
        if new_direction == 0:
            return 'right'
        elif new_direction == 1:
            return 'down'
        else:
            return 'left'


def get_opposite_direction(direction):
    if direction == 0:
        return 2
    elif direction == 1:
        return 3
    elif direction == 2:
        return 0
    return 1
