import pytest
from shapes import Circle

class TestCircle:

    def test_initialized_with_center_and_radius(self):
        # Инициализация круга с указанием центра и радиуса
        center = (0, 0)
        radius = 5
        circle = Circle(center, radius)
        assert circle.center == center
        assert circle.radius == radius

    def test_valid_color_string(self):
        # Рисование круга с допустимым цветом
        center = (0, 0)
        radius = 5
        circle = Circle(center, radius)
        color = "red"
        circle.draw(color)

    def test_integer_and_float_values(self):
        # Инициализация круга с центром и радиусом заданными числовыми значениями
        center = (0.5, 0.5)
        radius = 5.5
        circle = Circle(center, radius)
        assert circle.center == center
        assert circle.radius == radius

    def test_circle_draw(self, capsys):
        # Рисование круга с заданным цветом и проверка вывода
        center = (0, 0)
        radius = 5
        circle = Circle(center, radius)
        color = "blue"
        circle.draw(color)

        captured = capsys.readouterr()
        expected_output = f"Drawing Circle: {center} with radius {radius} in {color} color\n"
        assert captured.out == expected_output

    def test_circle_draw_empty_color(self, capsys):
        # Рисование круга с пустой строкой в качестве цвета и проверка вывода
        center = (0, 0)
        radius = 5
        circle = Circle(center, radius)
        color = ""
        circle.draw(color)

        captured = capsys.readouterr()
        expected_output = f"Drawing Circle: {center} with radius {radius} in {color} color\n"
        assert captured.out == expected_output

    def test_circle_default_color(self, capsys):
        # Рисование круга с цветом по умолчанию и проверка вывода
        center = (0, 0)
        radius = 5
        circle = Circle(center, radius)
        color = "black"
        circle.draw(color) 

        captured = capsys.readouterr()
        expected_output = f"Drawing Circle: {center} with radius {radius} in black color\n"
        assert captured.out == expected_output

    def test_circle_draw_long_color(self, capsys):
        # Рисование круга с очень длинной строкой в качестве цвета и проверка вывода
        center = (0, 0)
        radius = 5
        circle = Circle(center, radius)
        color = "this_is_a_very_long_string"
        circle.draw(color)

        captured = capsys.readouterr()
        expected_output = f"Drawing Circle: {center} with radius {radius} in {color} color\n"
        assert captured.out == expected_output

    def test_circle_draw_special_character_color(self, capsys):
        # Рисование круга с специальным символом в качестве цвета и проверка вывода
        center = (0, 0)
        radius = 5
        circle = Circle(center, radius)
        color = "@"
        circle.draw(color)

        captured = capsys.readouterr()
        expected_output = f"Drawing Circle: {center} with radius {radius} in {color} color\n"
        assert captured.out == expected_output

    def test_invalid_center_not_tuple(self):
        # Проверка исключения при передаче центра, не являющегося кортежем
        center = [0, 0]
        radius = 5
        with pytest.raises(ValueError):
            Circle(center, radius)
    
    def test_invalid_center_more_than_two_values(self):
        # Проверка исключения при передаче центра с более чем двумя значениями
        center = (0, 0, 0)
        radius = 5
        with pytest.raises(ValueError):
            Circle(center, radius)

    def test_invalid_center_non_numerical_values(self):
        # Проверка исключения при передаче центра с нечисловыми значениями
        center = ("0", "0")
        radius = 5
        with pytest.raises(ValueError):
            Circle(center, radius)

    def test_invalid_center_type(self):
        # Проверка исключения при передаче центра некорректного типа
        with pytest.raises(ValueError, match="Invalid center"):
            Circle("not a tuple", 5)

    def test_invalid_center_length(self):
        # Проверка исключения при передаче центра с неверной длиной
        with pytest.raises(ValueError, match="Invalid center"):
            Circle((1, 2, 3), 5)

    def test_invalid_center_coordinate_type(self):
        # Проверка исключения при передаче центра с нечисловым типом координат
        with pytest.raises(ValueError, match="Invalid center"):
            Circle(("string", 2), 5)

    def test_invalid_radius_type(self):
        # Проверка исключения при передаче некорректного типа радиуса
        with pytest.raises(ValueError, match="Invalid radius"):
            Circle((0, 0), "not a number")

    def test_invalid_negative_radius(self):
        # Проверка исключения при передаче отрицательного значения радиуса
        with pytest.raises(ValueError, match="Invalid radius"):
            Circle((0, 0), -5)
