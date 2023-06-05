from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
# from components.faceplates.faceplate_gauge import Gauge
from components.faceplates.faceplate_on_off import OnOffButton
from components.faceplates.faceplate_fault import FaultBox
from components.faceplates.faceplate_fackel import FackelBox



class SideBarFaceplate(QGroupBox):
    """Mixer set of elements for the Strasse 1 tab

    :param QGroupBox: _description_
    :type QGroupBox: _type_
    """
    
    def __init__(self, name, layout, opcID=None):
        
        super().__init__(name) 
        self.layout = layout

        #Main laout of the side bar
        self.vbox = QVBoxLayout()
        self.vbox.setAlignment(Qt.AlignTop)

        self.on_of_lock = OnOffButton()
        self.vbox.addWidget(self.on_of_lock)

        self.fault_box = FaultBox()
        self.vbox.addWidget(self.fault_box)

        self.fackel_box = FackelBox(name="Fackel", layout = self.vbox)

        
        

        self.layout.addWidget(self)
        self.setLayout(self.vbox)





