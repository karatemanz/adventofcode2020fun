import os

OPEN_SLOPE = '.'
TREE_ON_SLOPE = '#'
OPEN = 'O'
TREE = 'X'
PWD = os.path.dirname(os.path.abspath(__file__))

def multiply_list(myList) :
    # Multiply elements one by one
    result = 1
    for x in myList:
            result = result * x
    return result

def show_slopes(running_path):
    recombine_path = []
    for i in running_path:
        recombine_path.append("".join(i))

    final_path = "\n".join(recombine_path)
    print(final_path)

def traverse(current_x, current_y, field, move_right, move_down):
    hit_tree = False
    #print(f'Current Coord: ({current_y}, {current_x}) - {field[current_y][current_x]}')

    new_x = (current_x + move_right) % (len(field[current_x]))
    new_y = (current_y + move_down)

    if (field[new_y][new_x] == TREE_ON_SLOPE):
        field[new_y][new_x] = TREE
        hit_tree = True
    else:
        field[new_y][new_x] = OPEN

    #print(f'New Coord   : ({new_y}, {new_x}) - {field[new_y][new_x]}')
    return (new_x, new_y, field, hit_tree)

def hit_the_slopes(x_rate, y_rate):
    path = os.path.join(PWD, 'toboggan-field.txt')
    toboggan_array = open(path, "r").read().split('\n')
    # remove trailing path
    toboggan_array = toboggan_array[:-1]

    toboggan_path = []

    for plane in toboggan_array:
        toboggan_path.append(list(plane))

    running_path = toboggan_path
    x = initial_position_x = 0
    y = initial_position_y = 0

    open_position_count = 0
    tree_position_count = 0

    while (y < (len(toboggan_path)-1)):
        (x, y, running_path, hit_tree) = traverse(x, y, toboggan_path, x_rate, y_rate)
        if (hit_tree):
            tree_position_count += 1
        else:
            open_position_count += 1

    print(f'Rate            : ({x_rate}, {y_rate})')
    print(f'Dimensions      : {len(toboggan_path[x])-1}, {len(toboggan_path)-1}')
    print(f'Tree encounters : {tree_position_count}!')
    print(f'Open encounters : {open_position_count}!')
    print(f'Total encounters: {tree_position_count + open_position_count} (Should be: {len(toboggan_path)-1})!')
    # To see the output post-run
    #show_slopes(running_path)
    return (tree_position_count, open_position_count)

ratelist = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
slope_hit_list = map((lambda t: hit_the_slopes(t[0], t[1])), ratelist)
tree_hit_list = map(lambda t: t[0], list(slope_hit_list))
result = multiply_list(list(tree_hit_list))

print(f'Product of hits: {result}')