import sys
import random

from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QWidget, QApplication, QPushButton


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.do = False

    def initUI(self):
        self.setGeometry(300, 300, 200, 200)
        self.setWindowTitle('Рисование')
        self.btn = QPushButton(self)
        self.btn.move(200, 500)
        self.setGeometry(300, 300, 700, 700)
        self.btn.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()

    def paint(self):
        self.do = True
        self.repaint()
    def draw_circle(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        d = random.randint(10, 100)
        qp.drawEllipse(150, 150, d, d)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())