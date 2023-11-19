class Engine2D:
    def __init__(self):
        # Инициализация двумерного движка с пустым холстом и цветом по умолчанию "black"
        self.canvas = []
        self.current_color = "black"

    def set_color(self, color):
        # Установка текущего цвета для рисования
        self.current_color = color

    def add_shape(self, shape):
        # Добавление формы на холст
        self.canvas.append(shape)

    def draw(self):
        # Отрисовка всех форм на холсте с использованием текущего цвета,
        # затем очистка холста
        for shape in self.canvas:
            shape.draw(self.current_color)
        self.canvas = []