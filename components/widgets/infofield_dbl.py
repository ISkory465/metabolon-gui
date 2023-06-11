from threading import local
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt


class InfoField(QWidget):
    """Group element that combines QLabel and QSpinBox with settings to them
    """

    instances = []

    def __init__(self, name, opcID='None', buttonSymbol=2, dec_num=None, max_width=None):
        super().__init__()
        self.instances.append(self)
        self.opcName = name
        self.state = False
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        #Header (QLabel) for the numerical field
        self.name = QLabel(name)
        self.layout.addWidget(self.name)

        # Create the appropriate spin box type
        if dec_num is not None:
            # Use QDoubleSpinBox for floating point values
            self.spin = QDoubleSpinBox()
            self.spin.setDecimals(dec_num)
        else:
            # Use QSpinBox for integer values
            self.spin = QSpinBox()

        self.spin.setEnabled(self.state)
        
        #Check range of values in LabView
        self.spin.setMinimum(10)
        self.spin.setMaximum(150)
        self.spin.setAlignment(Qt.AlignRight)

        #Deleting the arrows
        self.spin.setButtonSymbols(buttonSymbol)

        #Setting size of the field
        self.spin.setMaximumSize(35 if dec_num is None else 70, 25 if dec_num is None else 20)

        # Restrict the maximum width of the widget if max_width is specified
        if max_width is not None:
            self.setMaximumWidth(max_width)

        self.layout.addWidget(self.spin)

    def update(self,val:dict):
        self.spin.setValue(val[self.opcName])

    @classmethod
    def set_all_states(cls, state):
        for instance in cls.instances:
            instance.state = state
            instance.spin.setEnabled(state)