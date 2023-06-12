from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class ThermometerWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(70, 150)
        self.temperature = 35

    def setTemperature(self, value):
        self.temperature = value
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Draw the background
        painter.fillRect(self.rect(), Qt.lightGray)

        # Calculate the scale position based on the temperature value
        scale_height = int((self.height() - 20) * (self.temperature - 20) / (60 - 20))

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
        tick_spacing = (self.height() - 20) / (60 - 20)
        degree_spacing = 5
        
        for temperature in range(20, 61, degree_spacing):
            y = self.height() - 10 - int((temperature - 20) * tick_spacing)
            # y = buffer + self.height() - 30 - int((level / 100) * (self.height() - buffer))  # Adjusted y coordinate calculation
            if temperature in [20, 40, 60]:  # Display labels for values 0, 50, and 100 only
                label_font = painter.font()
                label_font.setBold(True)
                painter.setFont(label_font)
                metrics = QFontMetrics(label_font)
                label_width = metrics.horizontalAdvance(str(temperature))
                painter.drawText(self.width() - tick_length - int(self.width()*0.37), y + 3, f"{temperature}°C")
                # painter.drawText(self.width() - label_width - 12, y + 5, str(temperature))
                tick_length = 8  # Longer tick length for values 0, 50, and 100
                pen = QPen(painter.pen())
                pen.setWidth(2)  # Thicker pen for values 0, 50, and 100
                painter.setPen(pen)
            else:
                tick_length = 5
                pen = QPen(painter.pen())
                pen.setWidth(1)
                painter.setPen(pen)

            painter.drawLine(self.width() - tick_length - int(self.width()*0.57625), y, self.width() - int(self.width()*0.575), y)
            # painter.drawText(self.width() - tick_length - int(self.width()*0.37), y + 3, f"{temperature}°C")
            # painter.drawLine(self.width() - tick_length - 40, y, self.width() - 32, y)
            # painter.drawText(self.width() - tick_length - 22, y + 3, f"{temperature}°C")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QWidget()

    # Create a QVBoxLayout
    layout = QVBoxLayout()
    window.setLayout(layout)

    # Create the thermometer widget
    thermometer = ThermometerWidget()

    # Add the thermometer widget to the layout
    layout.addWidget(thermometer)
    # thermometer.setTemperature(33)
    window.show()

    thermometer.setTemperature(40)

    sys.exit(app.exec_())