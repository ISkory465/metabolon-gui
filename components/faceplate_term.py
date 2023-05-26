from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class ThermometerWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(50, 200)
        self.temperature = 0
        # self.opcName = name 

    def setTemperature(self,val:dict):
        self.temperature = val[self.opcName]
        self.update()


    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Draw the background
        painter.fillRect(self.rect(), Qt.lightGray)

        # Calculate the scale position based on the temperature value
        scale_height = int((self.height() - 20) * (self.temperature - 20) / (60 - 20))
        scale_rect = QRect(10, self.height() - scale_height - 10, self.width() - 20, scale_height)
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
            painter.drawLine(self.width() - tick_length, y, self.width(), y)
            painter.drawText(self.width() - tick_length - 25, y + 5, f"{temperature}°C")
