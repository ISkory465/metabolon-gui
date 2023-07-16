import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QSpacerItem, QSizePolicy
from PyQt5.QtGui import QPainter, QColor, QPen, QFont, QFontMetrics
from PyQt5.QtCore import Qt, QRectF, QPoint, QRect, pyqtSignal
from PyQt5.QtWidgets import QPushButton

class EndlagerTank(QWidget):

    def __init__(self,name, level=100):
        super().__init__()
        self.setMinimumSize(100, 80)
        self.level = level
        self.buffer = 0
        self.opcName=name

        self.initUI()

    def initUI(self):
        pass

    def setLevel(self, val):
        self.level = val
        self.update()

    def update1(self,val:dict):
        try:
          self.setLevel(val[self.opcName])
        except Exception as e:
          print(self.opcName)
          print(str(e))
          
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setClipRect(self.rect(), Qt.ReplaceClip)

        # Draw the background
        painter.fillRect(self.rect(), Qt.lightGray)

        # Calculate the scale position based on the level value
        # self.buffer = 200  # Adjust the self.buffer value to control the empty space at the top
        scale_height = int((self.height() - self.buffer - 20) * self.level / 100)
        scale_rect = QRect(10, self.height() - 10 - scale_height - 1, self.width() - 70, scale_height + 1)
        
        painter.fillRect(scale_rect, QColor(62, 84, 230))

        # Draw ticks and labels on the right side
        font = QFont()
        font.setPointSize(8)
        painter.setFont(font)
        tick_length = 5
        tick_spacing = (self.height() - self.buffer - 20) / 100
        degree_spacing = 5
        for level in range(0, 101, degree_spacing):
            y = self.height() - 10 - int(level * tick_spacing)
            # y = self.buffer + self.height() - 30 - int((level / 100) * (self.height() - self.buffer))  # Adjusted y coordinate calculation
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
    tank = EndlagerTank()
    tank.show()

    # window = QWidget()
    # layout = QVBoxLayout()
    # window.setLayout(layout)
    # layout.addWidget(tank)

    # tank.setState(1)
    # tank.setState(2)
    tank.setLevel(100)

    # Trigger a repaint of the tank
    tank.update()

    sys.exit(app.exec_())
