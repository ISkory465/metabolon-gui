from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from components.faceplates.faceplate_gauge import Gauge
from components.faceplates.faceplate_on_off import OnOffButton



class SideBarFaceplate(QGroupBox):
    """Mixer set of elements for the Strasse 1 tab

    :param QGroupBox: _description_
    :type QGroupBox: _type_
    """
    
    def __init__(self, name, layout, opcID=None):
        
        super().__init__(name) 
        self.layout = layout

        #Main laout of the side bar
        self.hbox = QVBoxLayout()
        self.hbox.setAlignment(Qt.AlignTop)

        self.on_of_lock = OnOffButton()
        self.hbox.addWidget(self.on_of_lock)

        self.gauge = Gauge()
        self.hbox.addWidget(self.gauge)

        
        

        self.layout.addWidget(self)
        self.setLayout(self.hbox)





