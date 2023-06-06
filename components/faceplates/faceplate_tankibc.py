import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PyQt5.QtGui import QPainter, QColor, QBrush, QPen, QFont
from PyQt5.QtCore import Qt, QRect


class TankIBC(QWidget):
    def __init__(self, name, max_level=100, min_level=15):
        super().__init__()

        self.max_level = max_level
        self.min_level = min_level
        self.current_level = 55

        self.max_led_color = QColor(255, 0, 0)  # Red
        self.min_led_color = QColor(0, 255, 0)  # Green
        self.led_off_color = QColor(64, 64, 64)  # Dark gray
        self.setup_ui(name)

    def setup_ui(self, name):
        self.setFixedSize(200, 200)
        self.label = QLabel(name)
        self.label.setAlignment(Qt.AlignCenter)
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Draw the tank
        tank_rect = QRect(30, 30, self.width() - 80, self.height() - 80)
        tank_color = QColor(128, 128, 128)  # Gray
        painter.setPen(QPen(Qt.NoPen))
        painter.setBrush(QBrush(tank_color))
        painter.drawRect(tank_rect)

        # Draw the max LED
        max_led_rect = QRect(
            tank_rect.right() - 50,
            tank_rect.top() + 5,
            tank_rect.width() - 80,
            10
        )
        if self.current_level >= self.max_level:
            painter.setBrush(QBrush(self.max_led_color))
        else:
            painter.setBrush(QBrush(self.led_off_color))
        painter.drawRect(max_led_rect)

        # Draw the min LED
        min_led_rect = QRect(
            tank_rect.right() - 50,
            tank_rect.bottom() - 15,
            tank_rect.width() - 80,
            10
        )
        if self.current_level <= self.min_level:
            painter.setBrush(QBrush(self.min_led_color))
        else:
            painter.setBrush(QBrush(self.led_off_color))
        painter.drawRect(min_led_rect)

    def set_max_led_color(self, color):
        self.max_led_color = color
        self.update()

    def set_min_led_color(self, color):
        self.min_led_color = color
        self.update()

    def set_led_off_color(self, color):
        self.led_off_color = color
        self.update()

    def set_current_level(self, level):
        self.current_level = level
        self.update()

        # Update LED colors based on current level
        self.update_led_colors()

    def set_label_text(self, text):
        self.label.setText(text)

    def update_led_colors(self):
        self.update()

    def get_widget(self):
        return self
    
    def sizeHint(self):
        return self.minimumSizeHint()



if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Example usage in a different UI
    tank = TankIBC(max_level=100, min_level=15)

    # Create your main UI
    main_window = QWidget()
    main_layout = QVBoxLayout()
    main_layout.addWidget(tank.get_widget())  # Add the tank widget to your main UI layout
    main_window.setLayout(main_layout)

    # Set the LED colors (example)
    tank.set_max_led_color(QColor(255, 0, 0))  # Red
    tank.set_min_led_color(QColor(0, 255, 0))  # Green
    tank.set_led_off_color(QColor(64, 64, 64))  # Dark gray

    # Set the tank level and label text (example)
    tank.set_current_level(15)
    tank.set_label_text("IBC")

    main_window.show()

    sys.exit(app.exec_())
