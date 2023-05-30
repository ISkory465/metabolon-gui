import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QPainter, QColor, QFont, QPainterPath
from PyQt5.QtCore import Qt, QRect, QPoint, pyqtSignal


class CircularButton(QPushButton):
    turnedOn = pyqtSignal()
    turnedOff = pyqtSignal()

    def __init__(self):
        super().__init__()

        self.active = False
        self.setMinimumSize(100, 100)

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
        font = QFont('Arial', 50, QFont.Bold)
        painter.setFont(font)
        painter.drawText(self.rect(), Qt.AlignCenter, "M")


if __name__ == '__main__':
    app = QApplication(sys.argv)

    button = CircularButton()
    button.show()

    def onTurnedOn():
        print("Button turned ON")

    def onTurnedOff():
        print("Button turned OFF")

    button.turnedOn.connect(onTurnedOn)
    button.turnedOff.connect(onTurnedOff)

    sys.exit(app.exec_())
