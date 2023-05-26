from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *




class PlayButton(QWidget):
    def __init__(self):
        super().__init__()

        self.active = False
        self.setMinimumSize(60, 60)
        self.setMouseTracking(True)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Define the button's dimensions and colors
        rect = QRect(10, 10, self.width() - 20, self.height() - 20)
        background_color = Qt.green if self.active else Qt.gray
        icon_color = Qt.white if self.active else Qt.darkGray

        # Draw the button background
        painter.setPen(Qt.NoPen)
        painter.setBrush(background_color)
        painter.drawEllipse(rect)

        # Draw the play icon
        painter.setPen(icon_color)
        painter.setBrush(icon_color)
        path = QPainterPath()
        path.moveTo(rect.center().x() - 5, rect.center().y() - 10)
        path.lineTo(rect.center().x() + 10, rect.center().y())
        path.lineTo(rect.center().x() - 5, rect.center().y() + 10)
        path.lineTo(rect.center().x() - 5, rect.center().y() - 10)
        painter.drawPath(path)

    def mousePressEvent(self, event):
        self.active = not self.active
        self.update()

    def enterEvent(self, event):
        QApplication.setOverrideCursor(Qt.PointingHandCursor)

    def leaveEvent(self, event):
        QApplication.restoreOverrideCursor()