def square(length, width):
        length = float(input("Enter the length of the house: "))
        width = float(input("Enter the width of the house: "))
        area = length * width
        print(f'The square footage of your house is {area}')


def calculate_circumference(radius):
    halfCircle = int(input("Enter the radius of the circle: "))
    radius = 2 * 3.14 * halfCircle
    print(f'The circumference of the circle is {radius}')
