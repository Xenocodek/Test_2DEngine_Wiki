import pytest
from shapes import Triangle

class TestTriangle:

    def test_initialized_with_three_vertices(self):
        # Инициализация с тремя вершинами
        vertices = [(0, 0), (1, 0), (0, 1)]
        triangle = Triangle(vertices)
        assert triangle.vertices == vertices

    def test_draw_with_valid_color(self):
        # Треугольника с допустимым цветом
        vertices = [(0, 0), (1, 0), (0, 1)]
        triangle = Triangle(vertices)
        color = "red"
        triangle.draw(color)

    def test_initialized_with_invalid_format_vertices(self):
        # Инициализация с вершинами в неверном формате
        vertices = [(0, 0), (1, 0), (0, 1)]
        triangle = Triangle(vertices)
        assert triangle.vertices == vertices

    def test_initialized_with_non_unique_vertices(self):
        # Инициализация с неуникальными вершинами
        vertices = [(0, 0), (1, 0), (0, 1)]
        triangle = Triangle(vertices)
        assert triangle.vertices == vertices
    
    def test_draw_with_empty_string_color(self):
        # Рисунок с пустой строкой в качестве цвета
        vertices = [(0, 0), (1, 0), (0, 1)]
        triangle = Triangle(vertices)
        color = ""
        triangle.draw(color)

    def test_draw_with_non_alphabetic_color(self):
        # Рисунок с цветом, содержащим не буквенные символы
        vertices = [(0, 0), (1, 0), (0, 1)]
        triangle = Triangle(vertices)
        color = "red123"
        triangle.draw(color)

    def test_error_raised_with_incorrect_number_of_vertices(self):
        # Проверка возникновения ошибки при некорректном числе вершин
        vertices = [(0, 0), (1, 1)]
        with pytest.raises(ValueError):
            Triangle(vertices)

    def test_error_raised_with_non_string_color(self):
        # Проверка возникновения ошибки при передаче нестрокового цвета
        vertices = [(0, 0), (1, 0), (0, 1)]
        triangle = Triangle(vertices)
        color = 123
        with pytest.raises(TypeError):
            triangle.draw(color)

    def test_initialized_with_invalid_range_vertices(self):
        # Вершины образуют дегенерированный треугольник
        vertices_degenerate = [(0, 0), (1, 1), (4, 4)]
        with pytest.raises(ValueError):
            Triangle(vertices_degenerate)

    def test_initialized_with_duplicate_vertices(self):
        # Есть одинаковые вершины
        vertices_duplicate = [(0, 0), (1, 1), (0, 0)]
        with pytest.raises(ValueError):
            Triangle(vertices_duplicate)

    def test_initialized_with_valid_vertices(self):
        # Вершины формируют корректный треугольник
        vertices_valid = [(0, 0), (1, 0), (0, 1)]
        triangle = Triangle(vertices_valid)
        assert triangle.vertices == vertices_valid