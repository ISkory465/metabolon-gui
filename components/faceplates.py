from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from QLed import QLed



class Box(QGroupBox):
  def __init__(self,name, opcID='blank'):
    #self.setTitle(name)
    super().__init__(name)

    mainLayout=QFormLayout()
  
    self.led1=QLed(onColour=QLed.Green, shape=QLed.Circle)
    
    self.led2=QLed(onColour=QLed.Green, shape=QLed.Circle)
    
    self.led3=QLed(onColour=QLed.Green, shape=QLed.Circle)
    

    self.radioBtn1=QRadioButton('Hand')
    self.radioBtn2=QRadioButton('AUS')
    self.radioBtn2.setChecked(True)
    self.radioBtn3=QRadioButton('AUTO')
    self.opcID=opcID
    self.radioBtn1.clicked.connect(self.write1)
    self.radioBtn2.clicked.connect(self.write2)
    self.radioBtn3.clicked.connect(self.write3)
    
    mainLayout.addRow(self.radioBtn1,self.led1)
    mainLayout.addRow(self.radioBtn2,self.led2)
    mainLayout.addRow(self.radioBtn3,self.led3)
    mainLayout.setVerticalSpacing(8)
    mainLayout.setFormAlignment(Qt.AlignLeft)

    self.setLayout(mainLayout)
  
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


  