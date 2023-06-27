from threading import local
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class ToggleButton(QFrame):
    """Groupelement that combines QLabel and QPushbutton with settings to them
    :param QGroupBox: _description_
    :type QGroupBox: _type_
    """
    def __init__(self, name, opcID='None'):
        super().__init__()

        self.layout = QVBoxLayout()
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setFixedWidth(150)

        # Header (QLabel) for the numerical field
        self.name = QLabel(name)
        self.layout.addWidget(self.name)

        # Creating a push button
        self.button = QPushButton(self)
        self.button.setFixedSize(100, 30)  # Set the size of the button

        # Styling the button
        self.button.setStyleSheet("""
             QPushButton {
                background-color: lightgrey;
                border: 1px solid darkgrey;
                border-radius: 5px;
                padding: 5px;
            }
            QPushButton:checked {
                background-color: green;
            }
        """)

        # setting checkable to true
        self.button.setCheckable(True)
        # setting calling method by button 
        self.button.clicked.connect(self.toggle) 
        self.layout.addWidget(self.button)  
        self.setLayout(self.layout)
    
    #<-------------------------------------->
    # action methods
    def toggle(self):
        if self.button.isChecked():
           print("Button 1 is checked")
        else:
           print("Button 1 is unchecked")
      
            
            
class UnlabelledButton(QFrame):
    """Groupelement that combines QLabel and QPushbutton with settings to them
    :param QGroupBox: _description_
    :type QGroupBox: _type_
    """

    def __init__(self, opcID='None'):
      super().__init__()
  
      self.layout = QVBoxLayout()
      self.layout.setSpacing(0)
      self.layout.setContentsMargins(0,0,0,0)
      self.setFixedHeight(20)
      self.setFixedWidth(20)
                        
      # creating a push button
      self.button = QPushButton("",self)
      # setting default color of button to light-grey
      self.button.setStyleSheet("""
            QPushButton {
                background-color: lightgrey;
                border: 1px solid darkgrey;
                border-radius: 5px;
                padding: 5px;
            }
            QPushButton:checked {
                background-color: green;
            }
        """)
                                            
      # setting checkable to true
      self.button.setCheckable(True)
      # setting calling method by button 
      self.button.clicked.connect(self.toggle) 
      self.layout.addWidget(self.button)  
      self.setLayout(self.layout)
      
    #<-------------------------------------->
    # action methods
    def toggle(self):
        if self.button.isChecked():
           pass
          #  print("Button 1 clicked")
