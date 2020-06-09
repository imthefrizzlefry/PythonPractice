'''  Asked by Google

you have an infinate chess board, and every peice on the chess board is a knight.

Given starting and target coordinates, write a method to calculate the number of moves to take the knight.

T(x,y)  (2,2) => 4
(0,0) -> (2,1) -> (3,3) -> (4,1) -> (2,2)
num min moves ?
 1:8  
s(x,y) T(x,y)
S(0,0)==> [(1,2),(1,-2),(-1,2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)]

def find_next_step(start): => []
    ret_list = []
    for d in lookk_source:
        ret_list.append((start[0]+d[0],start[1]+d[1]))
    return ret_list

loop 
'''



def find_target(start, target):
    memory = {start:0}
    move_queue = [start]
    num_iter = 0
    max_dist = abs(target[0]-start[0]) + abs(target[1]-start[1]) +2

    def find_next_step(start, max_dist, moves, memory):
        look_source = [(1,2),(1,-2),(-1,2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)]
        next_moves = []
        

        for d in look_source:
            position= (start[0]+d[0], start[1]+d[1])            
            if position not in memory:
                

                cur_dist = abs(target[0]-position[0]) + abs(target[1]-position[1])

                if cur_dist < max_dist or cur_dist < 4:
                    memory[position] = moves+1
                    next_moves.append(position)
                    max_dist -= max_dist-cur_dist

        return (next_moves, max_dist)


    while target not in memory:
        cur_pos = move_queue.pop(0)
        
        next_moves = find_next_step(cur_pos, max_dist, memory[cur_pos], memory)
                                
        move_queue.extend(next_moves[0])
        max_dist = next_moves[1]
        num_iter += 1

    return (memory[target], num_iter)


if __name__ == "__main__":
    start = (0,0)

    target = (1,0)
    print(find_target(start, target))

    target = (1,1)
    print(find_target(start, target))

    target = (1,2)
    print(find_target(start, target))

    target = (2,2)
    print(find_target(start, target))

    target = (1,10)
    print(find_target(start, target))

    target = (1,1000)
    print(find_target(start, target))

    target = (1000,1)
    print(find_target(start, target))