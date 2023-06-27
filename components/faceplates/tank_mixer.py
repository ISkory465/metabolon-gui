import sys
from PyQt5.QtCore import Qt, QPoint, QRectF
from PyQt5.QtGui import QColor, QPainter, QFont, QPen
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout


class TankMixerWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(120, 150)
        self._max_level = 100  # Set the maximum level
        self._min_level = 20  # Set the minimum level
        self._current_level = 30  # Initial level of the tank
        self._motor_mode = 'idle'  # Initial motor mode

        main_layout = QVBoxLayout()  
        self.setLayout(main_layout)

        self.tank_label = QLabel(self)  # Label for the tank
        self.tank_label.setAlignment(Qt.AlignCenter)
        self.tank_label.setFont(QFont('Arial', 9))
        self.tank_label.setStyleSheet('color: white')
        main_layout.addWidget(self.tank_label)

        self.motor_label = QLabel(self)  # Label for the motor
        self.motor_label.setAlignment(Qt.AlignCenter)
        self.motor_label.setFont(QFont('Arial', 9, QFont.Bold))
        self.motor_label.setText("M")
        main_layout.addWidget(self.motor_label)
        
        self.motorName_label = QLabel(self)  # Motor Name
        self.motorName_label.setAlignment(Qt.AlignCenter)
        self.motorName_label.setStyleSheet('color: black')
        self.motorName_label.setFont(QFont('Arial', 8))
        main_layout.addWidget(self.motorName_label)

    def resizeEvent(self, event):
        tank_width = self.width()
        tank_height = self.height()

        # Set the tank label position
        tank_label_width = int(tank_width * 0.8)
        tank_label_height = int(tank_height * 0.1)
        tank_label_x = int((tank_width - tank_label_width) / 2)
        tank_label_y = int((tank_height - tank_label_height) / 2 - tank_height * 0.05)
        self.tank_label.setGeometry(tank_label_x, tank_label_y, tank_label_width, tank_label_height)

        # Set the motor label position
        motor_radius = int(tank_height * 0.2)
        motor_x = int((tank_width - motor_radius) / 2)
        motor_y = int((tank_height - motor_radius) / 20)+ 5
        self.motor_label.setGeometry(motor_x, motor_y, motor_radius, motor_radius)
        
       # Set the Motor Name label position
        motor_label_width = int(tank_width * 0.8)
        motor_label_height = int(tank_height * 0.05)
        motor_label_x = int((tank_width - motor_label_width) / 2)
        motor_label_y = int(motor_y - motor_label_height * 2)  # Adjust the vertical position above the motor
        self.motorName_label.setGeometry(motor_label_x, motor_label_y, motor_label_width, motor_label_height)

    def set_motorName_label(self, text):
        self.motorName_label.setText(text)
    
    def set_tank_label(self, text):
        self.tank_label.setText(text)

    def set_level(self, level):
        self._current_level = max(0.0, min(1.0, level))
        self.update()

    def increase_level(self, increment):
        self.set_level(self._current_level + increment)

    def decrease_level(self, decrement):
        self.set_level(self._current_level - decrement)

    def set_motor_mode(self, mode):
        self._motor_mode = mode
        self.update()

    def paintEvent(self, event):
        tank_width = self.width()
        tank_height = self.height()
        max_level_height = int(self._max_level * tank_height)
        min_level_height = int(self._min_level * tank_height)
        current_level_height = int(self._current_level * (tank_height - tank_height // 10))

        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Draw the motor circle
        motor_radius = tank_height // 6
        motor_x = (tank_width - motor_radius) // 2
        motor_y = tank_height // 20 + 5
        motor_color = QColor(0, 0, 255) if self._motor_mode == 'idle' else QColor(255, 0, 0) if self._motor_mode == 'malfunction' else QColor(0, 255, 0)
        painter.setBrush(motor_color)
        painter.drawEllipse(motor_x, motor_y, motor_radius, motor_radius)

        # Draw the tank
        tank_color = QColor(192, 192, 192)  # Grey color
        tank_x = 0
        tank_y = motor_y + motor_radius + tank_height // 20 
        painter.fillRect(tank_x, tank_y, tank_width, tank_height - tank_y - tank_height // 20, tank_color)

        # Line to the tank
        motor_center = QPoint(motor_x + motor_radius // 2, motor_y + motor_radius)  # Bottom edge of the motor
        tank_center = QPoint(tank_width // 2, tank_y + (tank_height - tank_y) // 2)  # Tank center
        painter.setPen(QColor(0, 0, 0)) 
        painter.drawLine(motor_center, tank_center)

        infinity_color = QColor(64, 64, 64)  # Dark grey 
        infinity_fill_color = Qt.gray  # Grey
        infinity_width = 2
        infinity_radius_x = 12
        infinity_radius_y = 6

        # Calculate the position of the infinity symbol
        line_length = tank_center.x() - motor_center.x()
        touch_point = tank_center - QPoint(line_length, 0)
        infinity_center = touch_point

        # Draw the infinity symbol
        painter.setPen(QPen(infinity_color, infinity_width))

        # Draw the first ellipse of the infinity symbol
        first_ellipse_top_center = infinity_center + QPoint(infinity_radius_x, 0)
        first_ellipse_bottom_center = infinity_center - QPoint(infinity_radius_x, 0)
        painter.setBrush(infinity_fill_color)
        painter.drawEllipse(first_ellipse_top_center, infinity_radius_x, infinity_radius_y)
        painter.drawEllipse(first_ellipse_bottom_center, infinity_radius_x, infinity_radius_y)

        # Draw the second ellipse of the infinity symbol
        second_ellipse_top_center = infinity_center + QPoint(infinity_radius_x, 0)
        second_ellipse_bottom_center = infinity_center - QPoint(infinity_radius_x, 0)
        painter.setBrush(infinity_fill_color)
        painter.drawEllipse(second_ellipse_top_center, infinity_radius_x, infinity_radius_y)
        painter.drawEllipse(second_ellipse_bottom_center, infinity_radius_x, infinity_radius_y)


        # Draw the max level sensor
        max_sensor_color = QColor(255, 0, 0) if current_level_height >= max_level_height else QColor(255, 255, 255)
        max_sensor_width = tank_width // 5
        max_sensor_height = current_level_height // 14
        max_sensor_x = tank_width - max_sensor_width - tank_width // 20  # Move away from the right border
        max_sensor_y = tank_y + tank_height // 20  # Move away from the top border
        painter.setBrush(max_sensor_color)
        painter.drawRect(max_sensor_x, max_sensor_y, max_sensor_width, max_sensor_height)

        # Draw the min level sensor
        min_sensor_color = QColor(0, 255, 0) if current_level_height <= min_level_height else QColor(255, 255, 255)
        min_sensor_width = tank_width // 5
        min_sensor_height = current_level_height // 14
        min_sensor_x = tank_width - min_sensor_width - tank_width // 20  # Move away from the right border
        min_sensor_y = tank_y + tank_height - min_sensor_height - tank_height // 3 - 5  # Move away from the bottom border
        painter.setBrush(min_sensor_color)
        painter.drawRect(min_sensor_x, min_sensor_y, min_sensor_width, min_sensor_height)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    tank = TankMixerWidget()
    tank.set_tank_label("My Tank")  
    tank.show()

    #increase and decrease the level of the tank
    tank.increase_level(0.1)  # Increase the level by 0.1
    tank.decrease_level(0.2)  # Decrease the level by 0.2

    #set the motor mode
    tank.set_motor_mode('malfunction')  
    
    sys.exit(app.exec_())
