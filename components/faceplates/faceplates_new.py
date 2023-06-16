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
      self.setFlat(True) #remove QGroupBox frame
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
           pass
          #  print("Button 1 clicked")
       

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
    """Group element that combines QLabel and QSpinBox with settings to them

    :param QGroupBox: _description_
    :type QGroupBox: _type_
    """

    instances = []

    def __init__(self, name, layout, opcID='None', buttonSymbol=2):
        super().__init__(name)
        self.instances.append(self)
        self.setFlat(True)
        self.layout = layout
        self.opcName = name
        self.state = False

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
        self.spin.setMinimum(0)
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
        try:
          self.spin.setValue(val[self.opcName])
        except:
          self.spin.setValue(0)
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

class InfoFieldDouble(QGroupBox):
    
    instances = []

    def __init__(self, name, layout, dec_num = 2, opcID='None', buttonSymbol=2):
        super().__init__(name)
        self.instances.append(self)
        self.layout = layout
        self.state = False

        #Header (QLabel) for the numerical field
        self.name = QLabel(name)
        self.layout.addWidget(self.name)
        self.opcName=name

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
    def update(self,val:dict):
        try:
          self.spin.setValue(val[self.opcName])
        except:
          self.spin.setValue(0)

    @classmethod
    def set_all_states(cls, state):
        for instance in cls.instances:
            instance.state = state
            instance.spin.setEnabled(state)

class SingleLed(QGroupBox):
    def __init__(self, name, layout, opcID='opcID'):
        super().__init__()
        self.layout = layout
        self.opcName = name
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
        try:
          self.led.value=val[self.opcName]
        except:
          self.led.value=False

class Box(QGroupBox):

  instances = []

  def __init__(self, name, layout, opcID='opcID', horizontal_spacing=55, width=165):
    #self.setTitle(name)
    super().__init__(name)
    self.instances.append(self)
    self.layout = layout
    self.opcName=name
    mainLayout = QFormLayout()
    self.state = False

    self.setEnabled(self.state)
  
    self.led1=QLed(onColour=QLed.Green, shape=QLed.Circle)
    self.led2=QLed(onColour=QLed.Green, shape=QLed.Circle)
    self.led3=QLed(onColour=QLed.Green, shape=QLed.Circle)
    

    self.radioBtn1=QRadioButton('Hand')
    self.radioBtn2=QRadioButton('AUS')
    #self.radioBtn2.setChecked(True)
    #self.led2.value = True
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
    mainLayout.setHorizontalSpacing(horizontal_spacing)
    self.setFixedHeight(120)
    self.setFixedWidth(width)


    self.setLayout(mainLayout)
    self.layout.addWidget(self)
  
  @classmethod
  def set_all_states(cls, state):
        for instance in cls.instances:
            instance.state = state
            instance.setEnabled(state)


  def write1(self):
    if self.led1.value==False:
        print(self.opcID+': '+ self.radioBtn1.text())
    self.led1.setValue(True)
    self.led2.setValue(False)  # Add this line
    self.led3.setValue(False)  # Add this line


  def write2(self):

    if self.led2.value==False:
      print(self.opcID+': '+ self.radioBtn2.text())

    self.led2.setValue(True)
    self.led1.setValue(False)
    self.led3.setValue(False)

  def write3(self):

    if self.led3.value==False:
      print(self.opcID+': '+ self.radioBtn3.text())

    self.led2.setValue(False)
    self.led1.setValue(False)
    self.led3.setValue(True)


  def update(self,val):
   
    # self.led1.value=val[self.opcName+'.Hand']
    # self.led2.value=val[self.opcName+'.AUS']
    # self.led3.value=val[self.opcName+'.AUTO']
    try:
      if (val[self.opcName+'.Hand']):
        self.radioBtn2.setChecked(False)
        self.radioBtn3.setChecked(False)
        self.radioBtn1.setChecked(True)
        
        self.led2.setValue(False)
        self.led3.setValue(False)
        self.led1.setValue(True)

        #print("Led1 is true")

      elif (val[self.opcName+'.AUS']):
        self.radioBtn1.setChecked(False)
        self.radioBtn2.setChecked(True)
        self.radioBtn3.setChecked(False)
        self.led1.setValue(False)
        self.led2.setValue(True)
        self.led3.setValue(False)
        #print("Led2 is true")

      elif (val[self.opcName+'.AUTO']):
        self.radioBtn1.setChecked(False)
        self.radioBtn2.setChecked(False)
        self.radioBtn3.setChecked(True)
        self.led1.setValue(False)
        self.led2.setValue(False)
        self.led3.setValue(True)
        #print("Led3 is true")
    except Exception as e:
        self.led1.setValue(False)
        self.led2.setValue(False)
        self.led3.setValue(False)
        print(str(e))

    #print(val[self.opcName+'.Hand'])

class Led_5(QGroupBox):
    def __init__(self, box_name, name, layout, opcID='opcID'):
        super().__init__(box_name)
        self.layout = layout

        local_layout = QFormLayout()

        #self.name = QLabel(name)
        self.led1=QLed(onColour=QLed.Red, shape=QLed.Circle)
        self.led2=QLed(onColour=QLed.Red, shape=QLed.Circle)
        self.led3=QLed(onColour=QLed.Red, shape=QLed.Circle)
        self.led4=QLed(onColour=QLed.Red, shape=QLed.Circle)
        self.led5=QLed(onColour=QLed.Red, shape=QLed.Circle)
        

        #add if-condition with opc input
        self.led1.value = False
        self.led2.value = False
        self.led3.value = True
        self.led4.value = False
        self.led5.value = False

        #self.led1 = name.split(',')[0]


        local_layout.addRow(self.led1, QLabel(name.split(',')[0]))
        local_layout.addRow(self.led2, QLabel(name.split(',')[1]))
        local_layout.addRow(self.led3, QLabel(name.split(',')[2]))
        local_layout.addRow(self.led4, QLabel(name.split(',')[3]))
        local_layout.addRow(self.led5, QLabel(name.split(',')[4]))
        
        

        #Settings:
        self.setFixedHeight(200)
        self.setFixedWidth(300)
        #local_layout.setVerticalSpacing(18)
        local_layout.setFormAlignment(Qt.AlignLeft)
        local_layout.setHorizontalSpacing(25)

        self.setLayout(local_layout)
        self.layout.addWidget(self)

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
        self.opcName=[]
        self.opcName.append(name.split(',')[0])
        self.opcName.append(name.split(',')[1])
        self.opcName.append(name.split(',')[2])
        self.opcName.append(name.split(',')[3])
        self.opcName.append(name.split(',')[4])
        self.opcName.append(name.split(',')[5])
        
        

        #Settings:
        #self.setFixedHeight(78)
        self.setFixedHeight(200)
        self.setFixedWidth(300)
        #local_layout.setVerticalSpacing(18)
        local_layout.setFormAlignment(Qt.AlignLeft)
        local_layout.setHorizontalSpacing(25)

        self.setLayout(local_layout)
        self.layout.addWidget(self)
    def update(self,val:dict):
        try:
          self.led1.value=val[self.opcName[0]]
          self.led2.value=val[self.opcName[1]]
          self.led3.value=val[self.opcName[2]]
          self.led4.value=val[self.opcName[3]]
          self.led5.value=val[self.opcName[4]]
          self.led6.value=val[self.opcName[5]]
          

        except:
          self.led1.value = False
          self.led2.value = False
          self.led3.value = False
          self.led4.value = False
          self.led5.value = False
          self.led6.value = False
         

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
        self.opcName=[]
        self.opcName.append(name.split(',')[0])
        self.opcName.append(name.split(',')[1])
        self.opcName.append(name.split(',')[2])
        self.opcName.append(name.split(',')[3])
        self.opcName.append(name.split(',')[4])
        self.opcName.append(name.split(',')[5])
        self.opcName.append(name.split(',')[6])
        self.opcName.append(name.split(',')[7])


        #Settings:
        #self.setFixedHeight(106)
        self.setFixedHeight(250)
        self.setFixedWidth(300)

        #local_layout.setVerticalSpacing(18)
        local_layout.setFormAlignment(Qt.AlignLeft)
        local_layout.setHorizontalSpacing(25)


        self.setLayout(local_layout)
        self.layout.addWidget(self)

    def update(self,val:dict):
        try:
          self.led1.value=val[self.opcName[0]]
          self.led2.value=val[self.opcName[1]]
          self.led3.value=val[self.opcName[2]]
          self.led4.value=val[self.opcName[3]]
          self.led5.value=val[self.opcName[4]]
          self.led6.value=val[self.opcName[5]]
          self.led7.value=val[self.opcName[6]]
          self.led8.value=val[self.opcName[7]]

        except Exception as e:
          print(str(e))
          self.led1.value = False
          self.led2.value = False
          self.led3.value = False
          self.led4.value = False
          self.led5.value = False
          self.led6.value = False
          self.led7.value = False
          self.led8.value = False
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


class Led(QGroupBox):
    def __init__(self, name, layout, opcID='opcID'):
        super().__init__()
        self.layout = layout
        self.opcName=name
        self.led1=QLed(onColour=QLed.Green, shape=QLed.Circle)
              
        self.led1.value = True

        self.led1.setFixedHeight(25)
        
        self.layout.addWidget(self.led1)
        self.layout.addWidget(QLabel(name))
    def update(self,val:dict):
        try:
          self.led1.value=val[self.opcName]
        except:
          self.led1.value=False

class Led_DA(QGroupBox): #Description Above
    def __init__(self, name, layout, opcID='opcID'):
        super().__init__()
        self.layout = layout

        self.led1=QLed(onColour=QLed.Green, shape=QLed.Circle)
              
        self.led1.value = True

        self.led1.setFixedHeight(25)
        self.opcName=name
        
        self.layout.addWidget(QLabel(name))
        self.layout.addWidget(self.led1, alignment = Qt.AlignLeft)
    def update(self,val:dict):
        try:
          self.led1.value=val[self.opcName]
        except:
          self.led1.value=False


class Feststoffbtn(QGroupBox):
    def __init__(self, firstElement, secondElement, thirdElement, fourthElement, fifthElement, sixthElement, layout, opcID='opcID'):
        super().__init__()
        self.setFlat(True)
        self.layout = layout #vbox 
        self.mainLayout=QHBoxLayout()
        self.buttonLayout=QVBoxLayout()
        self.vbox1=QVBoxLayout()
    
        #<-------------------------------------->
        #first row 
        button1 = UnlabelledButton(layout=self.buttonLayout)
        #Left elements of the row
        firstElement = InfoField(name =firstElement, 
                         layout = self.vbox1, buttonSymbol=2) 
        
        self.buttonLayout.addWidget(button1)
        #<-------------------------------------->
        #Second row
        button2 = UnlabelledButton(layout=self.buttonLayout)
        secondElement = InfoField(name =secondElement, 
                         layout = self.vbox1, buttonSymbol=2)
        
        self.buttonLayout.addWidget(button2)
        
        #Third row
        button3 = UnlabelledButton(layout=self.buttonLayout)
        thirdElement = InfoField(name =thirdElement, 
                         layout = self.vbox1, buttonSymbol=2)
        
        self.buttonLayout.addWidget(button3)
       
        #Fourth row
        button4 = UnlabelledButton(layout=self.buttonLayout)
        fourthElement = InfoField(name =fourthElement, 
                         layout = self.vbox1, buttonSymbol=2)
        
        self.buttonLayout.addWidget(button4)

        #Fifth row
        button5 = UnlabelledButton(layout=self.buttonLayout)
        fifthElement = InfoField(name =fifthElement, 
                         layout = self.vbox1, buttonSymbol=2)
        
        self.buttonLayout.addWidget(button5)
        
        #Six row
        button6 = UnlabelledButton(layout=self.buttonLayout)
        sixthElement = InfoField(name = sixthElement, 
                         layout = self.vbox1, buttonSymbol=2)
        self.buttonLayout.addWidget(button6)
         
        #adding layouts to main layout
        self.mainLayout.addLayout(self.buttonLayout)
        self.mainLayout.addLayout(self.vbox1)
       
        #setting for adjasting space between elements in layouts
        self.vbox1.setSpacing(5)
        self.mainLayout.setSpacing(5)
       
        self.layout.addLayout(self.mainLayout)


class UnlabelledButton(QGroupBox):
    """Groupelement that combines QLabel and QPushbutton with settings to them
    :param QGroupBox: _description_
    :type QGroupBox: _type_
    """

    def __init__(self, layout, opcID='None'):
      super().__init__()
      self.setFlat(True)
      self.layout = layout
      self.layout.setSpacing(0)
      self.layout.setContentsMargins(0,0,0,0)
      self.setFixedHeight(20)
      self.setFixedWidth(20)

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
           pass
          #  print("Button 1 clicked")
       

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
