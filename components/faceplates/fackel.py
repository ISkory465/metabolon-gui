# Importing necessary modules
from PyQt5.QtWidgets import QLabel, QGroupBox, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import Qt

# Importing necessary components
from components.widgets.box import Box

from components.widgets.infofield_dbl import InfoField

class Indicator(QLabel):
    """Indicator is a custom QLabel that changes its background color based on state. It represents the current state of the fackel"""

    def __init__(self,name, parent=None):
        super().__init__(parent)
        self.setAlignment(Qt.AlignCenter)
        self.opcName=name
        # self.setAlignment(Qt.AlignLeft)
        self.setFixedSize(30, 120)
        self.set_state('idle')  # Set default state

    def set_state(self, state):
        """Update the indicator's style based on the state."""
        styles = {
            'active': "border: 1px solid black; background-color: green;",
            'idle': "border: 1px solid black; background-color: blue;",
            'error': "border: 1px solid black; background-color: red;",
        }
        try:
            self.setStyleSheet(styles[state])
        except KeyError:
            print(f'Unknown state: {state}')
    def update(self,val:dict):
        try:
          Auf:bool
          error1:bool
          Auf=val[self.opcName+':Auf']
          error1=val[self.opcName+':error1']


          if error1:
            self.set_state('error')
          elif Auf:
            self.set_state('active')
          else:
            self.set_state('idle')
          #print('If Statement done')
        except Exception as e:
          print('Exception raised')
          #print(val[self.opcName])
          print(str(e))
class FackelBox(QGroupBox):
    """FackelBox is a custom QGroupBox that encapsulates Fackel related UI elements."""

    def __init__(self, name, opcID=None):
        super().__init__(name)

        self.opcID = opcID  # TODO: add OPC functionality

        # Initialize the main layout
        main_layout = QHBoxLayout()
        self.setLayout(main_layout)

        # Initialize columns
        col1, col2, col3 = QVBoxLayout(), QVBoxLayout(), QVBoxLayout()

        # Add columns to the main layout
        main_layout.addLayout(col1)
        main_layout.addLayout(col2)
        main_layout.addLayout(col3)

        # # Initialize and add InfoField instances to col1
        self.fackel_fer1 = InfoField("Fackel Ein \nFer1 [mbar]", buttonSymbol=1, max_width=100)
        col1.addWidget(self.fackel_fer1)
        self.fackel_fer2 = InfoField("Fackel Ein \nFer2 [mbar]", buttonSymbol=1, max_width=100)
        col1.addWidget(self.fackel_fer2)
        self.fackel_s = InfoField("[s]", max_width=100)
        col1.addWidget(self.fackel_s)

        # Initialize and add the indicator to col2
        self.indicator = Indicator(name="Fackel Indicator")
        col2.addWidget(self.indicator)

        # Initialize and add Fackel controls to col3
        self.fackel_controls = Box("Control mode", horizontal_spacing=10, width=100)
        col3.addWidget(self.fackel_controls)
    def update(self,inputs: dict):
        """method to update all objects in current tab periodically after reading the values in different thread

        :param inputs: tag values
        :type inputs: dict
        """
        objectList=[    self.fackel_fer1,
                        self.fackel_fer2,
                        self.fackel_s,
                        self.indicator,
                        self.fackel_controls
                    ]


        for o in objectList:
            #iterate over an update method that should be added to all faceplate objects similar to box object
            o.update(inputs)