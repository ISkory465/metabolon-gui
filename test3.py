import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor, QPen, QFont, QFontMetrics
from PyQt5.QtCore import Qt


from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class BigMixer(QWidget):
    def __init__(self, level=10):
        super().__init__()
        self.setMinimumSize(100, 200)  # Increased the minimum width to accommodate the ticks and labels
        self.level = level
        self.state = 0  # Initial state for level

    def setLevel(self, val):
        self.level = val
        self.update()

    def setState(self, state):
        self.state = state
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Draw the background
        painter.fillRect(self.rect(), Qt.lightGray)

        # # Calculate the scale position based on the level value
        # scale_width = int((self.width() - 30) * (self.level) / (100))
        # scale_rect = QRect(10, self.height() - 10 - scale_width, self.width() - 70, scale_width)
        # painter.fillRect(scale_rect, Qt.red)

        # Calculate the scale position based on the level value
        scale_height = int((self.height()) * (self.level) / 100)
        scale_rect = QRect(10, 10, self.width() - 20, self.height() - 30 - scale_height)
        painter.fillRect(scale_rect, Qt.red)


        # Draw small rectangles in the top corners
        rectangle_size = 40
        rectangle_spacing = 10
        rectangle1 = QRect(rectangle_spacing + 10, rectangle_spacing, rectangle_size + 20, rectangle_size)
        rectangle2 = QRect(self.width() - rectangle_size - rectangle_spacing - 80, rectangle_spacing, rectangle_size + 20, rectangle_size)

        # Determine the color based on the state
        rectangle1_color = Qt.green if self.state == 1 else Qt.gray
        rectangle2_color = Qt.green if self.state == 2 else Qt.gray

        painter.fillRect(rectangle1, rectangle1_color)
        painter.fillRect(rectangle2, rectangle2_color)

        # Draw ticks and labels on the right side
        font = QFont()
        font.setPointSize(12)
        painter.setFont(font)
        tick_length = 5
        tick_spacing = (self.height() - 20) / (100)
        degree_spacing = 5
        for level in range(0, 101, degree_spacing):
            y = self.height() - 10 - int((level) * tick_spacing)
            if level in [0, 50, 100]:  # Display labels for values 0, 50, and 100 only
                label_font = painter.font()
                label_font.setBold(True)
                painter.setFont(label_font)
                metrics = QFontMetrics(label_font)
                label_width = metrics.horizontalAdvance(str(level))
                painter.drawText(self.width() - label_width - 12, y + 5, str(level))
                tick_length = 5  # Longer tick length for values 0, 50, and 100
                pen = QPen(painter.pen())
                pen.setWidth(2)  # Thicker pen for values 0, 50, and 100
                painter.setPen(pen)
            else:
                tick_length = 8
                pen = QPen(painter.pen())
                pen.setWidth(1)
                painter.setPen(pen)

            painter.drawLine(self.width() - tick_length - 40, y, self.width() - 60, y)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    tank = BigMixer()
    tank.show()

    tank.setState(1)
    tank.setState(2)
    tank.setLevel(20)

    # Trigger a repaint of the tank
    tank.update()

    sys.exit(app.exec_())
