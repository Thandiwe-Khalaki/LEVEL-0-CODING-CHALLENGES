def area_triangle(a, b, c):
    """Takes three numbers and returns the area of a triangle"""
    s = (a + b + c) / 2  
    return (s*(s-a)*(s-b)*(s-c)) ** 0.5

print(area_triangle(5,6,9))