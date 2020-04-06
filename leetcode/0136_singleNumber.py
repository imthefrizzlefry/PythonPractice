def singleNumber(nums) -> int:
    i = 0
    for num in nums:
        i ^= num
    return i

if __name__ == "__main__":
    print(singleNumber([5,5,1]))
    print(singleNumber([5,4,1,6,22,1,5,22,4]))