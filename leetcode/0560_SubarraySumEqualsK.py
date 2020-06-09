from typing import List
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sums_so_far = defaultdict(int)
        our_sum = 0
        num_subarrays = 0
        for v in nums:
            our_sum += v
            if our_sum == k:
                num_subarrays += 1
            if (our_sum - k) in sums_so_far:
                num_subarrays += sums_so_far[our_sum - k]
            sums_so_far[our_sum] += 1
        return num_subarrays 

if __name__ == "__main__":
    temp = Solution()

    print(temp.subarraySum([1,1,1],2))
    print(temp.subarraySum([1,5,10,15,20,30,35],30))