class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.area = self.width*height

rectangle_1 = Rectangle(100,200)
print(rectangle_1.area)