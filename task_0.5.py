def area_triangle(a, b, c):
    s = (a + b + c) / 2  
    print((s*(s-a)*(s-b)*(s-c)) ** 0.5)

area_triangle(5,6,9)