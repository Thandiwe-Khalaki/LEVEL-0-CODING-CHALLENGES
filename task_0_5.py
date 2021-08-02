def area_triangle(a, b, c):
    s = (a + b + c) / 2
    print((s * (s - a) * (s - b) * (s - c)) ** 0.5)




def main():
    area_triangle(5, 6, 9)

if __name__ == "__main__":
    main()