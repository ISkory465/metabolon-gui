from PyQt5.QtWidgets    import *
from PyQt5.QtCore       import Qt
from ..widgets.box import Box
from ..faceplates.mixer  import Mixer
from ..faceplates.endlager import Endlager
from ..faceplates.tankibc import TankIBC
from ..widgets.pump import PumpWidget
from ..widgets.valve import *
from ..widgets.infofield_dbl import *
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

def half_dist_coor(coor1, coor2):
        return int((coor2-coor1)/2)



def create_group_box(title, boxes):
    # Create a group box
    group_box = QGroupBox(title)

    # Create a vertical layout for the group box
    group_box_layout = QVBoxLayout()

    # Iterate over each pair of boxes
    for i in range(0, len(boxes), 2):
        # Create a horizontal box layout and add the pair of boxes to it
        box_layout = QHBoxLayout()
        for box in boxes[i:i+2]:
            box_layout.addWidget(box)

        # Add the box layout to the group box layout
        box_layout.setAlignment(Qt.AlignTop)
        group_box_layout.addLayout(box_layout)
        group_box_layout.setAlignment(Qt.AlignTop)

    # Set the group box layout
    group_box.setLayout(group_box_layout)

    return group_box


class Page(LineDrawer):

    def __init__(self) -> None:
        super().__init__()
        self.UI()
         

    def UI(self):

        #Main layout of the first tab 'Straße 1"
        self.vbox=QVBoxLayout()


        #Tab is split into three horizontal boxes
        self.hbox1 = QHBoxLayout()
        self.hbox2 = QGridLayout()
        self.hbox3 = QGridLayout()
        
        # First horizontal hbox1 layout contains three vertical boxes
        self.vbox1_1 = QVBoxLayout()
        self.vbox1_2 = QVBoxLayout()
        self.vbox1_3 = QVBoxLayout()


        # Layout relation
        self.vbox.addLayout(self.hbox1)
        self.vbox.addLayout(self.hbox2)
        self.vbox.addLayout(self.hbox3)
        self.vbox.setAlignment(Qt.AlignTop)
        self.hbox1.addLayout(self.vbox1_1)
        self.hbox1.addLayout(self.vbox1_2)
        self.hbox1.addLayout(self.vbox1_3)
        self.vbox1_1.setAlignment(Qt.AlignTop)
        self.vbox1_2.setAlignment(Qt.AlignTop)
        self.vbox1_3.setAlignment(Qt.AlignTop)
        self.hbox1.setAlignment(Qt.AlignLeft)
        self.hbox2.setAlignment(Qt.AlignTop)

        #Main layout assignment to the widget of the page
        self.setLayout(self.vbox)


        # hbox1 Content
        self.mixer1 = Mixer(name="Fermenter")
        self.vbox1_1.addWidget(self.mixer1)
        
        self.mixer2 = Mixer(name="Nachgaerer")
        self.vbox1_2.addWidget(self.mixer2)

        self.endlager = Endlager(name="Endlager")
        self.vbox1_3.addWidget(self.endlager)

        self.hbox1_4 = QHBoxLayout()
        self.hbox1.addLayout(self.hbox1_4)

        self.vbox_h_1_4 = QVBoxLayout() 
        self.vbox_h_1_4.setAlignment(Qt.AlignTop)
        self.hbox1_4.addLayout(self.vbox_h_1_4)
        self.hbox1_4.setAlignment(Qt.AlignTop)

        # Create the boxes
        pump1 = Box("PU12")
        pump2 = Box("PU11")
        ruhr1 = Box("RW11")
        ruhr2 = Box("RW12")
        vent1 = Box("AA11")
        vent2 = Box("AA12")
        vent3 = Box("AA13")
        vent4 = Box("AA14")

        # Create the group boxes
        group_box_ruhr = create_group_box("Ruehrwerke controls", [ruhr1, ruhr2])
        group_box_pumpe = create_group_box("Pumpe controls", [pump1, pump2])
        group_box_vents = create_group_box("Vents controls", [vent1, vent2, vent3, vent4])

        self.vbox_h_1_4.addWidget(group_box_ruhr)
        self.vbox_h_1_4.addWidget(group_box_pumpe)
        self.vbox_h_1_4.setAlignment(Qt.AlignTop)
        self.hbox1_4.addWidget(group_box_vents)





############################################################################################

        # hbox2 Content
        
        # Create the TankIBC widget
        self.tankIbc = TankIBC(name="IBC", max_level=100, min_level=15)
        self.tankIbc.set_current_level(10)
        
        
        # Create the TankIBC widget
        self.hbox2.addWidget(self.tankIbc.get_widget(), 4, 0, 1, 1)  # Add the tank widget to the grid layout
        
        # Create infofield and add it to the grid 
        self.infofieldNah = InfoField("Temp. Nahwaermenetz [C]")
        self.hbox2.addWidget(self.infofieldNah, 0, 0)
        
        self.infofieldWar = InfoField("Temp. Waermetauscher [C]")
        self.hbox2.addWidget(self.infofieldWar, 1, 0)
        
        self.infofieldSub = InfoField("IDM_SUB1")
        self.hbox2.addWidget(self.infofieldSub, 0, 8)
        
        # Create Pump widget and add it to the grid layout
        self.pumpWidget1 = PumpWidget(name="Pumpe PU11")
        self.pumpWidget1.set_mode("idle")
        self.hbox2.addWidget(self.pumpWidget1, 4, 2, 1, 1)  # Add the Pump widget to the grid layout

        
        self.tankMixer1 = TankMixerWidget()
        self.tankMixer1.set_tank_label("Fluessigvorl.")  # Set the tank label to "My Tank"
        self.tankMixer1.set_motor_mode('malfunction') 
        self.tankMixer1.set_level(50) # Set the level 
        self.tankMixer1.set_motorName_label("Ruehrwerk RW11")
        self.tankMixer1.motorName_label.setMinimumHeight(15)
        self.tankMixer1.setMinimumHeight(175)

        
        self.tankMixer2 = TankMixerWidget()
        self.tankMixer2.set_tank_label("Anmalschb")  # Set the tank label to "My Tank"
        self.tankMixer2.set_motor_mode('idle') 
        self.tankMixer2.set_level(50) # Set the level 
        self.tankMixer2.set_motorName_label("Ruehrwerk RW12")
        self.tankMixer2.motorName_label.setMinimumHeight(15)
        self.tankMixer2.setMinimumHeight(175)
        
        self.hbox2.addWidget(self.tankMixer1, 4, 3, 2, 1)
        self.hbox2.addWidget(self.tankMixer2, 1, 5, 2, 1)
        
        self.hbox2.setRowStretch(1, 0)
        self.hbox2.setRowStretch(2, 0)
        self.hbox2.setRowStretch(3, 0)
        self.hbox2.setRowStretch(4, 0)
        self.hbox2.setColumnStretch(1, 0)
        self.hbox2.setColumnStretch(2, 0)
        self.hbox2.setColumnStretch(3, 0)
        self.hbox2.setColumnStretch(4, 0)
        self.hbox2.setColumnStretch(5, 0)
        self.hbox2.setColumnStretch(6, 0)
        self.hbox2.setColumnStretch(7, 0)
        
        # Create and add Valve Widgets
        self.valve1 = ValveLabelWidget("Ventil AA11")
        self.hbox2.addWidget(self.valve1, 4, 5)

        self.valve2 = ValveLabelWidget("Ventil AA14")
        self.hbox2.addWidget(self.valve2, 0, 6, 1, 3)

        self.valve3 = ValveLabelWidget("Ventil AA13")
        self.hbox2.addWidget(self.valve3, 1, 6)

        self.valve4 = ValveLabelWidget("Ventil AA12")
        self.hbox2.addWidget(self.valve4, 2, 6)

        self.pumpLED = SingleLed(name="PU12 Rezi (Maisch)")
        self.hbox2.addWidget(self.pumpLED, 1, 8)
        
        self.pumpWidget = PumpWidget(name="Pumpe   PU12")
        self.pumpWidget.set_mode("operational")
        self.hbox2.addWidget(self.pumpWidget, 2, 7)


        self.lines = []

    def resizeEvent(self, event):
        super().resizeEvent(event)

        # Fermenter center
        fermenter_center = self.mixer1.geometry().center()
        fermenter_center_x = fermenter_center.x()
        fermenter_center_y = fermenter_center.y()

        # Nachgaerer center
        nah_center = self.mixer2.geometry().center()
        nah_center_x = nah_center.x()
        nah_center_y = nah_center.y()          

        # Endlager center
        endlager_center = self.endlager.geometry().center()
        endlager_center_x = endlager_center.x()
        endlager_center_y = endlager_center.y() 

        # IBC tank center
        tankIbc_center = self.tankIbc.geometry().center()
        tankIbc_center_x = tankIbc_center.x()
        tankIbc_center_y = tankIbc_center.y()

        # Pump11 center
        pumpWidget11_center = self.pumpWidget1.geometry().center()
        pumpWidget11_center_x = pumpWidget11_center.x()
        pumpWidget11_center_y = pumpWidget11_center.y()

        # Mixer tank 1 center
        tankMixer1_center = self.tankMixer1.geometry().center()
        tankMixer1_center_x = tankMixer1_center.x()
        tankMixer1_center_y = tankMixer1_center.y()

        # Ventil 11 center
        valve1_center = self.valve1.geometry().center()
        valve1_center_x = valve1_center.x()
        valve1_center_y = valve1_center.y()

        # Mixer tank 2 center
        tankMixer2_center = self.tankMixer2.geometry().center()
        tankMixer2_center_x = tankMixer2_center.x()
        tankMixer2_center_y = tankMixer2_center.y()

        # Ventil 12 center
        valve4_center = self.valve4.geometry().center()
        valve4_center_x = valve4_center.x()
        valve4_center_y = valve4_center.y()  + 9 

        # Ventil 13 center
        valve3_center = self.valve3.geometry().center()
        valve3_center_x = valve3_center.x()
        valve3_center_y = valve3_center.y()

        # Ventil 14 center
        valve2_center = self.valve2.geometry().center()
        valve2_center_x = valve2_center.x()
        valve2_center_y = valve2_center.y()

        # Pump 12 center
        pump12_center = self.pumpWidget.geometry().center()
        pump12_center_x = pump12_center.x()
        pump12_center_y = pump12_center.y()

        # Update lines to draw
        self.lines = []

        # Bottom
        self.add_line(tankIbc_center_x, tankIbc_center_y+9, pumpWidget11_center_x, pumpWidget11_center_y+9)
        self.add_line(pumpWidget11_center_x, pumpWidget11_center_y+9, pumpWidget11_center_x+30, pumpWidget11_center_y+9)
        self.add_line(pumpWidget11_center_x+30, pumpWidget11_center_y+9, pumpWidget11_center_x+30, tankMixer1_center_y+20)
        self.add_line(pumpWidget11_center_x+30, tankMixer1_center_y+20, pumpWidget11_center_x+60, tankMixer1_center_y+20)
        self.add_line(pumpWidget11_center_x+60, tankMixer1_center_y+20, valve1_center_x-45, tankMixer1_center_y+20)
        self.add_line(valve1_center_x-45, tankMixer1_center_y+20, valve1_center_x-45, valve1_center_y+10)
        self.add_line(valve1_center_x-45, valve1_center_y+10, valve1_center_x, valve1_center_y+10)

        self.add_line(valve1_center_x, valve1_center_y+9,
                      valve4_center_x + half_dist_coor(valve4_center_x, pump12_center_x), valve1_center_y+9)

        # Mid
        self.add_line(tankMixer2_center_x, valve4_center_y, valve4_center_x, valve4_center_y)
        self.add_line(tankMixer2_center_x, valve3_center_y+45, valve3_center_x + half_dist_coor(valve3_center_x, tankMixer2_center_x), valve3_center_y+45)
        self.add_line(valve3_center_x + half_dist_coor(valve3_center_x, tankMixer2_center_x), valve3_center_y+45,
                      valve3_center_x + half_dist_coor(valve3_center_x, tankMixer2_center_x), valve3_center_y+9)
        self.add_line(valve3_center_x + half_dist_coor(valve3_center_x, tankMixer2_center_x), valve3_center_y+9,
                      valve3_center_x, valve3_center_y+9)
        
        self.add_line(valve4_center_x, valve4_center_y, pump12_center_x, pump12_center_y+9)
        self.add_line(pump12_center_x, pump12_center_y+9, pump12_center_x, valve2_center_y+9)
        self.add_line(valve3_center_x, valve3_center_y+9, pump12_center_x, valve3_center_y+9)

        # Top
        self.add_line(fermenter_center_x+100, fermenter_center_y+210, nah_center_x-100, nah_center_y+210)
        self.add_line(fermenter_center_x+100, fermenter_center_y+210, fermenter_center_x+100, fermenter_center_y+198)
        self.add_line(nah_center_x-100, nah_center_y+210, nah_center_x-100, nah_center_y+198)

        self.add_line(fermenter_center_x+185, fermenter_center_y+210, fermenter_center_x+185, fermenter_center_y+225)
        self.add_line(fermenter_center_x+185, fermenter_center_y+225, endlager_center_x, fermenter_center_y+225)
        self.add_line(endlager_center_x, fermenter_center_y+225, endlager_center_x, endlager_center_y+147)

        self.add_line(valve2_center_x, valve2_center_y+9, pump12_center_x, valve2_center_y+9)
        self.add_line(nah_center_x, valve2_center_y+9, valve2_center_x, valve2_center_y+9)
        self.add_line(nah_center_x, fermenter_center_y+225, nah_center_x, valve2_center_y+9)

        # Bottom to Mid
        self.add_line(valve4_center_x + half_dist_coor(valve4_center_x, pump12_center_x), valve1_center_y+9,
                      valve4_center_x + half_dist_coor(valve4_center_x, pump12_center_x), valve4_center_y)
        

        # Trigger a repaint to see the lines
        self.update()


if __name__ == '__main__':
    pass