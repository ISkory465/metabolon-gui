import sys
from PyQt5.QtWidgets import *



class Mixer(QGroupBox):

    def __init__(self,name,opcID=None):
        super().__init__(name)

        mainLayout=QFormLayout()



        #<-------------------------------------->
        #first row
        #Left elements of the row

        self.label1 = QLabel("CH4 [%]")
        self.ch4 = QSpinBox(self) #uses integers; for floats use QDoubleSpinBox

        #Check range of values in LabView
        self.ch4.setMinimum(10)
        self.ch4.setMaximum(100)

        #Removing button arrows:
        self.ch4.setButtonSymbols(2)
        self.ch4.setMaximumSize(35, 20)

        #connect some function when value changed, source: https://www.pythonguis.com/tutorials/pyqt-basic-widgets/
        # temp1.valueChanged.connect(self.value_changed)


        #Right element of the row
        self.label2 = QLabel("Qgas [l/min]")
        self.Qgas = QSpinBox(self)
        self.Qgas.setMinimum(15)
        self.Qgas.setMaximum(100)

        #Arrow delete
        self.Qgas.setButtonSymbols(2)

        #boxsize (width, height)
        self.Qgas.setMaximumSize(35, 20)
                
        mainLayout.addRow(self.label1, self.label2)
        mainLayout.addRow(self.ch4, self.Qgas)
        

        #<-------------------------------------->
        #Second row

        #Left
        self.label3 = QLabel("CO2 [%]")
        self.co2 = QSpinBox(self)

        self.co2.setMinimum(10)
        self.co2.setMaximum(100)

        self.co2.setButtonSymbols(2)
        self.co2.setMaximumSize(35, 20)


        #Right
        self.label4 = QLabel("Qgas [l]")
        self.Qgas1 = QSpinBox(self)

        self.Qgas1.setMinimum(15)
        self.Qgas1.setMaximum(100)

        self.Qgas1.setButtonSymbols(2)
        self.Qgas1.setMaximumSize(35, 20)

        mainLayout.addRow(self.label3, self.label4)
        mainLayout.addRow(self.co2, self.Qgas1)


        #<-------------------------------------->
        #Third row

        #Left
        self.label5 = QLabel("H2 [ppm]")
        self.H2 = QSpinBox(self)

        self.H2.setMinimum(10)
        self.H2.setMaximum(100)

        self.H2.setButtonSymbols(2)
        self.H2.setMaximumSize(35, 20)

        #Right
        self.label6 = QLabel("pH [-]")
        self.pH = QSpinBox(self)

        self.pH.setMinimum(15)
        self.pH.setMaximum(100)

        self.pH.setButtonSymbols(2)
        self.pH.setMaximumSize(35, 20)

        mainLayout.addRow(self.label5, self.label6)
        mainLayout.addRow(self.H2, self.pH)



        #<-------------------------------------->
        #Third row

        #Left
        self.label7 = QLabel("H2S [ppm]")
        self.H2S = QSpinBox(self)

        self.H2S.setMinimum(10)
        self.H2S.setMaximum(100)

        self.H2S.setButtonSymbols(2)
        self.H2S.setMaximumSize(35, 20)


        mainLayout.addRow(self.label7)
        mainLayout.addRow(self.H2S)

        self.setLayout(mainLayout)

