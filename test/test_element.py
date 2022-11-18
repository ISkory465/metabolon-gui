import sys
from PyQt5.QtWidgets import *



class Mixer(QGroupBox):

    def __init__(self,name,opcID=None):
        super().__init__(name)

        mainLayout=QFormLayout()

        #<-------------------------------------->

        self.label1 = QLabel("\nFermenter Temp.-Sollwert (\N{DEGREE SIGN}C)")
        
        #Fermenter Temperature value
        self.temp1 = QSpinBox(self) #uses integers; for floats use QDoubleSpinBox

        #Check range of values in LabView
        self.temp1.setMinimum(10)
        self.temp1.setMaximum(100)

        #connect some function when value changed, source: https://www.pythonguis.com/tutorials/pyqt-basic-widgets/
        # temp1.valueChanged.connect(self.value_changed)

                
        mainLayout.addRow(self.label1)
        mainLayout.addRow(self.temp1)
        

        self.setLayout(mainLayout)

