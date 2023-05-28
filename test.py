from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class GaugeWidget(QWidget):
    def __init__(self, parent=None, opc_value=0):
        super().__init__(parent)
        self.setMinimumSize(200, 200)
        self.value = opc_value

    def setValue(self, value):
        self.value = value
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Draw the gauge
        size = min(self.width(), self.height())
        side = size * 0.8
        offset = (size - side) / 2
        gauge_rect = QRectF(offset, offset, side, side)

        # Set background color to white
        painter.setBrush(Qt.white)
        painter.setPen(Qt.NoPen)
        painter.drawEllipse(gauge_rect)

        # Draw the gauge pointer
        pointer_length = gauge_rect.width() / 2  # Length of the arrow
        pointer_angle = 90 #225 + (270 - 225) * (self.value - 20) / (60 - 20)  # Modified angle calculation

        painter.save()
        painter.translate(gauge_rect.center())
        painter.rotate(pointer_angle)

        # Draw the small red circle in the middle
        small_circle_radius = int(gauge_rect.width() * 0.1)
        small_circle_rect = QRectF(-small_circle_radius / 2, -small_circle_radius / 2, small_circle_radius, small_circle_radius)
        small_circle_rect.moveCenter(gauge_rect.center())

        small_circle_radius_half = int(gauge_rect.width() * 0.05)
        pointer_path = QPainterPath()
        pointer_path.moveTo(-small_circle_radius_half, 0)
        pointer_path.lineTo(small_circle_radius_half, 0)
        pointer_path.lineTo(0, pointer_length)
        pointer_path.lineTo(-small_circle_radius_half, 0)
        pointer_path.lineTo(0, 0)
        pointer_path.closeSubpath()

        painter.setBrush(Qt.red)
        painter.setPen(Qt.NoPen)
        painter.drawPath(pointer_path)
        painter.restore()


        painter.setBrush(Qt.red)
        painter.setPen(Qt.NoPen)
        painter.drawEllipse(small_circle_rect)

        # Draw the gauge scale
        num_ticks = 30
        tick_length = int(gauge_rect.width() / 2 * 0.1)

        painter.save()
        painter.translate(gauge_rect.center())

        for i in range(num_ticks + 1):
            angle = 225 + (270 - 225) * i / num_ticks
            painter.rotate(angle)

            painter.setPen(Qt.NoPen)
            painter.setBrush(Qt.black)
            painter.drawRect(-tick_length / 2, -int(gauge_rect.height() / 2), tick_length, int(gauge_rect.width() / 2))

            painter.rotate(-angle)

        painter.restore()

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = QWidget()
    layout = QVBoxLayout(window)

    gauge = GaugeWidget()
    gauge.setValue(15)

    layout.addWidget(gauge)
    window.show()

    sys.exit(app.exec_())
