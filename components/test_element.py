from threading import local
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from QLed import QLed

class ToggleButton(QGroupBox):
    """Groupelement that combines QLabel and QPushbutton with settings to them
    :param QGroupBox: _description_
    :type QGroupBox: _type_
    """
    def __init__(self, name, layout, opcID='None'):
      super().__init__()
      self.layout = layout
      self.layout.setSpacing(0)
      self.layout.setContentsMargins(0,0,0,0)
      #self.setFixedHeight(250)
      self.setFixedWidth(150)

      #Header (QLabel) for the numerical field
      self.name = QLabel(name)
      self.layout.addWidget(self.name)
      
      # creating a push button
      self.button = QPushButton("",self)
  
      # setting default color of button to light-grey
      self.button.setStyleSheet("""
        QPushButton{
        background-color:'lightgrey';
        }
        """
                                )               
      # setting checkable to true
      self.button.setCheckable(True)
      # setting calling method by button 
      self.button.clicked.connect(self.toggle)
      self.button.clicked.connect(self.changeColor)
      self.layout.addWidget(self.button)      
      
    #<-------------------------------------->
    # action methods
    def toggle(self):
        if self.button.isChecked():
           print("Button 1 clicked")
       

     # method called by button
    def changeColor(self):
        # if button is checked
        if self.button.isChecked():
            # setting background color to light-blue
           self.button.setStyleSheet("""
        QPushButton{
        background-color:'green';
        }
        """
                                      )
        # if it is unchecked
        else:
            # set background color back to light-grey
            self.button.setStyleSheet("QPushButton"
                                      "{"
                                        "background-color : lightgrey;"
                                      "}"
                                      )

class InfoField(QGroupBox):
    """Groupelement that combines QLabel and QSpinBox with settings to them

    :param QGroupBox: _description_
    :type QGroupBox: _type_
    """

    def __init__(self, name, layout, opcID='None', buttonSymbol=2):
        super().__init__(name)
        self.layout = layout
        self.opcName=name
        #Header (QLabel) for the numerical field
        self.name = QLabel(name)
        self.layout.addWidget(self.name)

        #Field for numerical Value
        self.spin = QSpinBox() #uses integers; for floats use QDoubleSpinBox

        #Check range of values in LabView
        self.spin.setMinimum(10)
        self.spin.setMaximum(150)
        self.spin.setAlignment(Qt.AlignRight)

        #Deleting the arrows
        self.spin.setButtonSymbols(buttonSymbol)

        #Setting size of the field
        self.spin.setMaximumSize(45, 30)

        #connect some function when value changed, source: https://www.pythonguis.com/tutorials/pyqt-basic-widgets/
        # temp1.valueChanged.connect(self.value_changed)

        self.layout.addWidget(self.spin)

    def update(self,val:dict):
        self.spin.value=val[self.opcName]


# Field for Double parameter with decimal setting
#Example if dec_num = 2 you get 10,00
#If dec_num = 4 - 10,0000
# Default dec_num is 2

class InfoFieldDouble(QGroupBox):
    def __init__(self, name, layout, dec_num = 2, opcID='None', buttonSymbol=2):
        super().__init__(name)
        self.layout = layout

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

class SingleLed(QGroupBox):
    def __init__(self, name, layout, opcID='opcID'):
        super().__init__()
        self.layout = layout
        self.opcName=name
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

    def update(self,val:dict):
        self.led.value=val[self.opcName]
        

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
                         layout = self.mainLayout)

        #Right element of the row
        self.Qgas = InfoField(name = "Qgas [l/min]", 
                         layout = self.mainLayout)

        self.mainLayout.addRow(self.ch4.name, self.Qgas.name)
        self.mainLayout.addRow(self.ch4.spin, self.Qgas.spin)
        

        #<-------------------------------------->
        #Second row
        #Left
        self.co2 = InfoField(name = "CO2 [%]", 
                         layout = self.mainLayout)

        #Right
        self.Qgas1 = InfoField(name = "CH4 [%]", 
                         layout = self.mainLayout)

        self.mainLayout.addRow(self.co2.name, self.Qgas1.name)
        self.mainLayout.addRow(self.co2.spin, self.Qgas1.spin)


        #<-------------------------------------->
        #Third row
        #Left
        self.H2 = InfoField(name = "H2 [ppm]", 
                         layout = self.mainLayout)
  
        #Right
        self.pH = InfoField(name = "pH [-]", 
                         layout = self.mainLayout)
 
        self.mainLayout.addRow(self.H2.name, self.pH.name)
        self.mainLayout.addRow(self.H2.spin, self.pH.spin)


        #<-------------------------------------->
        #Fourth row
        #Left
        self.H2S = InfoField(name = "H2S [ppm]", 
                         layout = self.mainLayout)
 
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
    self.opcName=name
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
  def update(self,val):
    self.led1.value=val[self.opcName+'.Hand']
    self.led2.value=val[self.opcName+'.AUS']
    self.led3.value=val[self.opcName+'.AUTO']


class Led_6(QGroupBox):
    def __init__(self, name, layout, opcID='opcID'):
        super().__init__()
        self.layout = layout

        local_layout = QFormLayout()

        #self.name = QLabel(name)
        self.led1=QLed(onColour=QLed.Green, shape=QLed.Circle)
        self.led2=QLed(onColour=QLed.Green, shape=QLed.Circle)
        self.led3=QLed(onColour=QLed.Green, shape=QLed.Circle)
        self.led4=QLed(onColour=QLed.Green, shape=QLed.Circle)
        self.led5=QLed(onColour=QLed.Green, shape=QLed.Circle)
        self.led6=QLed(onColour=QLed.Green, shape=QLed.Circle)
        

        #add if-condition with opc input
        self.led1.value = True
        self.led2.value = True
        self.led3.value = True
        self.led4.value = True
        self.led5.value = True
        self.led6.value = True
        #self.led1 = name.split(',')[0]

        #self.layout.addWidget(self.led1)
        #self.layout.addWidget(QLabel(name.split(',')[0]))
       # self.layout.addWidget(self.led2)
       # self.layout.addWidget(QLabel(name.split(',')[1]))


        local_layout.addRow(self.led1, QLabel(name.split(',')[0]))
        local_layout.addRow(self.led2, QLabel(name.split(',')[1]))
        local_layout.addRow(self.led3, QLabel(name.split(',')[2]))
        local_layout.addRow(self.led4, QLabel(name.split(',')[3]))
        local_layout.addRow(self.led5, QLabel(name.split(',')[4]))
        local_layout.addRow(self.led6, QLabel(name.split(',')[5]))
        
        

        #Settings:
        #self.setFixedHeight(78)
        self.setFixedHeight(200)
        self.setFixedWidth(300)
        #local_layout.setVerticalSpacing(18)
        local_layout.setFormAlignment(Qt.AlignLeft)
        local_layout.setHorizontalSpacing(25)

        self.setLayout(local_layout)
        self.layout.addWidget(self)

class Led_8(QGroupBox):
    def __init__(self, name, layout, opcID='opcID'):
        super().__init__()
        self.layout = layout

        local_layout = QFormLayout()

        #self.name = QLabel(name)
        self.led1=QLed(onColour=QLed.Green, shape=QLed.Circle)
        self.led2=QLed(onColour=QLed.Green, shape=QLed.Circle)
        self.led3=QLed(onColour=QLed.Green, shape=QLed.Circle)
        self.led4=QLed(onColour=QLed.Green, shape=QLed.Circle)
        self.led5=QLed(onColour=QLed.Green, shape=QLed.Circle)
        self.led6=QLed(onColour=QLed.Green, shape=QLed.Circle)
        self.led7=QLed(onColour=QLed.Green, shape=QLed.Circle)
        self.led8=QLed(onColour=QLed.Green, shape=QLed.Circle)
        
        
        #add if-condition with opc input
        self.led1.value = True
        self.led2.value = False
        self.led3.value = True
        self.led4.value = True
        self.led5.value = True
        self.led6.value = True
        self.led7.value = True
        self.led8.value = True

        #self.led1 = name.split(',')[0]

        local_layout.addRow(self.led1, QLabel(name.split(',')[0]))
        local_layout.addRow(self.led2, QLabel(name.split(',')[1]))
        local_layout.addRow(self.led3, QLabel(name.split(',')[2]))
        local_layout.addRow(self.led4, QLabel(name.split(',')[3]))
        local_layout.addRow(self.led5, QLabel(name.split(',')[4]))
        local_layout.addRow(self.led6, QLabel(name.split(',')[5]))
        local_layout.addRow(self.led7, QLabel(name.split(',')[6]))
        local_layout.addRow(self.led8, QLabel(name.split(',')[7]))

        #Settings:
        #self.setFixedHeight(106)
        self.setFixedHeight(250)
        self.setFixedWidth(300)

        #local_layout.setVerticalSpacing(18)
        local_layout.setFormAlignment(Qt.AlignLeft)
        local_layout.setHorizontalSpacing(25)


        self.setLayout(local_layout)
        self.layout.addWidget(self)

<<<<<<< HEAD
<<<<<<< HEAD
class Futter1():
  """Mixer set of elements for the Strasse 1 tab
    :param QGroupBox: _description_
    :type QGroupBox: _type_
  """
    
  def __init__(self, buttonName, sollwert11, solwert12, solwert21, solwert22, layout, opcID=None):
        super().__init__()

        self.layout = layout #vbox 
        self.mainLayout=QHBoxLayout()
        self.buttonLayout=QVBoxLayout()
        self.vbox1=QVBoxLayout()
        self.vbox2=QVBoxLayout()
    
        #<-------------------------------------->
        #first row 
        button=ToggleButton(name=buttonName, layout=self.buttonLayout)
        #Left elements of the row
        festSollwert11 = InfoField(name =sollwert11, 
                         layout = self.vbox1, buttonSymbol=1)

        #Right element of the row
        festSollwert12 = InfoField(name = solwert12, 
                         layout = self.vbox2)
        
        #<-------------------------------------->
        #Second row
        #Left 
       
        festSollwert21 = InfoField(name = solwert21, 
                         layout = self.vbox1)

        #Right
        festSollwert22 = InfoField(name = solwert22, 
                         layout = self.vbox2)
        
        self.buttonLayout.addWidget(button)
        
        #adding layouts to main layout
        self.mainLayout.addLayout(self.buttonLayout)
        self.mainLayout.addLayout(self.vbox1)
        self.mainLayout.addLayout(self.vbox2)
       
        #setting for adjasting space between elements in layouts
        self.vbox1.setSpacing(10)
        self.vbox2.setSpacing(10)
        self.mainLayout.setSpacing(10)
       
        self.layout.addLayout(self.mainLayout)
        #self.layout.addStretch()
=======
  
>>>>>>> OPC-Branch
=======
  
>>>>>>> OPC-Branch
