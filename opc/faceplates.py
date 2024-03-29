import opcode
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QObject, QThread, pyqtSignal,QTimer
from PyQt5.QtGui import QPixmap
from QLed import QLed
import OpenOPC



class Box(QGroupBox):
  def __init__(self,name,layout, opcClient:OpenOPC.client = 'none',opcID='NONE'):
    #self.setTitle(name)
    self.name=name
    self.client=opcClient
    super().__init__(self.name)
    self.layout = layout

    mainLayout=QFormLayout()
  
    self.led1=QLed(onColour=QLed.Green, shape=QLed.Circle)
    
    self.led2=QLed(onColour=QLed.Green, shape=QLed.Circle)
    
    self.led3=QLed(onColour=QLed.Green, shape=QLed.Circle)
    

    self.radioBtn1=QRadioButton('Hand')
    self.radioBtn2=QRadioButton('AUS')
    self.radioBtn3=QRadioButton('AUTO')
    self.opcID=opcID
    self.radioBtn1.clicked.connect(self.write1)
    self.radioBtn2.clicked.connect(self.write2)
    self.radioBtn3.clicked.connect(self.write3)
    
    mainLayout.addRow(self.radioBtn1,self.led1)
    mainLayout.addRow(self.radioBtn2,self.led2)
    mainLayout.addRow(self.radioBtn3,self.led3)


    self.setLayout(mainLayout)
    self.layout.addWidget(self)

  
  def write1(self):
    if self.led1.value==False:
      print(self.opcID+': '+ self.radioBtn1.text())
      self.client.write(('Ack_All',False))

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
    self.led1.value=val[self.name+'.Hand']
    self.led2.value=val[self.name+'.AUS']
    self.led3.value=val[self.name+'.AUTO']

  