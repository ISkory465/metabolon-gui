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
        self.button = ToggleButton(name=buttonName)
        self.vbox0.addWidget(self.button)

        # Left elements of the row
        self.festSollwert11 = InfoField(name=sollwert11, buttonSymbol=1,dec_num=1)
        self.vbox1.addWidget(self.festSollwert11)

        # Right element of the row
        self.festSollwert12 = InfoField(name=solwert12)
        self.vbox2.addWidget(self.festSollwert12)

        # Second row
        # Left
        self.festSollwert21 = InfoField(name=solwert21,dec_num=3)
        self.vbox1.addWidget(self.festSollwert21)

        # Right
        self.festSollwert22 = InfoField(name=solwert22)
        self.vbox2.addWidget(self.festSollwert22)

        self.vbox0.addWidget(self.button)

        # Adding layouts to main layout
        self.mainLayout.addLayout(self.vbox0)
        self.mainLayout.addLayout(self.vbox1)
        self.mainLayout.addLayout(self.vbox2)

        # Setting spacing between elements in layouts
        self.vbox1.setSpacing(10)
        self.vbox2.setSpacing(10)
        self.mainLayout.setSpacing(10)

        self.setLayout(self.mainLayout)  # Set the main layout for the widget

    def update(self,inputs: dict):
        """method to update all objects in current tab periodically after reading the values in different thread

        :param inputs: tag values
        :type inputs: dict
        """
        objectList=[    self.festSollwert11,
                        self.festSollwert12,
                        self.festSollwert21,
                        self.festSollwert22
                    ]


        for o in objectList:
            #iterate over an update method that should be added to all faceplate objects similar to box object
            o.update(inputs)



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
        self.firstElement = InfoField(name =firstElement, 
                                 buttonSymbol=2) 
        self.vbox1.addWidget(self.firstElement)
        
        self.vbox0.addWidget(button1)
        #<-------------------------------------->
        #Second row
        button2 = UnlabelledButton()
        self.secondElement = InfoField(name =secondElement, 
                                 buttonSymbol=2)
        self.vbox1.addWidget(self.secondElement)
        
        self.vbox0.addWidget(button2)
        
        #Third row
        button3 = UnlabelledButton()
        self.thirdElement = InfoField(name =thirdElement, 
                          buttonSymbol=2)
        self.vbox1.addWidget(self.thirdElement)
        
        self.vbox0.addWidget(button3)
       
        #Fourth row
        button4 = UnlabelledButton()
        self.fourthElement = InfoField(name =fourthElement, 
                                  buttonSymbol=2)
        self.vbox1.addWidget(self.fourthElement)
        
        self.vbox0.addWidget(button4)

        #Fifth row
        button5 = UnlabelledButton()
        self.fifthElement = InfoField(name =fifthElement, 
                                 buttonSymbol=2)
        self.vbox1.addWidget(self.fifthElement)
        self.vbox0.addWidget(button5)
        
        #Six row
        button6 = UnlabelledButton()
        self.sixthElement = InfoField(name = sixthElement, 
                                 buttonSymbol=2)
        self.vbox1.addWidget(self.sixthElement)
        self.vbox0.addWidget(button6)
         
        #adding layouts to main layout
        self.mainLayout.addLayout(self.vbox0)
        self.mainLayout.addLayout(self.vbox1)
       
        #setting for adjasting space between elements in layouts
        self.vbox1.setSpacing(5)
        self.mainLayout.setSpacing(5)
       
        self.setLayout(self.mainLayout)
    
    def update(self,inputs: dict):
        """method to update all objects in current tab periodically after reading the values in different thread

        :param inputs: tag values
        :type inputs: dict
        """
        objectList=[    self.firstElement,
                        self.secondElement,
                        self.thirdElement,
                        self.fourthElement,
                        self.fifthElement,
                        self.sixthElement
                    ]


        for o in objectList:
            #iterate over an update method that should be added to all faceplate objects similar to box object
            o.update(inputs)

