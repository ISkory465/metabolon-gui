from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys



class PlayButton(QWidget):
    def __init__(self):
        super().__init__()

        self.state = 2 #3 states: 0 - RED(Faulty); 1 - BLUE(Idle); 2 - GREEN(Active)
        self.setFixedSize(60, 60)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Determine the color based on the state of the indicator
        if self.state == 0:
            background_color = Qt.red
            icon_color = Qt.white
        elif self.state == 1:
            background_color = Qt.blue
            icon_color = Qt.white
        else:
            background_color = Qt.green
            icon_color = Qt.white

        # Define the button's dimensions and colors
        # rect = QRect(10, 10, self.width() - 20, self.height() - 20)
        rect = QRect(1, 1, self.width()-2, self.height()-2)

        # Draw the button background
        painter.setPen(Qt.NoPen)
        painter.setBrush(background_color)
        painter.drawEllipse(rect)

        # Draw the play icon
        painter.setPen(icon_color)
        painter.setBrush(icon_color)
        path = QPainterPath()

        path.moveTo(rect.center().x() + int(self.width()*0.33), rect.center().y())
        path.lineTo(rect.center().x() - int(self.width()*0.16), rect.center().y() - int(self.height()*0.28))
        path.lineTo(rect.center().x() - int(self.width()*0.16), rect.center().y() + int(self.height()*0.3))
        path.lineTo(rect.center().x() + int(self.width()*0.33), rect.center().y())
        painter.drawPath(path)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    btn = PlayButton()
    btn.show()

    sys.exit(app.exec_())