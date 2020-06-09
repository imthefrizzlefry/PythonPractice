''' Asked by an ex-Googler in a practice interview

Go chess

19*19 board

You hold white stones; and i hold black stones

W w
W B w
W w

Black stone at (1,1) -> dead

W w w
W B _  w
W w w

    w w
W b b _
   W w b

    w w
W b w w
   W b b

   b
B b b
   b

Black stones: dead

isDead(board, position)  // true if dead; false if alive
'''
memory = {} # key tuple, val True


def build_empty_board(size=19):
    board = []
    for r in range(size):
        board.append([])

        for c in range(size):
            board[r].append("")
    return board

def look_direction(board, cur, desire):
    if board[cur[0]] [cur[1]] != desire:	
        if board[cur[0]] [cur[1]] == "":
            return False
    else:
        if cur not in memory:
            if not is_dead(board, cur):
                return False

    return True

def is_dead(board, position):
    memory[position] = True
    size = len(board)-1
    if min(*position) < 0 or max(*position) > size:
        return True

    desire = board[position[0]] [position[1]] 

    if desire == "":
        return True

    # up
    if position[0] >= 0:
        if not look_direction(board, (position[0]-1, position[1]), desire):
            return False

    # left 
    if position[1] > 0:
        if not look_direction(board, (position[0], position[1]-1), desire):
            return False

    # down 
    if position[0] < size:
        if not look_direction(board, (position[0]+1, position[1]), desire):
            return False

    # right 
    if position[1] < size:
        
        if not look_direction(board, (position[0], position[1]+1), desire):
            return False

    return True

def print_board(board):
    print("--------------------------------------------")
    print("    A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P  Q  R  S")
    counter = 1
    for r in board:
        if counter < 10:
            print(" {}".format(counter), end="  ")
        else:
            print("{}".format(counter), end="  ")

        for c in r:
            cur = "_" if c == "" else c
            print(cur,end="  ")
        
        print("", end='\n')
        counter += 1
    print("--------------------------------------------")


if __name__ == "__main__":
    memory = {} # key tuple, val True
    board = build_empty_board()
    position = (0,3)
    print_board(board)
    assert is_dead(board, (-1, 0))
    assert is_dead(board, (0, -1))
    assert is_dead(board, (19, 0))
    assert is_dead(board, (0, 19))
    assert is_dead(board, (3,3))

    memory = {} # key tuple, val True
    board[3][3] = "b"
    print_board(board)
    assert not is_dead(board, (3,3))

    memory = {} # key tuple, val True
    board[2][3] = "w"
    board[3][2] = "w"
    board[4][3] = "w"
    board[3][4] = "w"
    print_board(board)
    assert is_dead(board, (3,3))

    memory = {} # key tuple, val True
    board[3][4] = "b"
    print_board(board)
    assert not is_dead(board, (3,3))

    memory = {} # key tuple, val True
    board[3][5] = "w"
    print_board(board)
    result = is_dead(board, (3,3))
    assert not result
    print("Position (3,3) is {}".format("Dead" if result else "Alive"))


    memory = {} # key tuple, val True
    board[2][4] = "b"
    board[4][4] = "b"
    print_board(board)
    assert not is_dead(board, (3,3))
    result = "Dead" if is_dead(board, (3,3)) else "Alive"
    print("Position (3,3) is {}".format(result))

    memory = {} # key tuple, val True
    board[2][4] = "w"
    board[4][4] = "w"
    print_board(board)
    assert is_dead(board, (3,3))
    result = "Dead" if is_dead(board, (3,3)) else "Alive"
    print("Position (3,3) is {}".format(result))
