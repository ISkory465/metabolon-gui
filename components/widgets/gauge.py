import math
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt


class Gauge(QWidget):
    def __init__(self, value=12):
        super().__init__()
        self.setFixedSize(100, 100)
        self.value = value

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        size = self.size()
        side = min(size.width(), size.height())
        painter.setViewport((size.width() - side) // 2, (size.height() - side) // 2, side, side)
        painter.setWindow(0, 0, 100, 100)
        painter.setPen(Qt.NoPen)

        # Draw outline
        painter.setBrush(Qt.black)
        painter.drawEllipse(4, 4, 92, 92)

        # Draw background
        painter.setBrush(Qt.white)
        painter.drawEllipse(5, 5, 90, 90)

        # Draw ticks and labels
        painter.setPen(QPen(Qt.black, 2))
        font = painter.font()
        font.setPointSize(8)
        painter.setFont(font)
        metrics = painter.fontMetrics()
        label_height = metrics.height()

        for i in range(-2, 7):
            angle = 0 + i * 36
            x1, y1 = map(int, self._get_point(angle, 0.85)) # closer to the center of the circle
            x2, y2 = map(int, self._get_point(angle, 0.95)) # farther from the center of the circle
            x3, y3 = map(int, self._get_point(angle, 0.55))
            painter.drawLine(x1, y1, x2, y2)

            label_value = i * 5
            label_width = metrics.width(str(label_value))
            label_x = x3 - (label_width) // 2 
            label_y = y3 + (label_height-5) // 2 # Adjust the label position
            if label_value % 10 == 0:
                painter.drawText(label_x, label_y, str(label_value))

        # Draw needle
        painter.setPen(QPen(Qt.red, 2))
        angle = 270 + self.value * 12
        x1, y1 = map(int, self._get_point(angle, 0.15))
        x2, y2 = map(int, self._get_point(angle, 0.85))
        painter.drawLine(x1, y1, x2, y2)

    def _get_point(self, angle, radius):
        angle_rad = math.radians(540 - angle)
        x = 50 + math.cos(angle_rad) * 40 * radius
        y = 50 - math.sin(angle_rad) * 40 * radius
        return x, y

    def set_value(self, value):
        self.value = min(max(value, 0), 25)
        self.update()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QWidget()

    # Create a QVBoxLayout
    layout = QVBoxLayout()
    window.setLayout(layout)

    gauge = Gauge()
    layout.addWidget(gauge)
    window.show()

    

    sys.exit(app.exec_())