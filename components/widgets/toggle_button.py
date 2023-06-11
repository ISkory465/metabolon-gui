from threading import local
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class ToggleButton(QGroupBox):
    """Groupelement that combines QLabel and QPushbutton with settings to them
    :param QGroupBox: _description_
    :type QGroupBox: _type_
    """
    def __init__(self, name, opcID='None'):
      super().__init__()
      
      #remove QGroupBox frame
      self.setFlat(True) 
      self.layout = QVBoxLayout()
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
            
            
class UnlabelledButton(QGroupBox):
    """Groupelement that combines QLabel and QPushbutton with settings to them
    :param QGroupBox: _description_
    :type QGroupBox: _type_
    """

    def __init__(self, opcID='None'):
      super().__init__()
      self.setFlat(True)
      self.layout = QVBoxLayout()
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
