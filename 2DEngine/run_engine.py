from engine_2d import Engine2D
from shapes import Circle, Triangle, Rectangle


def start():

    # Создаем движок
    engine = Engine2D()

    # Создаем фигуры
    circle = Circle((0, 1), 5)
    triangle = Triangle([(0, 0), (1, 0), (0, 1)])
    rectangle = Rectangle((1, 1), 3, 2)

    # Добавляем фигуры на холст
    engine.add_shape(circle)
    engine.add_shape(triangle)
    engine.add_shape(rectangle)

    # Рисуем все фигуры на холсте с текущим цветом
    engine.draw()

    # Меняем цвет и добавляем новые фигуры
    engine.set_color("red")
    new_circle = Circle((2, 2), 4)
    new_triangle = Triangle([(1, 2), (3, 2), (2, 4)])

    engine.add_shape(new_circle)
    engine.add_shape(new_triangle)

    # Рисуем новые фигуры на холсте с новым цветом
    engine.draw()

if __name__ == '__main__':
    start()