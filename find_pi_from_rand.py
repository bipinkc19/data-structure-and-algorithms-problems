import random
def estimate_py(n):
    """Finds the value of pi using only random function
    
    Args:
        n (int): number of iteratin
    """
    inside_circle = 0
    total_points = 0
    for i in range(n):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        # Generate random point of maximum distance 1. Imagine a square and circle of unit scale
        # Areas of circle / ares of square = points in circle / points in square
        # pi * r * r / (2r)**2 = points in circle / points in square
        # r = 4 * points in circle / points in square
        if (x**2 + y**2) <= 1:
            inside_circle += 1
        total_points += 1
    
    print(4 * inside_circle / total_points) 

estimate_py(10000)
