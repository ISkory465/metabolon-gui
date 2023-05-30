from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

class ThermometerWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(50, 100)
        self.temperature = 0
        # self.opcName = name 

    def setTemperature(self,value):
        self.temperature = value
        self.update()


    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        # painter.setClipRect(self.rect(), Qt.ReplaceClip)

        # Draw the background
        painter.fillRect(self.rect(), Qt.lightGray)

        # Calculate the scale position based on the temperature value
        scale_height = int((self.height() - 20) * (self.temperature - 20) / (60 - 20))
        scale_rect = QRect(10, self.height() - scale_height - 10, self.width() - int(self.width()*0.2), scale_height)
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
            painter.drawLine(self.width() - tick_length - 40, y, self.width() - 32, y)
            painter.drawText(self.width() - tick_length - self.width()*0.034375, y + 3, f"{temperature}°C")
            # print(self.width())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    tank = ThermometerWidget()
    tank.show()

    tank.setTemperature(35)

    # Trigger a repaint of the tank
    tank.update()

    sys.exit(app.exec_())

