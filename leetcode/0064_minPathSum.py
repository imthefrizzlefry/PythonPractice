
from typing import List

def minPathSum(grid: List[List[int]]) -> int:
    if len(grid) <= 0 or grid is None:
        return 0
    
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if r==0 and c==0:
                    continue
            if r-1<0:
                grid[r][c] = grid[r][c] + grid[r][c-1]  
            elif c-1<0:
                grid[r][c] = grid[r][c] + grid[r-1][c]  
            else:
                grid[r][c] = grid[r][c] + min(grid[r-1][c], grid[r][c-1])               
    
    return grid[-1][-1]


print(minPathSum([[1,3,1],[1,5,1],[4,2,1]]))