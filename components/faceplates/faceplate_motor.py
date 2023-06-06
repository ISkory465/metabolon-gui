from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QApplication
from PyQt5.QtGui import QPainter, QColor, QPen, QBrush
from PyQt5.QtCore import Qt
import sys

class MotorLabelWidget(QWidget):
    def __init__(self, label, innerlabel = "Motor", size=50):
        super().__init__()
        self.motor = MotorWidget(innerlabel, size)
        self.motorName = label
        self.motor.set_mode = "idle"
        self.__drawmotor()
        
    def set_mode(self, mode):
        self.motor.set_mode = mode
        self.motor.update()
        
    def __drawmotor(self):
        self.layout = QVBoxLayout()
        self.layout.setSpacing(10)
        self.setLayout(self.layout)

        self.label = QLabel(self.motorName)
        self.layout.setAlignment(Qt.AlignCenter)
        
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.motor)

class MotorWidget(QWidget):
    def __init__(self, label, size=70):
        super().__init__()
        self.mode = "operational"
        self.size = size

        self.label = QLabel(label)
        self.label.setAlignment(Qt.AlignCenter)

        self.setFixedSize(size, size)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)

    def set_mode(self, mode):
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

        # Calculate the position and size of the Motor element
        radius = self.size * 0.6 / 2
        center_x = self.width() / 2
        center_y = self.height() / 2 - radius / 2

        # Fill the circle with the mode color
        painter.setBrush(color[self.mode])
        painter.drawEllipse(int(center_x - radius), int(center_y - radius), int(radius * 2), int(radius * 2))

    def sizeHint(self):
        return self.minimumSizeHint()


if __name__ == "__main__":
    # Create a QApplication instance
    app = QApplication(sys.argv)

    # Create the parent widget
    parent_widget = QWidget()

    # Create an instance of the LED widget
    motor_widget = MotorWidget("Motor", size=100)

    # Set the initial mode
    motor_widget.set_mode("operational")


    # Show the LED widget
    motor_widget.show()

    # Create a QHBoxLayout for the parent widget
    layout = QHBoxLayout()
    parent_widget.setLayout(layout)

    # Add the LED widget to the layout
    layout.addWidget(motor_widget)

    # Show the parent widget
    parent_widget.show()

    # Start the event loop
    sys.exit(app.exec())
