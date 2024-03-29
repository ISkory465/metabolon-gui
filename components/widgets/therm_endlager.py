from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class EndThermometerWidget(QWidget):
    def __init__(self,name):
        super().__init__()
        self.setMinimumSize(70, 150)
        self.temperature = 35
        self.opcName=name

    def setTemperature(self, value):
        self.temperature = value
        self.update()
    def update1(self,val:dict):
        try:
          self.setTemperature(val[self.opcName])
        except Exception as e:
          print(self.opcName)
          print(str(e))
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Draw the background
        painter.fillRect(self.rect(), Qt.lightGray)

        # Calculate the scale position based on the temperature value
        scale_height = int((self.height() - 20) * (self.temperature - 5) / (40 - 5))

        # Limit the width of the scale rectangle
        max_scale_width = int(self.width() * 0.4)
        scale_width = min(max_scale_width, self.width() - 20)
        scale_rect = QRect(2, self.height() - scale_height - 10, scale_width, scale_height)
        painter.fillRect(scale_rect, Qt.red)

        # Draw ticks and labels
        font = QFont()
        font.setPointSize(8)
        painter.setFont(font)
        tick_length = 5
        tick_spacing = (self.height() - 20) / (40 - 5)
        degree_spacing = 5
        for temperature in range(5, 41, degree_spacing):
            y = self.height() - 10 - int((temperature - 5) * tick_spacing)

            if temperature in [5, 20, 40]:  # Display labels for values 5, 20, and 40 only
                label_font = painter.font()
                label_font.setBold(True)
                painter.setFont(label_font)
                metrics = QFontMetrics(label_font)
                label_width = metrics.horizontalAdvance(str(temperature))
                painter.drawText(self.width() - tick_length - int(self.width()*0.37), y + 3, f"{temperature}°C")
                tick_length = 8  # Longer tick length for values 5, 20, and 40
                pen = QPen(painter.pen())
                pen.setWidth(2)  # Thicker pen for values 5, 20, and 40
                painter.setPen(pen)
            else:
                tick_length = 5
                pen = QPen(painter.pen())
                pen.setWidth(1)
                painter.setPen(pen)

            painter.drawLine(self.width() - tick_length - int(self.width()*0.57625), y, self.width() - int(self.width()*0.575), y)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QWidget()

    # Create a QVBoxLayout
    layout = QVBoxLayout()
    window.setLayout(layout)

    # Create the thermometer widget
    thermometer = EndThermometerWidget()

    # Add the thermometer widget to the layout
    layout.addWidget(thermometer)

    window.show()

    thermometer.setTemperature(40)  # This should be within the range [5, 40]

    sys.exit(app.exec_())
