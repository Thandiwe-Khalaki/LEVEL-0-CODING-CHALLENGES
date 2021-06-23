def area_triangle(a, b, c):
    s = (a + b + c) / 2  
    return (s*(s-a)*(s-b)*(s-c)) ** 0.5

print(area_triangle(5,6,9))