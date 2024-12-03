import sys
import random

from PyQt6 import uic  # Импортируем uic
from PyQt6.QtCore import QPoint
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QPainter, QColor


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.run)

    def run(self):
        self.update()

    def draw_krug(self, qp):
        size = random.randint(40, 100)
        qp.setBrush(QColor(255, 255, 0))
        qp.setPen(QColor(0, 0, 0))
        qp.drawEllipse(QPoint(random.randint(30, 600), random.randint(30, 600)), size, size)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw_krug(qp)
        qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
