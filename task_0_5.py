def area_triangle(side_a, side_b, side_c):
    sides = (side_a + side_b + side_c) / 2
    print((sides * (sides - side_a) * (sides - side_b) * (sides - side_c)) ** 0.5)




def main():
    area_triangle(5, 6, 9)

if __name__ == "__main__":
    main()