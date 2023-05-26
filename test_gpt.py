from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class ThermometerWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(30, 100)
        self.temperature = 0

    def setTemperature(self, temperature):
        self.temperature = temperature
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

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Thermometer Example")
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.thermometer = ThermometerWidget()
        self.layout.addWidget(self.thermometer)

        self.slider = QSlider(Qt.Vertical)
        self.slider.setMinimum(20)
        self.slider.setMaximum(60)
        self.slider.setTickInterval(5)
        self.slider.setTickPosition(QSlider.TicksRight)
        self.slider.valueChanged.connect(self.onSliderValueChanged)
        self.layout.addWidget(self.slider)

    def onSliderValueChanged(self, value):
        self.thermometer.setTemperature(value)

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    mainWindow = MainWindow()
    mainWindow.show()

    sys.exit(app.exec_())