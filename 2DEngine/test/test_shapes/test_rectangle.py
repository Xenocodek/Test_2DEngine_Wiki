import pytest
from shapes import Rectangle

class TestRectangle:

    def test_valid_arguments(self):
        # Проверка корректных аргументов для прямоугольника
        top_left = (0, 0)
        width = 5
        height = 10
        rectangle = Rectangle(top_left, width, height)
        assert rectangle.top_left == top_left
        assert rectangle.width == width
        assert rectangle.height == height

    def test_valid_color(self):
        # Рисование прямоугольника с допустимым цветом
        top_left = (0, 0)
        width = 5
        height = 10
        rectangle = Rectangle(top_left, width, height)
        color = "blue"
        rectangle.draw(color)

    def test_float_values(self):
        # Проверка использования вещественных значений для прямоугольника
        top_left = (0.5, 0.5)
        width = 5.5
        height = 10.5
        rectangle = Rectangle(top_left, width, height)
        assert rectangle.top_left == top_left
        assert rectangle.width == width
        assert rectangle.height == height
        
    def test_integer_values(self):
        # Проверка использования целочисленных значений для прямоугольника
        top_left = (1, 1)
        width = 5
        height = 10
        rectangle = Rectangle(top_left, width, height)
        assert rectangle.top_left == top_left
        assert rectangle.width == width
        assert rectangle.height == height

    def test_string_color(self):
        # Рисование прямоугольника с допустимым строковым цветом
        top_left = (0, 0)
        width = 5
        height = 10
        rectangle = Rectangle(top_left, width, height)
        color = "red"
        rectangle.draw(color)

    def test_invalid_top_left(self):
        # Проверка исключения при передаче некорректного значения top_left
        top_left = (0, 0, 0)
        width = 5
        height = 10
        with pytest.raises(ValueError):
            Rectangle(top_left, width, height)

    def test_invalid_width(self):
        # Проверка исключения при передаче отрицательной ширины
        top_left = (0, 0)
        width = -5
        height = 10
        with pytest.raises(ValueError):
            Rectangle(top_left, width, height)

    def test_invalid_height(self):
        # Проверка исключения при передаче отрицательной высоты
        top_left = (0, 0)
        width = 5
        height = -10
        with pytest.raises(ValueError):
            Rectangle(top_left, width, height)

    def test_non_string_color(self):
        # Проверка исключения при передаче нестрокового цвета
        top_left = (0, 0)
        width = 5
        height = 10
        rectangle = Rectangle(top_left, width, height)
        color = 123
        with pytest.raises(TypeError):
            rectangle.draw(color)

    def test_negative_width(self):
        # Проверка исключения при передаче отрицательной ширины
        top_left = (0, 0)
        width = -5
        height = 10
        with pytest.raises(ValueError):
            Rectangle(top_left, width, height)