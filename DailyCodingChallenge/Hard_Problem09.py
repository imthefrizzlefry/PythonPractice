''' his problem was asked by Airbnb.

Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?
'''

def largest_non_adjacent_sum(numbers):
    if not numbers:
        return 0

    if len(numbers) <= 2:
        return max(numbers)

    inclusive = 0
    exclusive = 0

    for num in numbers:
        temp = inclusive
        inclusive = max(inclusive, exclusive + num)
        exclusive = temp

    return max(inclusive, exclusive)

if __name__ == '__main__':
    print(largest_non_adjacent_sum([])) # --> 0
    print(largest_non_adjacent_sum([57])) # --> 57
    print(largest_non_adjacent_sum([5,2])) # --> 5
    print(largest_non_adjacent_sum([2, 4, 6, 2, 5])) # --> 13
    print(largest_non_adjacent_sum([5, 1, 1, 5])) # --> 10
    print(largest_non_adjacent_sum([-5, -6, 1, -5])) # --> 1