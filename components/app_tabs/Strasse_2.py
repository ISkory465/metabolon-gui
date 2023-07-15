from PyQt5.QtWidgets    import *
from PyQt5.QtCore       import Qt
#from ..faceplates.faceplates_new import Box
from ..widgets.box import Box,BoxV2
from ..faceplates.mixer  import Mixer
from ..faceplates.endlager import Endlager
from ..faceplates.tankibc import TankIBC
from ..widgets.pump import PumpWidget
from ..widgets.valve import *
from ..widgets.infofield_dbl import *
from ..faceplates.tank_mixer import *
from components.widgets.leds import SingleLed

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


class Page(QWidget):

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
        self.pump1 = Box("PU22")
        self.pump2 = Box("PU21")
        self.ruhr1 = Box("RW21")
        self.ruhr2 = Box("RW22")
        self.vent1 = BoxV2("AA21")
        self.vent2 = BoxV2("AA22")
        self.vent3 = BoxV2("AA23")
        self.vent4 = BoxV2("AA24")

        # Create the group boxes
        group_box_ruhr = create_group_box("Ruehrwerke controls", [self.ruhr1, self.ruhr2])
        group_box_pumpe = create_group_box("Pumpe controls", [self.pump1, self.pump2])
        group_box_vents = create_group_box("Vents controls", [self.vent1, self.vent2, self.vent3, self.vent4])

        self.vbox_h_1_4.addWidget(group_box_ruhr)
        self.vbox_h_1_4.addWidget(group_box_pumpe)
        self.vbox_h_1_4.setAlignment(Qt.AlignTop)
        self.hbox1_4.addWidget(group_box_vents)





############################################################################################

        # hbox2 Content
        
        # Create the TankIBC widget
        self.tankIbc = TankIBC(name="IBC", max_level=100, min_level=15)
        self.tankIbc.set_current_level(10)
        self.tankIbc.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        
        
        # Create the TankIBC widget
        self.hbox2.addWidget(self.tankIbc.get_widget(), 4, 0, 1, 1)  # Add the tank widget to the grid layout
        
        # # Create infofield and add it to the grid 
        # self.infofieldNah = InfoField("Temp. Nahwaermenetz [C]")
        # #self.infofield.setStyleSheet("QGroupBox { border: none; }")
        # self.hbox2.addWidget(self.infofieldNah, 1, 0)
        
        # self.infofieldWar = InfoField("Temp. Waermetauscher [C]")
        # #self.infofield.setStyleSheet("QGroupBox { border: none; }")
        # self.hbox2.addWidget(self.infofieldWar, 2, 0)
        
        self.infofieldSub = InfoField("IDM_SUB2",dec_num=3)
        #self.infofield.setStyleSheet("QGroupBox { border: none; }")
        self.hbox2.addWidget(self.infofieldSub, 0, 7)
        
        # Create Pump widget and add it to the grid layout
        self.pumpWidget1 = PumpWidget(name="Pumpe PU21")
        self.pumpWidget1.set_mode("idle")
        self.hbox2.addWidget(self.pumpWidget1, 4, 2, 1, 1)  # Add the Pump widget to the grid layout
        
        
        """ self.motor1 = MotorLabelWidget("Ruehrwerk RW11", size=70)
        self.tankMixer1 = TankIBC(name="Fluessigvorl.", max_level=100, min_level=15)
        self.motor2 = MotorLabelWidget("Ruehrwerk RW12", size=70)
        self.tankMixer2 = TankIBC(name="Anmalschb", max_level=100, min_level=15) """
        
        self.tankMixer1 = TankMixerWidget(name='Fluessigvorl')
        self.tankMixer1.set_tank_label("Fluessigvorl.")  # Set the tank label to "My Tank"
        self.tankMixer1.set_motor_mode('malfunction') 
        self.tankMixer1.set_level(50) # Set the level 
        self.tankMixer1.set_motorName_label("Ruehrwerk RW21")
        self.tankMixer1.motorName_label.setMinimumHeight(15)
        # self.tankMixer1.motorName_label.setContentsMargins(0,0,0,5)
        # self.tankMixer1.motor_label.setMinimumHeight(10)
        # self.tankMixer1.motor_label.setMargin(10)
        # self.tankMixer1.motorName_label.setAlignment(Qt.AlignHCenter)
        self.tankMixer1.setMinimumHeight(175)

        
        self.tankMixer2 = TankMixerWidget(name='Anmalschb')
        self.tankMixer2.set_tank_label("Anmalschb")  # Set the tank label to "My Tank"
        self.tankMixer2.set_motor_mode('idle') 
        self.tankMixer2.set_level(50) # Set the level 
        self.tankMixer2.set_motorName_label("Ruehrwerk RW22")
        self.tankMixer2.motorName_label.setMinimumHeight(15)
        self.tankMixer2.setMinimumHeight(175)
        
        #self.hbox2.addWidget(self.motor1, 2, 2)
        self.hbox2.addWidget(self.tankMixer1, 3, 4, 4, 1)
        #self.hbox2.addWidget(self.motor2, 0, 3)
        self.hbox2.addWidget(self.tankMixer2, 1, 5, 2, 1)
        
        self.hbox2.setRowStretch(4, 0)
        self.hbox2.setRowStretch(3, 2)
        self.hbox2.setColumnStretch(2, 1)
        
        # Create and add Valve Widgets
        self.valve1 = ValveLabelWidget("Ventil AA21")
        self.hbox2.addWidget(self.valve1, 4, 5)

        self.valve2 = ValveLabelWidget("Ventil AA24")
        self.hbox2.addWidget(self.valve2, 0, 6)

        self.valve3 = ValveLabelWidget("Ventil AA23")
        self.hbox2.addWidget(self.valve3, 1, 6)

        self.valve4 = ValveLabelWidget("Ventil AA22")
        self.hbox2.addWidget(self.valve4, 2, 6)

        self.pumpLED = SingleLed(name="PU22 Rezi (Maisch)")
        self.hbox2.addWidget(self.pumpLED, 1, 7)
        
        self.pumpWidget = PumpWidget(name="Pumpe PU22")
        self.pumpWidget.set_mode("operational")
        self.hbox2.addWidget(self.pumpWidget, 2, 7, 1, 1)
    def updateAll(self, inputs: dict):
        """method to update all objects in current tab periodically after reading the values in different thread

        :param inputs: tag values
        :type inputs: dict
        """
        objectList = [
            self.mixer1,
            self.mixer2,
            self.endlager,
            self.pump1,
            self.pump2,
            self.ruhr1,
            self.ruhr2,
            self.vent1,
            self.vent2,
            self.vent3,
            self.vent4,
            self.infofieldSub
            
        ]

        for o in objectList:
            #iterate over an update method that should be added to all faceplate objects similar to box object
            o.update(inputs)
        
        objectList2=[    #self.playbutton,
                        self.tankIbc,
                        self.valve1,
                        self.valve2,
                        self.valve3,
                        self.valve4,
                        self.pumpWidget1,
                        self.pumpWidget,
                        self.tankMixer1,
                        self.tankMixer2
                        
                    ]


        for i in objectList2:
            #iterate over an update method that should be added to all faceplate objects similar to box object
            i.update1(inputs)

if __name__ == '__main__':
    pass


""" # Create the MixerTank and  add it to the gridlayout  
        self.tankMotor1 = TankMotor(nameTank="Fluessigvorl.", nameMotor="Ruehrwerk RW11", modeMotor="idle",
                                    maxTank=120, minTank=15)
        self.tankMotor2 = TankMotor(nameTank="Anmalschb", nameMotor="Ruehrwerk RW12", modeMotor="idle",
                                    maxTank=120, minTank=15)

        self.hbox2.addWidget(self.tankMotor1, 4, 2)
        self.hbox2.addWidget(self.tankMotor2, 2, 3)  
"""