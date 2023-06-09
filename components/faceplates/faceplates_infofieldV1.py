from threading import local
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class InfoFieldV1(QGroupBox):
    """Group element that combines QLabel and QSpinBox with settings to them

    :param QGroupBox: _description_
    :type QGroupBox: _type_
    """
    def __init__(self, name, opcID='None', buttonSymbol=2):
        super().__init__()
        # Remove the group box name
        self.setFlat(True)
        self.setStyleSheet("QGroupBox { border: none; }")
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.opcName=name
        self.layout.setSpacing(0)

        #Header (QLabel) for the numerical field
        self.name = QLabel(name)
        self.layout.addWidget(self.name)

        #Field for numerical Value
        self.spin = QSpinBox() #uses integers; for floats use QDoubleSpinBox

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


# Field for Double parameter with decimal setting
# Example if dec_num = 2 you get 10,00
# If dec_num = 4 - 10,0000
# Default dec_num is 2

class InfoFieldDoubleV1(QGroupBox):
    def __init__(self, name, layout, dec_num = 2, opcID='None', buttonSymbol=2):
        super().__init__()
        
        self.setFlat(True)
        self.setStyleSheet("QGroupBox { border: none; }")
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        
        #Header (QLabel) for the numerical field
        self.name = QLabel(name)
        self.layout.addWidget(self.name)

        #Field for numerical Value
        self.spin = QDoubleSpinBox(decimals = dec_num) #uses integers; for floats use QDoubleSpinBox

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