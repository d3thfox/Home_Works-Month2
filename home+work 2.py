class Figure:
    unit = "cm"

    def __init__(self):
        def calculate_area(self):
            pass

        def info(self):
            pass


class Square(Figure):
    def __init__(self, side_lenght):
        super(Figure, self).__init__()
        self.__side_lenght = side_lenght

    def calculate_area(self):
        return self.__side_lenght ** 2

    def info(self):
        print(f"SQUARE SIDE LENGHT: {self.__side_lenght}{self.unit} AREA: {self.calculate_area()}{self.unit}")


class Rectangle(Figure):
    def __init__(self, lenght, wight):
        super(Figure, self).__init__()
        self.__lenght = lenght
        self.__wight = wight

    def calculate_area(self):
        return self.__lenght * self.__wight

    def info(self):
        print( f"RECTANGLE WIGHT: {self.__wight}{self.unit} RECTANGLE LENGHT: {self.__lenght}{self.unit} RECTANGLE AREA:{self.calculate_area()}{self.unit}")
square1 = Square(100)
square2 = Square(15)
rectangle1 = Rectangle(15,10)
rectangle2 = Rectangle(20,30)
rectangle3 = Rectangle(5,25)
list_figure = {square1,square2,rectangle1,rectangle2,rectangle3}
for figure in list_figure:
    print(figure.info())

