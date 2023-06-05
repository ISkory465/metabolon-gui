import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
# from facelpates_new import SingleLed, Led
from QLed import QLed

class SingleLed(QWidget):
    def __init__(self, name, layout, opcID='opcID'):
        super().__init__()
        self.layout = layout
        self.opcName = name
        local_layout = QFormLayout()

        self.name = QLabel(name)
        self.led = QLed(onColour=QLed.Green, shape=QLed.Circle)

        #add if-condition with opc input
        self.led.value = True

        # local_layout.addRow(self.name, self.led)
        local_layout.addRow(self.led)
        

        #Settings:
        self.setFixedHeight(40)
        self.setFixedWidth(40)
        local_layout.setVerticalSpacing(8)
        local_layout.setFormAlignment(Qt.AlignLeft)
        local_layout.setHorizontalSpacing(25)

        self.setLayout(local_layout)
        self.layout.addWidget(self)

    def update(self,val:dict):
        self.led.value=val[self.opcName]

class FaultBox(QWidget):
    def __init__(self, opcID=None):
        super().__init__()

        # Main layout for 2 horizontal boxes representing each row
        main_vbox = QVBoxLayout()
        
        label = QLabel("Stoerung Quittieren")
        label.setAlignment(Qt.AlignCenter)
        main_vbox.addWidget(label)

        # Second row
        row2 = QHBoxLayout()
        
        # Button
        self.button = QPushButton("Quittieren")
        self.button.clicked.connect(self.toggleActive)
        row2.addWidget(self.button)
        
        # LED
        self.led_layout = QVBoxLayout()
        self.single_led = SingleLed("LED", self.led_layout)
        # self.single_led = Led("LED", self.led_layout)
        row2.addLayout(self.led_layout)
        
        main_vbox.addLayout(row2)

        # parent_layout.addWidget(self)
        self.setLayout(main_vbox)

    def toggleActive(self):
        self.single_led.led.value = not self.single_led.led.value


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QWidget()
    layout = QVBoxLayout(window)
    fault_box = FaultBox()
    layout.addWidget(fault_box)
    window.show()
    sys.exit(app.exec_())