import sys
from random import randint

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        uic.loadUi('ui.ui', self)
        self.draw_button.clicked.connect(self.create)
        self.objects = []

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        for i in self.objects:
            i.draw(painter)
        painter.end()

    def create(self):
        x = randint(self.draw_widget.x() + 50, self.draw_widget.x() + self.draw_widget.width() - 50)
        y = randint(self.draw_widget.y() + 50, self.draw_widget.y() + self.draw_widget.height() - 50)
        color = QColor(randint(0, 255), randint(0, 255), randint(0, 255))
        radius = randint(10, 50)
        self.objects.append(Circle(x, y, radius, radius, color))
        self.update()


class Circle:
    def __init__(self, x, y, rx, ry, c):
        super(Circle, self).__init__()
        self.x = x
        self.y = y
        self.rx = rx
        self.ry = ry
        self.color = c

    def draw(self, painter):
        painter.setPen(self.color)
        painter.setBrush(self.color)
        painter.drawEllipse(self.x, self.y, self.rx, self.ry)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = Window()
    wnd.show()
    sys.exit(app.exec())
