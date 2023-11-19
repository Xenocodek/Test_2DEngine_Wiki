import pytest
from engine_2d import Engine2D
from shapes import Circle, Triangle, Rectangle


@pytest.fixture
def engine():
    return Engine2D()

@pytest.fixture
def circle():
    return Circle((0, 0), 1)

@pytest.fixture
def triangle():
    return Triangle([(0, 0), (1, 0), (0, 1)])

@pytest.fixture
def rectangle():
    return Rectangle((1, 1), 3, 2)

class TestEngine2D:

    def test_set_color(self, engine):
        # Установка цвета для двумерного движка
        engine.set_color("red")

        assert engine.current_color == "red"

    def test_add_shape(self, engine, circle):
        # Добавление формы в двумерный движок
        engine.add_shape(circle)

        assert engine.canvas == [circle]

    def test_draw(self, engine, circle, triangle):
        # Добавление двух форм и проверка их рисования
        engine.add_shape(circle)
        engine.add_shape(triangle)

        assert engine.canvas == [circle, triangle]

        engine.draw()
        assert engine.canvas == []


    def test_draw_multiple_shapes_with_same_color(self, engine, circle, rectangle):
        # Добавление форм с одинаковым цветом и их рисование
        engine.set_color("green")
        engine.add_shape(rectangle)
        engine.add_shape(circle)
        engine.draw()

        assert engine.canvas == []

    def test_draw_empty_canvas(self, engine):
        # Рисование пустого холста
        engine.draw()

        assert engine.canvas == []

    def test_draw_canvas_with_one_shape(self, engine, circle):
        # Рисование холста с одной формой
        engine.add_shape(circle)
        engine.draw()

        assert engine.canvas == []

    def test_draw_shapes_with_different_color(self, engine, circle, rectangle):
        # Рисование форм с разными цветами
        engine.set_color("red")
        engine.add_shape(circle)
        engine.set_color("blue")
        engine.add_shape(rectangle)
        engine.draw()
        assert engine.canvas == []