from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from QLed import QLed



class Box(QGroupBox):

  instances = []

  def __init__(self, name, opcID='opcID', horizontal_spacing=10, width=100):
    #self.setTitle(name)
    super().__init__(name)
    self.instances.append(self)
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


class BoxV2(QGroupBox):

  instances = []

  def __init__(self, name, opcID='opcID', horizontal_spacing=10, width=100):
    #self.setTitle(name)
    super().__init__(name)
    self.instances.append(self)
    self.opcName=name
    mainLayout = QFormLayout()
    self.state = False

    self.setEnabled(self.state)
  
    self.led1=QLed(onColour=QLed.Green, shape=QLed.Circle)
    self.led2=QLed(onColour=QLed.Green, shape=QLed.Circle)
    self.led3=QLed(onColour=QLed.Green, shape=QLed.Circle)
    

    self.radioBtn1=QRadioButton('Auf')
    self.radioBtn2=QRadioButton('Zu')
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
   
    try:
      if (val[self.opcName+'.Auf']):
        self.radioBtn2.setChecked(False)
        self.radioBtn3.setChecked(False)
        self.radioBtn1.setChecked(True)
        
        self.led2.setValue(False)
        self.led3.setValue(False)
        self.led1.setValue(True)

        #print("Led1 is true")

      elif (val[self.opcName+'.Zu']):
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