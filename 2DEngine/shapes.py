class Circle:
    def __init__(self, center, radius):
        # Проверка, что центр - это кортеж из двух чисел (x, y)
        if not isinstance(center, tuple) or len(center) != 2 or not all(isinstance(coord, (int, float)) for coord in center):
            raise ValueError("Invalid center. Please provide a tuple of two numerical values (x, y)")

        # Проверка, что радиус - положительное число
        if not isinstance(radius, (int, float)) or radius <= 0:
            raise ValueError("Invalid radius. Please provide a positive numerical value for the radius")
        
        self.center = center
        self.radius = radius

    def draw(self, color):
        # Проверка, что цвет является строкой
        if not isinstance(color, str):
            raise TypeError("Color must be a string.")
        print(f"Drawing Circle: {self.center} with radius {self.radius} in {color} color")


class Triangle:
    def __init__(self, vertices):
        # Проверка, что количество вершин треугольника равно трем
        if len(vertices) != 3:
            raise ValueError("A triangle must have exactly 3 vertices.")
        
        # Проверка, что вершины образуют недегенерированный треугольник
        if self._is_degenerate(vertices):
            raise ValueError("Invalid vertices. The vertices should form a non-degenerate triangle.")

        # Проверка, что вершины не совпадают
        if len(set(vertices)) != 3:
            raise ValueError("Invalid vertices. The vertices should be distinct.")

        self.vertices = vertices

    def _is_degenerate(self, vertices):
        # Проверка, что вершины не лежат на одной прямой
        x1, y1 = vertices[0]
        x2, y2 = vertices[1]
        x3, y3 = vertices[2]

        return (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) == 0

    def draw(self, color):
        # Проверка, что цвет является строкой
        if not isinstance(color, str):
            raise TypeError("Color must be a string.")
        print(f"Drawing Triangle: {self.vertices} in {color} color")


class Rectangle:
    def __init__(self, top_left, width, height):
        # Проверка, что top_left - это кортеж из двух чисел (x, y)
        if not isinstance(top_left, tuple) or len(top_left) != 2 or not all(isinstance(coord, (int, float)) for coord in top_left):
            raise ValueError("Invalid top_left. Please provide a tuple of two numerical values (x, y)")

        # Проверка, что ширина и высота - положительные числа
        if not isinstance(width, (int, float)) or width <= 0:
            raise ValueError("Invalid width. Please provide a positive numerical value for the width")

        if not isinstance(height, (int, float)) or height <= 0:
            raise ValueError("Invalid height. Please provide a positive numerical value for the height")

        self.top_left = top_left
        self.width = width
        self.height = height

    def draw(self, color):
        # Проверка, что цвет является строкой
        if not isinstance(color, str):
            raise TypeError("Color must be a string.")
        print(f"Drawing Rectangle: {self.top_left} with width {self.width} and height {self.height} in {color} color")