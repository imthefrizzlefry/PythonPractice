'''This problem was asked by Google.

You are given an M by N matrix consisting of booleans that represents a board. Each True boolean represents a wall. Each False boolean represents a tile you can walk on.

Given this matrix, a start coordinate, and an end coordinate, return the minimum number of steps required to reach the end coordinate from the start. If there is no possible path, then return null. You can move up, left, down, and right. You cannot move through walls. You cannot wrap around the edges of the board.

For example, given the following board:

[[f, f, f, f],
[t, t, f, t],
[f, f, f, f],
[f, f, f, f]]
and start = (3, 0) (bottom left) and end = (0, 0) (top left), the minimum number of steps required to reach the end is 7, since we would need to go through (1, 2) because there is a wall everywhere else on the second row.
'''

# I added a method to create a visualization grid so I could explore optimizing my solution visually
def create_vis_grid(m,n, ref_grid=None):
    grid = []
    for y in range(m):
        grid.append([])

        for x in range(n):
            if ref_grid is not None and ref_grid[y][x]:
                grid[y].append("#")
            else:
                grid[y].append(" ")

    return grid

# A method just to print the grid to the screen
def visualize_history(step, grid, counter=None):
    grid[step[0]][step[1]] = "*"
    #print top grid border
    print(" ", end="")
    for column in grid[0]:
        print(" - ", end="")
    print("", end="\n")

    
    for row in grid:
        print("|", end="")
        for cell in row:
            print("{:^3}".format(cell), end="")
        print("|", end="\n")

    # print bottom grid border
    print(" ", end="")
    for column in grid[0]:
        print(" - ", end="")
    print("", end="\n")
    if counter is not None:
        print(counter, end="\n")


# Begin implementation

# I used a heapq so my algorithm could prioritize going directly to the destination
import heapq

def take_a_step(start, step_num, memory, m, n, grid):
    # the set of potential moves: Up, Down, Left, Right
    move_options = [(1,0), (-1,0), (0,-1), (0,1)]
    # create a queue to contian valid moves
    queue = []

    for move in move_options:
        # find new position of a potential move
        new = (start[0] + move[0], start[1] + move[1])
        
        # if the new move is outside the grid boundaries, then skip it
        if new[0] < 0 or new[0] >= m:
            continue
        if new[1] < 0 or new[1] >= n:
            continue

        # if we have never evaluated that spot before, and that spot is not a wall
        if new not in memory and grid[new[0]][new[1]] == False:
            # add the new coordinate and number of steps to the queue
            queue.append((new, step_num))
            # add the step to the memory, to avoid duplicates
            memory[new] = step_num

    # return the queue of valid new moves for prioritization
    return queue



def navigate_grid(start, end, grid, visualize=True):
    
    # use a dictionary to prevent visiting the same cell more than once
    memory = {start:0}
    
    # Create a queue of position I need to visit, will be used in conjuntion with the heapq
    # will contain a touple of (int: distance_to_end, (tuple: position_coordinates, int: move_number))
    step_queue = []
    
    # these are used to detect right and bottom edges of the grid
    m = len(grid)
    n = len(grid[0])

    # this distance is computed for every move, and used to prioritize the queue
    dist = abs(start[0] - end[0]) + abs(start[1] - end[1])

    # create the visualization grid, and mark the start and end positions
    vis_grid = create_vis_grid(m,n, grid)
    vis_grid[start[0]][start[1]] = "S"
    vis_grid[end[0]][end[1]] = "X"
    # counter is also just used for visualization...
    counter = 0

    # push the starting point to the queue, distance isn't important for this because it's always the first item to pop
    # setp is also not important here, but it makes the loop a little cleaner 
    heapq.heappush(step_queue, (dist, (start, 0)))

    while end not in memory and step_queue:
        # pop the element in the heapqueue closest to end, then strip the distance
        # cur = ((cur_y, cur_x), step)
        cur = heapq.heappop(step_queue)[1]
        
        # print grid to screen if not the starting point
        if visualize and cur[0] != start:
            visualize_history(cur[0], vis_grid, counter)

        # generate the possible moves
        temp_queue = take_a_step(cur[0], cur[1]+1, memory, m, n, grid)

        # calculate distance for each possible move, then push to heapq, using shortest distance to prioritize
        for step in temp_queue:
            dist = abs(step[0][0] - end[0]) + abs(step[0][1] - end[1])
            heapq.heappush(step_queue, (dist, step))

        #increment counter (used to visualize the algorithms efficiency)
        counter += 1

    # if I exhaust the list of steps, then there is no path the destination
    if not step_queue:
        return None

    return memory[end]


my_start = (11, 4)
my_end = (0,0)
my_grid = [
    [False, False, False, False, False, False, False, False, False], 
    [True,   True,  True,  True,   True,  True,  True, True, False], 
    [False, False, False, False, False, False, False,  True, False],
    [False,  True,  True,  True,  True,  True, False,  True, False],
    [False,  True, False, False, False,  True, False,  True, False],
    [False,  True, False, False, False,  True, False,  True, False], 
    [False,  True, False, False, False,  True, False,  True, False], 
    [False,  True, False, False, False,  True, False,  True, False], 
    [False,  True, False, False, False,  True, False,  True, False], 
    [False,  True, False, False, False,  True, False,  True, False], 
    [False,  True, False, False, False,  True, False,  True, False], 
    [False,  True, False, False, False,  True, False,  True, False], 
    [False,  True, False, False, False, False, False,  True, False], 
    [False,  True,  True,  True,  True,  True,  True,  True, False], 
    [False, False, False, False, False, False, False, False, False]]

print(navigate_grid(my_start, my_end, my_grid, visualize=False))


my_start = (3, 0)
my_end = (0,0)
my_grid =[[False, False, False, False],
[True, True, True, True],
[False, False, False, False],
[False, False, False, False]]

print(navigate_grid(my_start, my_end, my_grid))