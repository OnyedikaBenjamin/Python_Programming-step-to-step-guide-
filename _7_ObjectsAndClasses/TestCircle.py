from Circle import Circle


class Main:
    circle3 = Circle(9)
    circle4 = Circle(8)

    print("Circle 3 area and perimeter are", circle3.get_area(), "and", format(circle3.get_perimeter(), ".2f"), "respectively")
    print("Circle 4 area and perimeter are", circle4.get_area(), "and", format(circle4.get_perimeter(), ".2f"), "respectively")
