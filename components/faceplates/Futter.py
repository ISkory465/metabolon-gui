from threading import local
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from QLed import QLed
from ..widgets.infofield_dbl import InfoField
from ..widgets.toggle_button import ToggleButton, UnlabelledButton

class Futter1(QWidget):
    """Mixer set of elements for the Strasse 1 tab
    :param QGroupBox: _description_
    :type QGroupBox: _type_
    """
    
    def __init__(self, buttonName, sollwert11, solwert12, solwert21, solwert22, opcID=None):
        super().__init__()

        self.mainLayout = QHBoxLayout()
        self.vbox0 = QVBoxLayout()
        self.vbox1 = QVBoxLayout()
        self.vbox2 = QVBoxLayout()

        # First row 
        button = ToggleButton(name=buttonName)
        self.vbox0.addWidget(button)

        # Left elements of the row
        festSollwert11 = InfoField(name=sollwert11, buttonSymbol=1)
        self.vbox1.addWidget(festSollwert11)

        # Right element of the row
        festSollwert12 = InfoField(name=solwert12)
        self.vbox2.addWidget(festSollwert12)

        # Second row
        # Left
        festSollwert21 = InfoField(name=solwert21)
        self.vbox1.addWidget(festSollwert21)

        # Right
        festSollwert22 = InfoField(name=solwert22)
        self.vbox2.addWidget(festSollwert22)

        self.vbox0.addWidget(button)

        # Adding layouts to main layout
        self.mainLayout.addLayout(self.vbox0)
        self.mainLayout.addLayout(self.vbox1)
        self.mainLayout.addLayout(self.vbox2)

        # Setting spacing between elements in layouts
        self.vbox1.setSpacing(10)
        self.vbox2.setSpacing(10)
        self.mainLayout.setSpacing(10)

        self.setLayout(self.mainLayout)  # Set the main layout for the widget



class Feststoffbtn(QGroupBox):
    def __init__(self, firstElement, secondElement, thirdElement, fourthElement, fifthElement, sixthElement, opcID='opcID'):
        super().__init__()
        self.setFlat(True)
        #self.layout = QVBoxLayout #vbox 
        self.mainLayout=QHBoxLayout()
        self.vbox0=QVBoxLayout()
        self.vbox1=QVBoxLayout()
    
        #<-------------------------------------->
        #first row 
        button1 = UnlabelledButton()
        #Left elements of the row
        firstElement = InfoField(name =firstElement, 
                                 buttonSymbol=2) 
        self.vbox1.addWidget(firstElement)
        
        self.vbox0.addWidget(button1)
        #<-------------------------------------->
        #Second row
        button2 = UnlabelledButton()
        secondElement = InfoField(name =secondElement, 
                                 buttonSymbol=2)
        self.vbox1.addWidget(secondElement)
        
        self.vbox0.addWidget(button2)
        
        #Third row
        button3 = UnlabelledButton()
        thirdElement = InfoField(name =thirdElement, 
                          buttonSymbol=2)
        self.vbox1.addWidget(thirdElement)
        
        self.vbox0.addWidget(button3)
       
        #Fourth row
        button4 = UnlabelledButton()
        fourthElement = InfoField(name =fourthElement, 
                                  buttonSymbol=2)
        self.vbox1.addWidget(fourthElement)
        
        self.vbox0.addWidget(button4)

        #Fifth row
        button5 = UnlabelledButton()
        fifthElement = InfoField(name =fifthElement, 
                                 buttonSymbol=2)
        self.vbox1.addWidget(fifthElement)
        self.vbox0.addWidget(button5)
        
        #Six row
        button6 = UnlabelledButton()
        sixthElement = InfoField(name = sixthElement, 
                                 buttonSymbol=2)
        self.vbox1.addWidget(sixthElement)
        self.vbox0.addWidget(button6)
         
        #adding layouts to main layout
        self.mainLayout.addLayout(self.vbox0)
        self.mainLayout.addLayout(self.vbox1)
       
        #setting for adjasting space between elements in layouts
        self.vbox1.setSpacing(5)
        self.mainLayout.setSpacing(5)
       
        self.setLayout(self.mainLayout)

