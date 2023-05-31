import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QSpacerItem, QSizePolicy
from PyQt5.QtGui import QPainter, QColor, QPen, QFont, QFontMetrics
from PyQt5.QtCore import Qt, QRectF, QPoint, QRect, pyqtSignal
from PyQt5.QtWidgets import QPushButton



class CircularButton(QPushButton):
    turnedOn = pyqtSignal()
    turnedOff = pyqtSignal()

    def __init__(self):
        super().__init__()

        self.active = False
        self.setMinimumSize(60, 60)

        self.clicked.connect(self.toggleActive)

    def toggleActive(self):
        self.active = not self.active
        if self.active:
            self.turnedOn.emit()
        else:
            self.turnedOff.emit()
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Draw the background
        painter.setPen(Qt.NoPen)
        if self.active:
            painter.setBrush(Qt.red)
        else:
            painter.setBrush(Qt.gray)
        painter.drawEllipse(self.rect())

        # Draw the "M" letter
        painter.setPen(Qt.white)
        font = QFont('Arial', 20, QFont.Bold)
        painter.setFont(font)
        painter.drawText(self.rect(), Qt.AlignCenter, "M")


class BigMixer(QWidget):
    def __init__(self, level=10):
        super().__init__()
        self.setMinimumSize(400, 400)
        self.level = level
        self.state = 0  # Initial state for level

        self.initUI()

    def initUI(self):
        buffer = 100

        # Create the circular button
        button = CircularButton()
        button.setGeometry(120, buffer // 2 - 30, 60, 60)  # Set the position and size of the button using absolute positioning
        button.setParent(self)  # Set the widget as the parent of the button

        # Connect the button signals to custom methods
        button.turnedOn.connect(self.onTurnedOn)
        button.turnedOff.connect(self.onTurnedOff)

    def setLevel(self, val):
        self.level = val
        self.update()

    def setState(self, state):
        self.state = state
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setClipRect(self.rect(), Qt.ReplaceClip)

        # Draw the background
        painter.fillRect(self.rect(), Qt.lightGray)

        # Calculate the scale position based on the level value
        buffer = 100  # Adjust the buffer value to control the empty space at the top
        scale_height = int((self.height() - buffer - 20) * self.level / 100)
        scale_rect = QRect(10, self.height() - 10 - scale_height - 1, self.width() - 70, scale_height + 1)
        painter.fillRect(scale_rect, Qt.red)

        # Draw small rectangles in the top corners
        rectangle_size = 40
        rectangle_spacing = 10
        rectangle1 = QRect(rectangle_spacing + 10, buffer + rectangle_spacing + 8, rectangle_size + 20, rectangle_size)
        rectangle2 = QRect(self.width() - rectangle_size - rectangle_spacing - 80, buffer + rectangle_spacing + 8, rectangle_size + 20, rectangle_size)

        # Determine the color based on the state
        rectangle1_color = Qt.green if self.state == 1 else Qt.gray
        rectangle2_color = Qt.green if self.state == 2 else Qt.gray

        # Draw the outline/frame
        outline_pen = QPen(Qt.black, 1)
        painter.setPen(outline_pen)
        painter.drawRect(rectangle1)
        painter.drawRect(rectangle2)

        painter.fillRect(rectangle1.adjusted(1, 1, -1, -1), rectangle1_color)
        painter.fillRect(rectangle2.adjusted(1, 1, -1, -1), rectangle2_color)

        # Draw ticks and labels on the right side
        font = QFont()
        font.setPointSize(12)
        painter.setFont(font)
        tick_length = 5
        tick_spacing = (self.height() - buffer - 20) / 100
        degree_spacing = 5
        for level in range(0, 101, degree_spacing):
            y = self.height() - 10 - int(level * tick_spacing)
            # y = buffer + self.height() - 30 - int((level / 100) * (self.height() - buffer))  # Adjusted y coordinate calculation
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

        # Draw the infinity sign
        ellipse1 = QRectF(60, self.height() - 100, 100, 30)
        ellipse2 = QRectF(140, self.height() - 100, 100, 30)
        painter.drawEllipse(ellipse1)
        painter.drawEllipse(ellipse2)

        # Draw the perpendicular line
        intersection_point = ellipse1.topRight().toPoint()
        line_start = QPoint(150, self.height() - 85)
        line_end = QPoint(150, buffer // 2)
        painter.drawLine(line_start, line_end)


    def onTurnedOn(self):
        print("Button turned ON")
        # Perform actions when the button is turned on

    def onTurnedOff(self):
        print("Button turned OFF")
        # Perform actions when the button is turned off


if __name__ == '__main__':
    app = QApplication(sys.argv)
    tank = BigMixer()
    tank.show()

    tank.setState(1)
    tank.setState(2)
    tank.setLevel(100)

    sys.exit(app.exec_())