from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
# from components.faceplates.faceplate_gauge import Gauge
from components.faceplates.faceplate_on_off import OnOffButton
from components.faceplates.faceplate_fault import FaultBox
from components.faceplates.faceplate_fackel import FackelBox
from components.faceplates.faceplates_new import Led_5, SingleLed
from components.faceplates.faceplate_email_button import EmailButton
from components.faceplates.faceplate_stop_button import STOPButton



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

        self.on_off_lock = OnOffButton()
        self.vbox.addWidget(self.on_off_lock)

        self.fault_box = FaultBox()
        self.vbox.addWidget(self.fault_box)

        self.fackel_box = FackelBox(name="Fackel", layout = self.vbox)

        self.stoerungBox = Led_5(box_name="Stoerungen", name="ML Sammelstoerung\
                            ,FE01 (Einspeisung / Steuerspannung)\
                            ,FE02 (Antriebe Pumpen / Diverse)\
                            ,FE03 (Antriebe Ruehrwerke)\
                            ,FE04 (SPS / MSR Technik)", layout = self.vbox)
        
        self.pumpeLED = SingleLed(name="Pumpe PU31 (Mobil)", layout = self.vbox)

        self.email = EmailButton()
        self.vbox.addWidget(self.email)

        stop_hbox = QHBoxLayout()
        self.stop1 = STOPButton(name="Stop 2")
        self.stop2 = STOPButton(name="Stop")
        stop_hbox.addWidget(self.stop1)
        stop_hbox.addWidget(self.stop2)
        self.vbox.addLayout(stop_hbox)
        
        

        self.layout.addWidget(self)
        self.setLayout(self.vbox)





