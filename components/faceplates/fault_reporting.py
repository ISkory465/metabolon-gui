from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout, QPushButton, QFormLayout
from PyQt5.QtCore import Qt
from QLed import QLed

# TODO: add OPC functionality

class SingleLed(QWidget):
    def __init__(self, opcID='opcID'):
        super().__init__()
        local_layout = QFormLayout()
        
        # LED setup
        self.led = QLed(onColour=QLed.Green, shape=QLed.Circle)
        self.led.value = True  # Start state of LED
        
        # Configuring the layout
        local_layout.addRow(self.led)  # add LED to the layout
        local_layout.setVerticalSpacing(8)
        local_layout.setFormAlignment(Qt.AlignLeft)
        local_layout.setHorizontalSpacing(25)
        self.setLayout(local_layout)
        
        # Configure widget size
        self.setFixedHeight(40)
        self.setFixedWidth(40)
        

    def update(self, val:dict):
        self.led.value = val[self.opcName]  # Updates the LED status


class FaultBox(QWidget):
    def __init__(self, opcID=None):
        super().__init__()
        main_vbox = QVBoxLayout()  # Main layout
        
        # Create and add title label to the layout
        label = QLabel("Stoerung Quittieren")
        label.setAlignment(Qt.AlignCenter)
        main_vbox.addWidget(label)

        # Row for button and LED
        row2 = QHBoxLayout()
        
        # Toggle button setup and connection to slot function
        self.button = QPushButton("Quittieren")
        self.button.clicked.connect(self.toggleActive)
        row2.addWidget(self.button)
        
        # Single LED setup and adding to the layout
        self.led_layout = QVBoxLayout()
        self.single_led = SingleLed("LED")
        self.led_layout.addWidget(self.single_led)
        row2.addLayout(self.led_layout)
        
        main_vbox.addLayout(row2)
        self.setLayout(main_vbox)

    # Slot function to toggle the LED on button press
    def toggleActive(self):
        self.single_led.led.value = not self.single_led.led.value
