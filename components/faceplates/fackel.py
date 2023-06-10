# Importing necessary modules
from PyQt5.QtWidgets import QLabel, QGroupBox, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import Qt

# Importing necessary components
from components.widgets.box import Box
from components.widgets.infofield_dbl import InfoField

class Indicator(QLabel):
    """Indicator is a custom QLabel that changes its background color based on state. It represents the current state of the fackel"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAlignment(Qt.AlignCenter)
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

        # Initialize and add InfoField instances to col1
        self.fackel_fer1 = InfoField("Fackel Ein \nFer1 [mbar]", col1, buttonSymbol=1)
        self.fackel_fer2 = InfoField("Fackel Ein \nFer2 [mbar]", col1, buttonSymbol=1)
        self.fackel_s = InfoField("[s]", col1)

        # Initialize and add the indicator to col2
        self.indicator = Indicator()
        col2.addWidget(self.indicator)

        # Initialize and add Fackel controls to col3
        self.fackel_controls = Box("Control mode", col3, horizontal_spacing=10, width=100)
