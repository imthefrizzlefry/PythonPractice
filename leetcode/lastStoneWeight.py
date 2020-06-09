from  typing import List
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # if len(stones) < 1: return 0
        # stones.sort(reverse=True)
        # x = stones[0]
        # for i in range(1,len(stones)):
        #     y = stones[i]
        #     if x < y:
        #         x, y = y, x
        #     if x == y:
        #         i += 1
        #         if i < len(stones):
        #             x = stones[i]
        #     else:
        #         x = x-y
                
        # return x

        # this is bad because it's (n log n) * n time complexity!
        # for i in range(len(stones) - 1):
        #     stones.sort()
        #     stones.append(stones.pop() - stones.pop()) 
        # return stones[0]

        stones = [-val for val in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            x1 = heapq.heappop(stones)
            x2 = heapq.heappop(stones)
            if x1 != x2:
                heapq.heappush(stones,-abs(x1-x2))
        if len(stones) == 0:
            return 0
        return -stones[0]

if __name__ == "__main__":
    my_solution = Solution()
    print(my_solution.lastStoneWeight([2,7,4,1,8,1]))
    print(my_solution.lastStoneWeight([2,2]))
    print(my_solution.lastStoneWeight([2]))
    print(my_solution.lastStoneWeight([92,700,54,771,80,100]))
    