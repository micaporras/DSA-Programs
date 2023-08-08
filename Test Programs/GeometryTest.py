# Test Program for Lab Assignment 3.1 - GEOMETRY

from Geometry import RegularPolygon

def main():
    # A polygon with default values
    polygon = RegularPolygon()
    print(f"The polygon with 3 sides and a side length of 1 x-coordinate is 0,\nand y-coordinate is 0 has:\n" 
        f"A perimeter of: {polygon.getPerimeter()}\nAn area of: {polygon.getArea()}")
    
    print("-------------------------------------------------------------------")

    # A polygon with 6 sides and its side length is 4
    polygon1 = RegularPolygon(6,4)
    print(f"The polygon with 6 sides and a side length of 4 has:\n" 
        f"A perimeter of: {polygon1.getPerimeter()}\nAn area of: {polygon1.getArea()}")
    
    print("-------------------------------------------------------------------")

    # A polygon with 10 sides, its side length is 4, x coordinate is 5.6, and y coordinate is 7.8
    polygon2 = RegularPolygon(10,4,5.6,7.8)
    print(f"The polygon with 10 sides, a side length of 4, x-coordinate is 5.6,\nand y-coordinate is 7.8 has:\n" 
        f"A perimeter of: {polygon2.getPerimeter()}\nAn area of: {polygon2.getArea()}")

main()