import opcode
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QObject, QThread, pyqtSignal,QTimer
from PyQt5.QtGui import QPixmap
import QLed



class Box(QGroupBox):
  def __init__(self,name,opcID):
    #self.setTitle(name)
    super().__init__(name)

    mainLayout=QFormLayout()
    self.img1=QLabel()
    self.img1.setPixmap(QPixmap('images/CIRCLEGRAY.png'))
    self.flag1=0
    self.img2=QLabel()
    self.img2.setPixmap(QPixmap('images/CIRCLEGRAY.png'))
    self.flag2=0
    self.img3=QLabel()
    self.img3.setPixmap(QPixmap('images/CIRCLEGRAY.png'))
    self.flag3=0

    self.radioBtn1=QRadioButton('Hand')
    self.radioBtn2=QRadioButton('AUS')
    self.radioBtn3=QRadioButton('AUTO')
    self.opcID=opcID
    self.radioBtn1.clicked.connect(self.write1)
    self.radioBtn2.clicked.connect(self.write2)
    self.radioBtn3.clicked.connect(self.write3)
    
    mainLayout.addRow(self.radioBtn1,self.img1)
    mainLayout.addRow(self.radioBtn2,self.img2)
    mainLayout.addRow(self.radioBtn3,self.img3)


    self.setLayout(mainLayout)
  
  def write1(self):

    print(self.opcID+': '+ self.radioBtn1.text())

    if self.flag1 == 0:

      self.img1.setPixmap(QPixmap('images/CIRCLEGREEN.png'))
      self.img2.setPixmap(QPixmap('images/CIRCLEGRAY.png'))
      self.img3.setPixmap(QPixmap('images/CIRCLEGRAY.png'))


      self.flag1=1
      self.flag2=0
      self.flag3=0
    else:
      self.img1.setPixmap(QPixmap('images/CIRCLEGRAY.png'))
      self.flag1=0

  def write2(self):

    print(self.opcID+': '+ self.radioBtn2.text())

    if self.flag2 == 0:

      self.img2.setPixmap(QPixmap('images/CIRCLEGREEN.png'))
      self.img1.setPixmap(QPixmap('images/CIRCLEGRAY.png'))
      self.img3.setPixmap(QPixmap('images/CIRCLEGRAY.png'))


      self.flag2=1
      self.flag1=0
      self.flag3=0
    else:
      self.img2.setPixmap(QPixmap('images/CIRCLEGRAY.png'))
      self.flag2=0
      
  def write3(self):

    print(self.opcID+': '+ self.radioBtn3.text())

    if self.flag3 == 0:

      self.img3.setPixmap(QPixmap('images/CIRCLEGREEN.png'))
      self.img1.setPixmap(QPixmap('images/CIRCLEGRAY.png'))
      self.img2.setPixmap(QPixmap('images/CIRCLEGRAY.png'))


      self.flag3=1
      self.flag1=0
      self.flag2=0
    else:
      self.img3.setPixmap(QPixmap('images/CIRCLEGRAY.png'))
      self.flag3=0
      


  