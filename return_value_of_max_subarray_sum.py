"""Given an array return the value of maximum subarray sum
[-2, -3, 4, -1, -2, 1, 5, -3]
4 + -1 + -2 + 1 + 5 = max
"""

def give_max_sum_of_sub_array(arr):
    if len(arr) == 0:
        return 0
    
    solutions = []
    summed = 0
    for i in arr:
        if summed < 0:
            summed = 0
        summed += i
        solutions.append(summed)

    return max(solutions)

print(give_max_sum_of_sub_array([-5, 2, 1, 3, -1, 4, -10, 12, -2, 1, 3]))
