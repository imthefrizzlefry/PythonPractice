import logging
from typing import List
from collections import deque

''' asked by a team at Microsoft

An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).

Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.

To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the newColor.

At the end, return the modified image.

Example 1:
Input: 
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: 
From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected 
by a path of the same color as the starting pixel are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected
to the starting pixel.
Note:

The length of image and image[0] will be in the range [1, 50].
The given starting pixel will satisfy 0 <= sr < image.length and 0 <= sc < image[0].length.
The value of each color in image[i][j] and newColor will be an integer in [0, 65535].
'''

def floodFill(image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
    frontier = deque()
    explored = []
    frontier.append((sr, sc))
    lenrow = len(image)
    lencol = len(image[0])
    centerColor = image[sr][sc]
    while frontier:
        logging.debug(frontier)
        curNode = frontier.popleft()
        currow = curNode[0]
        curcol = curNode[1]
        curVal = image[currow][curcol]
        if curVal == centerColor:
            image[curNode[0]][curNode[1]] = newColor
            logging.debug(image)
            # curVal = newColor
            explored.append(curNode)
            for i, j in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                nextrow = currow + i
                nextcol = curcol + j
                if nextrow >= 0 and nextcol >= 0 and nextrow < lenrow and nextcol < lencol and (nextrow, nextcol) not in explored:
                    frontier.append((currow + i, curcol + j))
    return image

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)

    example_image = [[1,1,1],[1,1,0],[1,0,1]]
    starting_point = (1, 1)
    new_color = 2
    logging.debug(example_image)

    result_image = floodFill(image = example_image, sr = starting_point[0], sc = starting_point[1], newColor = new_color)
    logging.debug(result_image)

