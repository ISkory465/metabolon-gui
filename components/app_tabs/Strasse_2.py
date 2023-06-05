from PyQt5.QtWidgets    import *
from PyQt5.QtCore       import Qt
from ..faceplates.faceplates_new import Box
# from ..faceplates.faceplates import Box
from ..faceplates.faceplate_mixer  import Mixer
from ..faceplates.faceplate_endlager import Endlager
from ..faceplates.faceplate_tankibc import TankIBC
from ..faceplates.faceplate_valve import *



class Page():

    def UI(self,window:QMainWindow):

        #Main layout of the first tab 'Straße 1"
        self.vbox=QVBoxLayout()


        #Tab is split into three horizontal boxes
        self.hbox1 = QHBoxLayout()
        #self.hbox2 = QHBoxLayout()
        self.hbox2 = QGridLayout()
        self.hbox3 = QGridLayout()

        #First horizontal hbox1 layout contains three vertical boxes
        self.vbox1_1 = QVBoxLayout()
        self.vbox1_2 = QVBoxLayout()
        self.vbox1_3 = QVBoxLayout()

        #Layout relation
        self.vbox.addLayout(self.hbox1)
        self.vbox.addLayout(self.hbox2)
        self.vbox.addLayout(self.hbox3)
        self.vbox.setAlignment(Qt.AlignTop)
        self.hbox1.addLayout(self.vbox1_1)
        self.hbox1.addLayout(self.vbox1_2)
        self.hbox1.addLayout(self.vbox1_3)
        self.hbox1.setAlignment(Qt.AlignLeft)
        self.hbox2.setAlignment(Qt.AlignTop)


        window.tab2.setLayout(self.vbox)

        
        # hbox1 Content
        self.mixer1 = Mixer(name="Fermenter", layout = self.vbox1_1)
        self.mixer2 = Mixer(name="Nachgärer", layout = self.vbox1_2)
        self.endlager = Endlager(name="Endlager", layout = self.vbox1_3)

        # hbox2 Content
        #self.box1 = Box("PU12", self.hbox2)
        self.tankIbc = TankIBC(max_level=100, min_level=15)
        self.tankIbc.set_current_level(70)
        self.tankIbc.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        #self.hbox2.addWidget(self.tankIbc)
        #self.hbox2.setAlignment(Qt.AlignRight)
        
         # Create the TankIBC widget
        self.hbox2.addWidget(self.tankIbc.get_widget(), 3, 0)  # Add the tank widget to the grid layout
        self.hbox2.setColumnStretch(0, 0)

        # Create and add Valve Widgets
        self.valve1 = ValveLabelWidget("Ventil AA11")
        self.hbox2.addWidget(self.valve1, 3, 3)
        
        self.valve2 = ValveLabelWidget("Ventil AA12")
        self.hbox2.addWidget(self.valve2, 0, 4)

        self.valve3 = ValveLabelWidget("Ventil AA13")
        self.hbox2.addWidget(self.valve3, 1, 4)

        self.valve4 = ValveLabelWidget("Ventil AA14")
        self.hbox2.addWidget(self.valve4, 2, 4)

        # Create and add the Box widget
        self.box1 = Box("PU12", self.hbox3)
        self.hbox2.addWidget(self.box1, 3, 6)  # Add the box widget to the grid layout
        
        # hbox3 Content
        self.box2 = Box("PU11", self.hbox3)
        self.box3 = Box("RW11", self.hbox3)
        self.box4 = Box("RW12", self.hbox3)
        self.box5 = Box("AA11", self.hbox3)
        self.box6 = Box("AA12", self.hbox3)
        self.box7 = Box("AA13", self.hbox3)
        self.box8 = Box("AA14", self.hbox3)
        
        self.hbox3.addWidget(self.box2, 0, 0)
        self.hbox3.addWidget(self.box3, 0, 1)
        self.hbox3.addWidget(self.box4, 0, 3)
        self.hbox3.addWidget(self.box5, 0, 4)
        self.hbox3.addWidget(self.box6, 0, 5)
        self.hbox3.addWidget(self.box7, 0, 6)
        self.hbox3.addWidget(self.box8, 0, 7)

if __name__=='__main__':
    pass