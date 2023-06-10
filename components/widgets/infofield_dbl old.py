from threading import local
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt


class InfoField(QWidget):
    """Group element that combines QLabel and QSpinBox with settings to them

    :param QGroupBox: _description_
    :type QGroupBox: _type_
    """

    instances = []

    def __init__(self, name, opcID='None', buttonSymbol=2):
        super().__init__()
        self.instances.append(self)
        # self.setFlat(True)
        self.opcName = name
        self.state = False
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        #Header (QLabel) for the numerical field
        self.name = QLabel(name)
        self.layout.addWidget(self.name)

        #Field for numerical Value
        self.spin = QSpinBox() #uses integers; for floats use QDoubleSpinBox
        self.spin.setEnabled(self.state)

        #LOCK-----------------------------------!!!!!!!!
        
        # op=QGraphicsOpacityEffect(self)
        # op.setOpacity(0.80)
        # self.spin.setEnabled(False)
        # self.spin.setGraphicsEffect(op)
        # self.spin.setReadOnly(True)

        #Check range of values in LabView
        self.spin.setMinimum(10)
        self.spin.setMaximum(150)
        self.spin.setAlignment(Qt.AlignRight)

        #Deleting the arrows
        self.spin.setButtonSymbols(buttonSymbol)

        #Setting size of the field
        self.spin.setMaximumSize(35, 25)

        #connect some function when value changed, source: https://www.pythonguis.com/tutorials/pyqt-basic-widgets/
        # temp1.valueChanged.connect(self.value_changed)

        self.layout.addWidget(self.spin)

    def update(self,val:dict):
        self.spin.setValue(val[self.opcName])
        #print(self.opcName+' : '+str(val[self.opcName]))

    @classmethod
    def set_all_states(cls, state):
        for instance in cls.instances:
            instance.state = state
            instance.spin.setEnabled(state)


# Field for Double parameter with decimal setting
# Example if dec_num = 2 you get 10,00
# If dec_num = 4 - 10,0000
# Default dec_num is 2

class InfoFieldDouble(QWidget):
    
    instances = []

    def __init__(self, name, dec_num = 2, opcID='None', buttonSymbol=2):
        super().__init__()
        self.instances.append(self)
        self.state = False
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        #Header (QLabel) for the numerical field
        self.name = QLabel(name)
        self.layout.addWidget(self.name)

        #Field for numerical Value
        self.spin = QDoubleSpinBox(decimals = dec_num) #uses integers; for floats use QDoubleSpinBox
        self.spin.setEnabled(self.state)

        #Check range of values in LabView
        self.spin.setMinimum(10)
        self.spin.setMaximum(150)
        self.spin.setAlignment(Qt.AlignRight)

        #Deleting the arrows
        self.spin.setButtonSymbols(buttonSymbol)

        #Setting size of the field
        self.spin.setMaximumSize(70, 20)

        #connect some function when value changed, source: https://www.pythonguis.com/tutorials/pyqt-basic-widgets/
        # temp1.valueChanged.connect(self.value_changed)

        self.layout.addWidget(self.spin)

    @classmethod
    def set_all_states(cls, state):
        for instance in cls.instances:
            instance.state = state
            instance.spin.setEnabled(state)