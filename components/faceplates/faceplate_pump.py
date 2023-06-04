from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QApplication
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt
import sys

class PumpWidget(QWidget):
    def __init__(self, name, size=80, parent=None):
        super().__init__(parent)

        # Define the default mode as idle
        self.mode = "idle"

        # Set the fixed size of the widget
        self.setFixedSize(size, size)

        # Create a QVBoxLayout for the widget
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 45)  # Remove margins
        main_layout.setAlignment(Qt.AlignTop)  # Align to the top
        self.setLayout(main_layout)

        # Create the QLabel for the pump state
        self.label = QLabel(self)
        self.label.setText(name)
        self.label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(self.label)

    def set_mode(self, mode):
        # Update the mode of the pump and trigger a repaint
        self.mode = mode
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Define the colors for each mode
        color = {
            "malfunction": QColor(255, 0, 0),  # Red
            "idle": QColor(0, 0, 255),  # Blue
            "operational": QColor(0, 255, 0)  # Green
        }

        # Calculate the position and size of the pump elements
        radius = self.width() * 0.8 / 2
        center_x = self.width() / 2
        center_y = self.height() * 0.5 + self.label.height() * 0.5

        # Draw the pump symbol
        painter.setPen(QPen(Qt.black, 2))

        # Fill the circle with the mode color
        painter.setBrush(color[self.mode])
        painter.drawEllipse(center_x - radius, center_y - radius, radius * 2, radius * 2)

        # Draw the pump symbol lines
        painter.setPen(QPen(Qt.black, 2))
        painter.drawLine(center_x - radius * 0.88, center_y - radius * 0.45,
                         center_x + radius * 0.88, center_y - radius * 0.25)
        painter.drawLine(center_x - radius * 0.88, center_y + radius * 0.45,
                         center_x + radius * 0.88, center_y + radius * 0.25)



if __name__ == "__main__":
    # Create a QApplication instance
    app = QApplication(sys.argv)

    # Create an instance of the PumpWidget
    pump_widget = PumpWidget("Pump", size=50)
    pump_widget.setFixedSize(50, 50)

    # Set the initial mode
    pump_widget.set_mode("operational")

    # Show the pump widget
    pump_widget.show()

    # Start the event loop
    sys.exit(app.exec())
