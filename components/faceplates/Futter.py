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

    @classmethod
    def set_all_states(cls, state):
        for instance in cls.instances:
            instance.state = state
            instance.spin.setEnabled(state)


# Field for Double parameter with decimal setting
# Example if dec_num = 2 you get 10,00
# If dec_num = 4 - 10,0000
# Default dec_num is 2


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
