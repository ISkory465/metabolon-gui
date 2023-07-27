import sys
from PyQt5.QtWidgets    import *
from PyQt5.QtCore       import Qt
from PyQt5.QtCore       import QTimer
from ..faceplates.tankibc import TankIBC
from .pump import PumpWidget
from .valve import *
from .infofield_dbl import *
from ..faceplates.tank_mixer import *
from components.widgets.leds import SingleLed

class LineDrawer(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        # List to store lines to draw [(x1, y1, x2, y2), ...]
        self.lines = []

    def add_line(self, x1, y1, x2, y2):
        # Add a line to draw on next repaint
        self.lines.append((x1, y1, x2, y2))

    def paintEvent(self, event):
        super().paintEvent(event)  # Call superclass paintEvent to draw child widgets

        # Called when the widget is being repainted
        painter = QPainter(self)

        # Set the pen to use for drawing
        pen = QPen()
        pen.setWidth(3)
        pen.setColor(Qt.black)
        painter.setPen(pen)

        # Draw all lines
        for line in self.lines:
            x1, y1, x2, y2 = line
            painter.drawLine(x1, y1, x2, y2)

class Str1(LineDrawer):  # Str1 now inherits from LineDrawer
    def __init__(self, opcID=None):
        super().__init__()

        self.opcID = opcID  # TODO: add OPC functionality

        # Initialize the main layout
        self.main_layout = QGridLayout()
        self.setLayout(self.main_layout)
        
        # Create the TankIBC widget
        self.tankIbc = TankIBC(name="IBC", max_level=100, min_level=15)
        self.tankIbc.set_current_level(10)
        self.tankIbc.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        # tankIbc_center = self.tankIbc.mapToGlobal(self.tankIbc.geometry().center())
        # tankIbc_center_x = tankIbc_center.x()
        # tankIbc_center_y = tankIbc_center.y()
        
        
        # Create the TankIBC widget
        self.main_layout.addWidget(self.tankIbc.get_widget(), 4, 0, 1, 1)  # Add the tank widget to the grid layout
        
        # Create infofield and add it to the grid 
        self.infofieldNah = InfoField("Temp. Nahwaermenetz [C]")
        #self.infofield.setStyleSheet("QGroupBox { border: none; }")
        self.main_layout.addWidget(self.infofieldNah, 1, 0)
        
        self.infofieldWar = InfoField("Temp. Waermetauscher [C]")
        #self.infofield.setStyleSheet("QGroupBox { border: none; }")
        self.main_layout.addWidget(self.infofieldWar, 2, 0)
        
        self.infofieldSub = InfoField("IDM_SUB1")
        #self.infofield.setStyleSheet("QGroupBox { border: none; }")
        self.main_layout.addWidget(self.infofieldSub, 0, 7)
        
        # Create Pump widget and add it to the grid layout
        self.pumpWidget1 = PumpWidget(name="Pumpe PU11")
        self.pumpWidget1.set_mode("idle")
        self.main_layout.addWidget(self.pumpWidget1, 4, 2, 1, 1)  # Add the Pump widget to the grid layout
        # pumpWidget11_center = self.pumpWidget.mapToGlobal(self.pumpWidget.geometry().center())
        # pumpWidget11_center_x = pumpWidget11_center.x()
        # pumpWidget11_center_y = pumpWidget11_center.y()
        
        
        """ self.motor1 = MotorLabelWidget("Ruehrwerk RW11", size=70)
        self.tankMixer1 = TankIBC(name="Fluessigvorl.", max_level=100, min_level=15)
        self.motor2 = MotorLabelWidget("Ruehrwerk RW12", size=70)
        self.tankMixer2 = TankIBC(name="Anmalschb", max_level=100, min_level=15) """
        
        self.tankMixer1 = TankMixerWidget()
        self.tankMixer1.set_tank_label("Fluessigvorl.")  # Set the tank label to "My Tank"
        self.tankMixer1.set_motor_mode('malfunction') 
        self.tankMixer1.set_level(50) # Set the level 
        self.tankMixer1.set_motorName_label("Ruehrwerk RW11")
        self.tankMixer1.motorName_label.setMinimumHeight(15)
        # self.tankMixer1.motorName_label.setContentsMargins(0,0,0,5)
        # self.tankMixer1.motor_label.setMinimumHeight(10)
        # self.tankMixer1.motor_label.setMargin(10)
        # self.tankMixer1.motorName_label.setAlignment(Qt.AlignHCenter)
        self.tankMixer1.setMinimumHeight(175)

        
        self.tankMixer2 = TankMixerWidget()
        self.tankMixer2.set_tank_label("Anmalschb")  # Set the tank label to "My Tank"
        self.tankMixer2.set_motor_mode('idle') 
        self.tankMixer2.set_level(50) # Set the level 
        self.tankMixer2.set_motorName_label("Ruehrwerk RW12")
        self.tankMixer2.motorName_label.setMinimumHeight(15)
        self.tankMixer2.setMinimumHeight(175)
        
        #self.main_layout.addWidget(self.motor1, 2, 2)
        self.main_layout.addWidget(self.tankMixer1, 4, 4, 2, 1)
        #self.main_layout.addWidget(self.motor2, 0, 3)
        self.main_layout.addWidget(self.tankMixer2, 1, 5, 2, 1)
        
        self.main_layout.setRowStretch(4, 0)
        self.main_layout.setRowStretch(3, 2)
        self.main_layout.setColumnStretch(2, 1)
        
        # Create and add Valve Widgets
        self.valve1 = ValveLabelWidget("Ventil AA11")
        self.main_layout.addWidget(self.valve1, 4, 5)

        self.valve2 = ValveLabelWidget("Ventil AA14")
        self.main_layout.addWidget(self.valve2, 0, 6)

        self.valve3 = ValveLabelWidget("Ventil AA13")
        self.main_layout.addWidget(self.valve3, 1, 6)

        self.valve4 = ValveLabelWidget("Ventil AA12")
        self.main_layout.addWidget(self.valve4, 2, 6)

        self.pumpLED = SingleLed(name="PU12 Rezi (Maisch)")
        self.main_layout.addWidget(self.pumpLED, 1, 7)
        
        self.pumpWidget = PumpWidget(name="Pumpe PU12")
        self.pumpWidget.set_mode("operational")
        self.main_layout.addWidget(self.pumpWidget, 2, 7, 1, 1)


        self.lines = []

    def resizeEvent(self, event):
        super().resizeEvent(event)

        tankIbc_center = self.tankIbc.geometry().center()
        tankIbc_center_x = tankIbc_center.x()
        tankIbc_center_y = tankIbc_center.y()

        pumpWidget11_center = self.pumpWidget1.geometry().center()
        pumpWidget11_center_x = pumpWidget11_center.x()
        pumpWidget11_center_y = pumpWidget11_center.y()

        # Update lines to draw
        self.lines = []
        self.add_line(tankIbc_center_x, tankIbc_center_y, pumpWidget11_center_x, pumpWidget11_center_y)
        
        # Trigger a repaint to see the lines
        self.update()












        # QTimer.singleShot(0, self.calculate_centers)

    # def calculate_centers(self):
    #     tankIbc_center = self.tankIbc.geometry().center()
    #     tankIbc_center_x = tankIbc_center.x()
    #     tankIbc_center_y = tankIbc_center.y()

    #     pumpWidget11_center = self.pumpWidget1.geometry().center()
    #     pumpWidget11_center_x = pumpWidget11_center.x()
    #     pumpWidget11_center_y = pumpWidget11_center.y()

    #     # Add lines to draw
    #     self.add_line(tankIbc_center_x, tankIbc_center_y, pumpWidget11_center_x, pumpWidget11_center_y)
        
    #     # Trigger a repaint to see the lines
    #     self.update()


        # # Add lines to draw
        # # self.add_line(0, 0, 100, 100)
        # self.add_line(100, 0, 200, 100)
        # self.add_line(tankIbc_center_x, tankIbc_center_y, pumpWidget11_center_x, pumpWidget11_center_y)
        # print(tankIbc_center_x, tankIbc_center_y, pumpWidget11_center_x, pumpWidget11_center_y)

        # # Trigger a repaint to see the lines
        # self.update()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Str1()
    window.show()

    sys.exit(app.exec_())