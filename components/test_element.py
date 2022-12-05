from threading import local
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from QLed import QLed



class InfoField(QGroupBox):
    """Groupelement that combines QLabel and QSpinBox with settings to them

    :param QGroupBox: _description_
    :type QGroupBox: _type_
    """

    def __init__(self, name, layout, buttonSymbol, opcID='None'):
        super().__init__(name)
        self.layout = layout

        #Header (QLabel) for the numerical field
        self.name = QLabel(name)
        self.layout.addWidget(self.name)

        #Field for numerical Value
        self.spin = QSpinBox() #uses integers; for floats use QDoubleSpinBox

        #Check range of values in LabView
        self.spin.setMinimum(10)
        self.spin.setMaximum(100)
        self.spin.setAlignment(Qt.AlignRight)

        #Deleting or adding the arrows
          #QAbstractSpinBox::UpDownArrows	0	Little arrows in the classic style.
          #QAbstractSpinBox::PlusMinus	1	+ and - symbols.
          #QAbstractSpinBox::NoButtons	2	Don't display buttons.
        self.spin.setButtonSymbols(buttonSymbol)

        #Setting size of the field
        self.spin.setMaximumSize(35, 20)

        #connect some function when value changed, source: https://www.pythonguis.com/tutorials/pyqt-basic-widgets/
        # temp1.valueChanged.connect(self.value_changed)

        self.layout.addWidget(self.spin)


class SingleLed(QGroupBox):
    def __init__(self, name, layout, opcID='opcID'):
        super().__init__()
        self.layout = layout

        local_layout = QFormLayout()

        self.name = QLabel(name)
        self.led = QLed(onColour=QLed.Green, shape=QLed.Circle)

        #add if-condition with opc input
        self.led.value = True

        local_layout.addRow(self.name, self.led)
        

        #Settings:
        self.setFixedHeight(50)
        self.setFixedWidth(200)
        local_layout.setVerticalSpacing(8)
        local_layout.setFormAlignment(Qt.AlignLeft)
        local_layout.setHorizontalSpacing(25)

        self.setLayout(local_layout)
        self.layout.addWidget(self)
        



class Mixer(QGroupBox):
    """Mixer set of elements for the Strasse 1 tab

    :param QGroupBox: _description_
    :type QGroupBox: _type_
    """
    
    def __init__(self, name, layout, opcID=None):
        super().__init__(name)

        self.layout = layout
        self.mainLayout=QFormLayout()

        #<-------------------------------------->
        #first row
        #Left elements of the row

        self.ch4 = InfoField(name = "CH4 [%]", 
                         layout = self.mainLayout, 
                         buttonSymbol=2)

        #Right element of the row
        self.Qgas = InfoField(name = "Qgas [l/min]", 
                         layout = self.mainLayout,
                         buttonSymbol=2)

        self.mainLayout.addRow(self.ch4.name, self.Qgas.name)
        self.mainLayout.addRow(self.ch4.spin, self.Qgas.spin)
        

        #<-------------------------------------->
        #Second row
        #Left
        self.co2 = InfoField(name = "CO2 [%]", 
                         layout = self.mainLayout,
                         buttonSymbol=2)

        #Right
        self.Qgas1 = InfoField(name = "CH4 [%]", 
                         layout = self.mainLayout,
                         buttonSymbol=2)

        self.mainLayout.addRow(self.co2.name, self.Qgas1.name)
        self.mainLayout.addRow(self.co2.spin, self.Qgas1.spin)


        #<-------------------------------------->
        #Third row
        #Left
        self.H2 = InfoField(name = "H2 [ppm]", 
                         layout = self.mainLayout,
                         buttonSymbol=2)
  
        #Right
        self.pH = InfoField(name = "pH [-]", 
                         layout = self.mainLayout,
                         buttonSymbol=2)
 
        self.mainLayout.addRow(self.H2.name, self.pH.name)
        self.mainLayout.addRow(self.H2.spin, self.pH.spin)


        #<-------------------------------------->
        #Fourth row
        #Left
        self.H2S = InfoField(name = "H2S [ppm]", 
                         layout = self.mainLayout,
                         buttonSymbol=2)
 
        self.mainLayout.addRow(self.H2S.name)
        self.mainLayout.addRow(self.H2S.spin)


        self.layout.addWidget(self)
        # self.setAlignment(Qt.AlignTop)
        self.mainLayout.setSpacing(0)
        self.mainLayout.setLabelAlignment(Qt.AlignTop)
        
        self.setLayout(self.mainLayout)



class Box(QGroupBox):
  def __init__(self,name, layout, opcID='opcID'):
    #self.setTitle(name)
    super().__init__(name)
    self.layout = layout

    mainLayout=QFormLayout()
  
    self.led1=QLed(onColour=QLed.Green, shape=QLed.Circle)
    self.led2=QLed(onColour=QLed.Green, shape=QLed.Circle)
    self.led3=QLed(onColour=QLed.Green, shape=QLed.Circle)
    

    self.radioBtn1=QRadioButton('Hand')
    self.radioBtn2=QRadioButton('AUS')
    self.radioBtn2.setChecked(True)
    self.led2.value = True
    self.radioBtn3=QRadioButton('AUTO')

    self.opcID=opcID
    self.radioBtn1.clicked.connect(self.write1)
    self.radioBtn2.clicked.connect(self.write2)
    self.radioBtn3.clicked.connect(self.write3)
    
    mainLayout.addRow(self.radioBtn1,self.led1)
    mainLayout.addRow(self.radioBtn2,self.led2)
    mainLayout.addRow(self.radioBtn3,self.led3)

    #Settings:
    mainLayout.setVerticalSpacing(8)
    mainLayout.setFormAlignment(Qt.AlignLeft)
    mainLayout.setHorizontalSpacing(55)
    self.setFixedHeight(120)
    self.setFixedWidth(165)


    self.setLayout(mainLayout)
    self.layout.addWidget(self)
  
  def write1(self):
    if self.led1.value==False:
      print(self.opcID+': '+ self.radioBtn1.text())

    self.led1.value=True
    self.led2.value=False
    self.led3.value=False

  def write2(self):

    if self.led2.value==False:
      print(self.opcID+': '+ self.radioBtn2.text())

    self.led2.value=True
    self.led1.value=False
    self.led3.value=False

  def write3(self):

    if self.led3.value==False:
      print(self.opcID+': '+ self.radioBtn3.text())

    self.led3.value=True
    self.led1.value=False
    self.led2.value=False