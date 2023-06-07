import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QSpacerItem, QSizePolicy
from PyQt5.QtGui import QPainter, QColor, QPen, QFont, QFontMetrics
from PyQt5.QtCore import Qt, QRectF, QPoint, QRect, pyqtSignal
from PyQt5.QtWidgets import QPushButton

class BigMixer(QWidget):

    def __init__(self, level=94):
        super().__init__()
        self.setMinimumSize(120, 80)
        self.level = level
        self.motor_state = 2 #3 states: 0 - RED(Faulty); 1 - BLUE(Idle); 2 - GREEN(Active)
        self.heater_state = 2 #3 states: 0 - RED(Faulty); 1 - BLUE(Idle); 2 - GREEN(Active)
        self.buffer = int(self.height() * 0.065) #area above the tank water level

    def setLevel(self, val):
        self.level = val
        self.update()

    def setState(self, state):
        if self.level >= 0.95:
            self.rectangle1_color = Qt.green
        else: self.rectangle1_color = Qt.gray
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setClipRect(self.rect(), Qt.ReplaceClip)

        # Draw the background
        painter.fillRect(self.rect(), Qt.lightGray)
        print(self.rect())

        # Calculate the scale position based on the level value
        scale_height = int((self.height() - self.buffer - 20) * self.level / 100)
        scale_rect = QRect(10, self.height() - 10 - scale_height - 1, self.width() - 70, scale_height + 1)

        #Color of the level in the tanks
        rect_color = QColor(102, 153, 255) #light blue
        painter.fillRect(scale_rect, rect_color)

        # Draw small rectangles in the top corners
        rectangle_size = int(self.width() * 0.05)
        rectangle_spacing = 2
        rectangle1 = QRect(rectangle_spacing + 10, self.buffer + rectangle_spacing + 5, rectangle_size + 20, rectangle_size)

        # Draw ticks and labels on the right side
        font = QFont()
        font.setPointSize(9)
        painter.setFont(font)
        tick_length = 5
        tick_spacing = (self.height() - self.buffer - 20) / 100
        degree_spacing = 5
        for level in range(0, 101, degree_spacing):
            y = self.height() - 10 - int(level * tick_spacing)
            if level in [0, 50, 100]:  # Display labels for values 0, 50, and 100 only
                label_font = painter.font()
                label_font.setBold(True)
                painter.setFont(label_font)
                metrics = QFontMetrics(label_font)
                label_width = metrics.horizontalAdvance(str(level))
                painter.drawText(self.width() - label_width - 14, y + 2, str(level))
                tick_length = 5  # Longer tick length for values 0, 50, and 100
                pen = QPen(painter.pen())
                pen.setWidth(2)  # Thicker pen for values 0, 50, and 100
                painter.setPen(pen)
            else:
                tick_length = 8
                pen = QPen(painter.pen())
                pen.setWidth(1)
                painter.setPen(pen)

            painter.drawLine(self.width() - tick_length - 40, y, self.width() - 60, y)

        
        # Draw small circles in the top corners
        circle_radius = 11
        circle_margin = 5
        motor_circle = QPoint(circle_margin + circle_radius + int(self.width()*0.13) , self.buffer + circle_margin + circle_radius - int(self.height()*0.27))
        heater_circle = QPoint(self.width() - circle_margin - circle_radius - 61, self.buffer + circle_margin + circle_radius + 33)

        
        # Determine the color based on the state of the motor
        if self.motor_state == 0:
            motor_color = Qt.red
        elif self.motor_state == 1:
            motor_color = Qt.blue
        else:
            motor_color = Qt.green
        
        # Determine the color based on the state of the heater
        if self.heater_state == 0:
            heater_color = Qt.red
        elif self.heater_state == 1:
            heater_color = Qt.blue
        else:
            heater_color = Qt.green

        end_x = QPoint(circle_margin + circle_radius + int(self.width()*0.13),  self.buffer + circle_margin + circle_radius + 30)

        elipse_y_var = self.buffer + circle_margin + circle_radius + 30
        painter.drawLine(motor_circle, end_x)


        # Determine the color based on the state
        if self.level >= 95:
            self.rectangle1_color = Qt.green
        else: self.rectangle1_color = Qt.gray

        outline_pen = QPen(Qt.black, 0.9)
        painter.setPen(outline_pen)
        painter.drawRect(rectangle1)
        painter.fillRect(rectangle1.adjusted(1, 1, -1, -1), self.rectangle1_color)

        # Draw the motor and heater circles
        painter.setBrush(motor_color)
        painter.drawEllipse(motor_circle, circle_radius, circle_radius)
        painter.setBrush(heater_color)
        painter.drawEllipse(heater_circle, circle_radius, circle_radius)

        #left heater line
        x_heat_right = QPoint(self.width() - circle_margin - circle_radius*2 - 58, self.buffer + circle_margin + circle_radius + 36)
        y_heat_right = QPoint(self.width() - circle_margin - circle_radius*2 - 58, self.buffer + circle_margin + circle_radius -5)
        painter.drawLine(x_heat_right, y_heat_right)
        
        #right heater line
        x_heat_left = QPoint(self.width() - circle_margin - circle_radius - 53, self.buffer + circle_margin + circle_radius + 36)
        y_heat_left = QPoint(self.width() - circle_margin - circle_radius - 53, self.buffer + circle_margin + circle_radius -5)
        painter.drawLine(x_heat_left, y_heat_left)

        #Draw of the /\ element between the lines
        #Central point is located few pixels above the center of the heater circle
        heater_central_p = heater_circle - QPoint(0, 4)
        painter.drawLine(x_heat_right, heater_central_p)
        painter.drawLine(heater_central_p, x_heat_left)

        # Draw the "M" letter
        if self.motor_state == 2:
            painter.setPen(Qt.black)
        else:
            painter.setPen(Qt.white)
        
        font = QFont('Arial', 9, QFont.Bold)
        painter.setFont(font)
        text_point = motor_circle- QPoint(5, -4)
        painter.drawText(text_point, "M")

        painter.setBrush(Qt.gray)
        painter.setPen(Qt.black)
        # Draw the infinity sign
        ellipse1 = QRectF(19, elipse_y_var, 15, 7)
        ellipse2 = QRectF(34, elipse_y_var, 15, 7)
        painter.drawEllipse(ellipse1)
        painter.drawEllipse(ellipse2)


    def onTurnedOn(self):
        print("Button turned ON")
        # Perform actions when the button is turned on

    def onTurnedOff(self):
        print("Button turned OFF")
        # Perform actions when the button is turned off

    def onCircleClicked(self, event):
        self.circle.setActive(not self.circle.active)  # Toggle the active state of the circle
        if self.circle.active:
            print("Circle activated")
        else:
            print("Circle deactivated")

    # def resizeEvent(self, event):
    #     # Get the new size of the widget
    #     new_size = event.size()

    #     # Calculate the new position of the button based on the new size
    #     new_button_x = new_size.width() - self.circle.width() - 10
    #     new_button_y = new_size.height() - self.circle.height() - 10

    #     # Set the new position of the button
    #     self.circle.move(new_button_x, new_button_y)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    tank = BigMixer()
    tank.show()

    # window = QWidget()
    # layout = QVBoxLayout()
    # window.setLayout(layout)
    # layout.addWidget(tank)

    # tank.setState(1)
    # tank.setState(2)
    tank.setLevel(95)

    # Trigger a repaint of the tank
    tank.update()

    sys.exit(app.exec_())
