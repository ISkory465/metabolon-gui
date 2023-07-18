# Importing necessary modules
from PyQt5.QtWidgets import QGroupBox, QVBoxLayout, QHBoxLayout, QWidget, QScrollArea
from PyQt5.QtCore import Qt
from QLed import QLed

# Importing necessary components
## Buttons
from components.widgets.control_lock import OnOffButton
from components.widgets.email_button import EmailButton
from components.widgets.stop_button import STOPButton
## Boxes
from components.faceplates.fault_reporting import FaultBox
from components.faceplates.fackel import FackelBox
## LEDs
from components.widgets.leds import SingleLed, LedGroupBox


class SideBarFaceplate(QGroupBox):
    """
    The collection of side bar widgets put together.
    Inherits from QGroupBox.
    """
    def __init__(self, name, opcID=None):
        super().__init__(name) 

        # Main layout of the sidebar
        self.vbox = QVBoxLayout()
        self.vbox.setAlignment(Qt.AlignTop) # might not be necessary at this point

        # Instantiate components and add to the layout
        # Controls (user input) lock button
        self.on_off_lock = OnOffButton()
        self.vbox.addWidget(self.on_off_lock)

        # Fault reporting box
        self.fault_box = FaultBox()
        self.vbox.addWidget(self.fault_box)

        # Fackel (torch) operation block
        self.fackel_box = FackelBox(name="Fackel")
        self.vbox.addWidget(self.fackel_box)
        
        # Controls box
        self.stoerungBox = LedGroupBox("Stoerungen", ["ML Sammelstoerung",
                                                      "FE01 (Einspeisung / Steuerspannung)",
                                                      "FE02 (Antriebe Pumpen / Diverse)",
                                                      "FE03 (Antriebe Ruehrwerke)",
                                                      "FE04 (SPS / MSR Technik)"], [QLed.Red] * 5)
        self.vbox.addWidget(self.stoerungBox)
        self.stoerungBox.set_led_state(0, True)


        # Pump status
        self.pumpeLED = SingleLed(name="Pumpe PU31 (Mobil)")
        self.vbox.addWidget(self.pumpeLED)

        # Email notifications button
        self.email = EmailButton()
        self.vbox.addWidget(self.email)

        # Instantiate STOP buttons and add them to a horizontal layout
        stop_hbox = QHBoxLayout()
        self.stop1 = STOPButton(name="Stop 2")
        self.stop2 = STOPButton(name="Stop")
        stop_hbox.addWidget(self.stop1)
        stop_hbox.addWidget(self.stop2)
        self.vbox.addLayout(stop_hbox) # add two buttons to the main layout

        # Set layout in a container, add to a scroll area
        # This is needed to ensure the whole side bar is not shifted in the full-screen mode
        container = QWidget()
        container.setLayout(self.vbox)
        scroll = QScrollArea()
        scroll.setWidget(container)
        scroll.setWidgetResizable(True)
        scroll.setMaximumWidth(400)  # Set maximum width of the scroll area

        # Set scroll area as the layout of SideBarFaceplate
        layout = QVBoxLayout(self)
        layout.addWidget(scroll)
    def updateAll(self, inputs: dict):
        """method to update all objects in current tab periodically after reading the values in different thread

        :param inputs: tag values
        :type inputs: dict
        """
        objectList = [
            self.fackel_box,
            self.stoerungBox,
            self.pumpeLED

        ]

        for o in objectList:
            #iterate over an update method that should be added to all faceplate objects similar to box object
            o.update(inputs)
        