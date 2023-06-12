from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from QLed import QLed


class SingleLed(QGroupBox):
    def __init__(self, name, opcID='opcID'):
        super().__init__()
        self.opcName = name
        local_layout = QFormLayout()

        # LED setup
        self.name = QLabel(name)
        self.led = QLed(onColour=QLed.Green, shape=QLed.Circle)

        # Add if-condition with opc input
        self.led.value = True

        local_layout.addRow(self.name, self.led)
        

        #Settings:
        self.setFixedHeight(50)
        self.setFixedWidth(200)
        local_layout.setVerticalSpacing(8)
        local_layout.setFormAlignment(Qt.AlignLeft)
        local_layout.setHorizontalSpacing(25)

        self.setLayout(local_layout)

    def update(self,val:dict):
        self.led.value=val[self.opcName]



class LedGroupBox(QGroupBox):
    def __init__(self, box_name, led_names, led_colors, opcID='opcID'):
        super().__init__(box_name)

        local_layout = QFormLayout()

        self.leds = []

        for i in range(len(led_names)):
            led = QLed(onColour=led_colors[i], shape=QLed.Circle)
            self.leds.append(led)

            # Add if-condition with opc input
            led.value = False

            local_layout.addRow(led, QLabel(led_names[i]))

        # Settings:
        self.setFixedHeight(200)
        self.setFixedWidth(300)
        local_layout.setFormAlignment(Qt.AlignLeft)
        local_layout.setHorizontalSpacing(25)

        self.setLayout(local_layout)

    def set_led_state(self, index, state):
        """
        Set the state of the LED at the given index.

        :param index: The index of the LED in the list.
        :param state: The new state of the LED.
        """
        if 0 <= index < len(self.leds):
            self.leds[index].value = state
        else:
            print(f"Invalid LED index: {index}")
