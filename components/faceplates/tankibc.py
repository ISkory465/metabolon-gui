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
        self.opcName=name


        self.max_led_color = QColor(255, 0, 0)  # Red
        self.min_led_color = QColor(0, 255, 0)  # Green
        self.led_off_color = QColor(0, 255, 0)  # Dark gray
        self.setup_ui(name)

    def setup_ui(self, name):
        self.setFixedSize(90, 140)
        self.label = QLabel(name)
        self.label.setAlignment(Qt.AlignCenter)
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Draw the tank
        tank_rect = QRect(0, 0, self.width() - 0, self.height() - 0)
        tank_color = Qt.lightGray  # Gray
        painter.setPen(QPen(Qt.NoPen))
        painter.setBrush(QBrush(tank_color))
        painter.drawRect(tank_rect)

        # Draw the max LED
        max_led_rect = QRect(
            tank_rect.right() - 54,
            tank_rect.top() + 5,
            tank_rect.width() - 70,
            8
        )
        if self.current_level >= self.max_level:
            painter.setBrush(QBrush(self.max_led_color))
        else:
            painter.setBrush(QBrush(self.led_off_color))
        painter.drawRect(max_led_rect)

        # # Draw the min LED
        min_led_rect = QRect(
            tank_rect.right() - 54,
            tank_rect.bottom() - 15,
            tank_rect.width() - 70,
            8
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
    
    def update1(self,val:dict):
        try:
          MaxNiv:bool
          MinNiv:bool
          MaxNiv=val[self.opcName+':MaxNiv']
          MinNiv=val[self.opcName+':MinNiv']
         


          if (MaxNiv==True):
            self.set_current_level(160)
            self.set_max_led_color(QColor(255, 0, 0))
            self.set_min_led_color(QColor(0, 255, 0))
          elif (MinNiv==True):
            self.set_current_level(2)
            self.set_max_led_color(QColor(0, 255, 0))
            self.set_min_led_color(QColor(255, 0, 0))
          else:
            print('Neither')
            self.set_max_led_color(QColor(64, 64, 64))
            self.set_min_led_color(QColor(64, 64, 64))  
          #print('If Statement done')
        except Exception as e:
          print('Exception raised')
          #print(val[self.opcName])
          print(str(e))


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
    tank = TankIBC(name='valera',max_level=100, min_level=15)

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
    tank.set_current_level(50)
    tank.set_label_text("IBC")

    main_window.show()

    sys.exit(app.exec_())
