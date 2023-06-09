from PyQt5.QtWidgets    import *
from PyQt5.QtCore       import Qt
#from ..faceplates.faceplates_new import Box
from ..faceplates.faceplates import Box
from ..faceplates.faceplate_mixer  import Mixer
from ..faceplates.faceplate_endlager import Endlager
from ..faceplates.faceplate_tankibc import TankIBC
from ..faceplates.faceplate_pump import PumpWidget
from ..faceplates.faceplate_valve import *
from ..faceplates.faceplates_infofieldV1 import *
from ..faceplates.faceplate_tank_mixer import *
from components.faceplates.faceplates_new import SingleLed

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
        self.hbox1.setAlignment(Qt.AlignLeft)
        self.hbox2.setAlignment(Qt.AlignTop)

        #Main layout assignment to the widget of the page
        self.setLayout(self.vbox)


        # hbox1 Content
        self.mixer1 = Mixer(name="Fermenter", layout=self.vbox1_1)
        self.mixer2 = Mixer(name="Nachgärer", layout=self.vbox1_2)
        self.endlager = Endlager(name="Endlager", layout=self.vbox1_3)

############################################################################################

        self.controlbox = QGridLayout()
        self.hbox1.addLayout(self.controlbox)

        ##### Ruhr Box #####

        # Create a group box
        group_box_ruhr = QGroupBox("Ruehrwerke controls")

        # Create a layout for the group box
        group_box_ruhr_layout = QHBoxLayout()

        # Ruhr box test
        ruhr_box_layout = QHBoxLayout()
        self.box3 = Box("RW11", ruhr_box_layout)
        self.box4 = Box("RW12", ruhr_box_layout)
        ruhr_box_layout.addWidget(self.box3)
        ruhr_box_layout.addWidget(self.box4)

        # Add the hbox1 layout to the group box layout
        group_box_ruhr_layout.addLayout(ruhr_box_layout)

        # Set the group box layout
        group_box_ruhr.setLayout(group_box_ruhr_layout)

        ###############################

        # Create a group box
        group_box_pumpe = QGroupBox("Pumpe controls")

        # Create a layout for the group box
        group_box_pumpe_layout = QHBoxLayout()

        # Pumpe box test
        pumpe_box_layout = QHBoxLayout()
        self.box1 = Box("PU12", pumpe_box_layout)
        self.box2 = Box("PU11", pumpe_box_layout)
        pumpe_box_layout.addWidget(self.box1)
        pumpe_box_layout.addWidget(self.box2)

        # Add the hbox1 layout to the group box layout
        group_box_pumpe_layout.addLayout(pumpe_box_layout)

        # Set the group box layout
        group_box_pumpe.setLayout(group_box_pumpe_layout)

        self.controlbox.addWidget(group_box_ruhr, 0, 0)
        self.controlbox.addWidget(group_box_pumpe, 1, 0)




############################################################################################

        # hbox2 Content
        
        # Create the TankIBC widget
        self.tankIbc = TankIBC(name="IBC", max_level=100, min_level=15)
        self.tankIbc.set_current_level(10)
        self.tankIbc.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        
        
        # Create the TankIBC widget
        self.hbox2.addWidget(self.tankIbc.get_widget(), 4, 0, 1, 1)  # Add the tank widget to the grid layout
        
        # Create infofield and add it to the grid 
        self.infofieldNah = InfoFieldV1("Temp. Nahwärmenetz [C]")
        #self.infofield.setStyleSheet("QGroupBox { border: none; }")
        self.hbox2.addWidget(self.infofieldNah, 1, 0)
        
        self.infofieldWar = InfoFieldV1("Temp. Wärmetauscher [C]")
        #self.infofield.setStyleSheet("QGroupBox { border: none; }")
        self.hbox2.addWidget(self.infofieldWar, 2, 0)
        
        self.infofieldSub = InfoFieldV1("IDM_SUB1")
        #self.infofield.setStyleSheet("QGroupBox { border: none; }")
        self.hbox2.addWidget(self.infofieldSub, 0, 7)
        
        # Create Pump widget and add it to the grid layout
        self.pumpWidget = PumpWidget(name="Pumpe PU11")
        self.pumpWidget.set_mode("idle")
        self.hbox2.addWidget(self.pumpWidget, 4, 2, 1, 1)  # Add the Pump widget to the grid layout
        
        
        """ self.motor1 = MotorLabelWidget("Rührwerk RW11", size=70)
        self.tankMixer1 = TankIBC(name="Flüssigvorl.", max_level=100, min_level=15)
        self.motor2 = MotorLabelWidget("Rührwerk RW12", size=70)
        self.tankMixer2 = TankIBC(name="Anmalschb", max_level=100, min_level=15) """
        
        self.tankMixer1 = TankMixerWidget()
        self.tankMixer1.set_tank_label("Flüssigvorl.")  # Set the tank label to "My Tank"
        self.tankMixer1.set_motor_mode('malfunction') 
        self.tankMixer1.set_level(50) # Set the level 
        self.tankMixer1.set_motorName_label("Rührwerk RW11")
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
        self.tankMixer2.set_motorName_label("Rührwerk RW12")
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
        self.valve1 = ValveLabelWidget("Ventil AA11")
        self.hbox2.addWidget(self.valve1, 4, 5)

        self.valve2 = ValveLabelWidget("Ventil AA14")
        self.hbox2.addWidget(self.valve2, 0, 6)

        self.valve3 = ValveLabelWidget("Ventil AA13")
        self.hbox2.addWidget(self.valve3, 1, 6)

        self.valve4 = ValveLabelWidget("Ventil AA12")
        self.hbox2.addWidget(self.valve4, 2, 6)

        self.pumpLED = SingleLed(name="PU12 Rezi (Maisch)", layout=(self.hbox2))
        self.hbox2.addWidget(self.pumpLED, 1, 7)
        
        self.pumpWidget = PumpWidget(name="Pumpe PU12")
        self.pumpWidget.set_mode("operational")
        self.hbox2.addWidget(self.pumpWidget, 2, 7, 1, 1)

        # Create and add the Box widget
        self.box1 = Box("PU12")
        self.hbox2.addWidget(self.box1, 4, 7, 1, 1, alignment=Qt.AlignRight)  # Add the box widget to the grid layout
        

        # hbox3 Content
        self.box2 = Box("PU11", self.hbox3)
        self.box3 = Box("RW11", self.hbox3)
        # self.box4 = Box("RW12", self.hbox3)
        self.box5 = Box("AA11", self.hbox3)
        self.box6 = Box("AA12", self.hbox3)
        self.box7 = Box("AA13", self.hbox3)
        self.box8 = Box("AA14", self.hbox3)
        
        # self.hbox3.addWidget(self.box2, 0, 0)
        # self.hbox3.addWidget(self.box3, 0, 1)
        # self.hbox3.addWidget(self.box4, 0, 3)
        self.hbox3.addWidget(self.box5, 0, 4)
        self.hbox3.addWidget(self.box6, 0, 5)
        self.hbox3.addWidget(self.box7, 0, 6)
        self.hbox3.addWidget(self.box8, 0, 7)
        
        # Set stretch factors for hbox2 and hbox3
        #self.vbox.addStretch(1)
        #self.hbox2.setColumnStretch(0, 1)
        #self.hbox2.setColumnStretch(5, 3)  
        #self.hbox3.setColumnStretch(7, 3)  
        
        self.hbox3.setContentsMargins(0, 50, 0, 0)
        self.hbox2.setContentsMargins(0, 0, 0, 10)

if __name__ == '__main__':
    pass


""" # Create the MixerTank and  add it to the gridlayout  
        self.tankMotor1 = TankMotor(nameTank="Flüssigvorl.", nameMotor="Rührwerk RW11", modeMotor="idle",
                                    maxTank=120, minTank=15)
        self.tankMotor2 = TankMotor(nameTank="Anmalschb", nameMotor="Rührwerk RW12", modeMotor="idle",
                                    maxTank=120, minTank=15)

        self.hbox2.addWidget(self.tankMotor1, 4, 2)
        self.hbox2.addWidget(self.tankMotor2, 2, 3)  
"""