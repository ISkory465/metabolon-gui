from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

from ..widgets.box import Box
from ..widgets.infofield_dbl import InfoField
from ..faceplates.faceplates_new import SingleLed


class Page(QWidget):

    def __init__(self) -> None:

        super().__init__()
        self.UI()

    def UI(self):
        
        #Main layout of the first window 'Steuerung_Strasse_2"
        vbox=QVBoxLayout()
        
        #Page has 2 horizontal boxes:
        hbox1=QHBoxLayout()
        hbox2=QHBoxLayout()

        #First horizontal hbox1 contains Three vertical layouts
        vbox1=QVBoxLayout()
        vbox2=QVBoxLayout()
        vbox2_2=QVBoxLayout()
        vbox3=QVBoxLayout()
        vbox3_3=QVBoxLayout()

        #Second horizontal hbox2 contains Two vertical layouts
        vbox4=QVBoxLayout()
        vbox5=QVBoxLayout()    
        vbox6=QVBoxLayout()



        #hbox1
        #----------------------FIRST COLUMN--------------------
        #First column elements of vbox1 for the hbox1:

        self.box1 = Box("HE11")
        vbox1.addWidget(self.box1)
        
        self.field1_1 = InfoField(name="Fermenter Temp.-Sollwert (\N{DEGREE SIGN}C)")
        vbox1.addWidget(self.field1_1)
        self.field1_2 = InfoField(name="Temp. Vorlauf Fer 1 (\N{DEGREE SIGN}C)")
        vbox1.addWidget(self.field1_2)
        self.field1_3 = InfoField(name="Temp. Fer 1 (\N{DEGREE SIGN}C)")
        vbox1.addWidget(self.field1_3)
        
        #Settings for the vbox1 (First Column of the hbox1)
        vbox1.setAlignment(Qt.AlignTop)
        vbox1.setSpacing(5)
        
        
    #----------------------SECOND COLUMN--------------------
        #Second column elements of vbox1 for the hbox1:
        self.box2 = Box("RW13")
        vbox2.addWidget(self.box2)
        
        self.field2_1 = InfoField(name="RW13 Auto Sollwert [%]")
        vbox2.addWidget(self.field2_1)
        self.field2_2 = InfoField(name="RW13 Hand Sollwert [%]")
        vbox2.addWidget(self.field2_2)
        self.field2_3 = InfoField(name="RW13 Pause Soll [min] ln")
        vbox2.addWidget(self.field2_3)
        self.field2_4 = InfoField(name="RW13 Run Soll [min] ln")
        vbox2.addWidget(self.field2_4)

        #Settings for the vbox2 (First Column of the hbox1)
        vbox2.setAlignment(Qt.AlignTop)
        vbox2.setSpacing(5)


    #----------------------THIRD COLUMN--------------------
        self.field2_add = InfoField(name="RW13.SW_AKT [%]")
        vbox2_2.addWidget(self.field2_add)
        
        #Settings for the vbox2_2 (Third Column of the hbox1)
        vbox2_2.setAlignment(Qt.AlignBottom)
        vbox2_2.setSpacing(5)                    

    #----------------------FOURTH COLUMN--------------------
        #Fourth column elements of vbox3 for the hbox1:
        self.box3 = Box("SC11")
        vbox3.addWidget(self.box3)

        self.field3_1 = InfoField(name="RW12 Auto Sollwert [%]")
        vbox3.addWidget(self.field3_1)
        self.field3_2 = InfoField(name="RW12 Hand Sollwert [%]")
        vbox3.addWidget(self.field3_2)
        self.field3_3 = InfoField(name="RW12 Pause Soll [min] ln")
        vbox3.addWidget(self.field3_3)
        self.field3_4 = InfoField(name="RW12 Run Soll [min] ln")
        vbox3.addWidget(self.field3_4)

        #Settings for the vbox3 (Third Column of the hbox1)
        vbox3.setAlignment(Qt.AlignTop)
        vbox3.setSpacing(5)


    #----------------------FIFTH COLUMN--------------------
        #Fifth column elements of vbox3_3 for the hbox1:
        
        self.field3_1a = InfoField(name="RW11 Auto Sollwert [%]")
        vbox3_3.addWidget(self.field3_1a)
        self.field3_2a = InfoField(name="RW11 Hand Sollwert [%]")
        vbox3_3.addWidget(self.field3_2a)
        self.field3_3a = InfoField(name="RW11 Pause Soll [min] ln")
        vbox3_3.addWidget(self.field3_3a)
        self.field3_4a = InfoField(name="RW11 Run Soll [min] ln")
        vbox3_3.addWidget(self.field3_4a)

        #Settings for the vbox3 (Third Column of the hbox1)
        vbox3_3.setAlignment(Qt.AlignBottom)
        vbox3_3.setSpacing(5)

        #Settings for the hbox1:
        hbox1.setAlignment(Qt.AlignTop)
        hbox1.setSpacing(10)
        hbox1.addLayout(vbox1, 2)
        hbox1.addLayout(vbox2, 2)
        hbox1.addLayout(vbox2_2, 1)
        hbox1.addLayout(vbox3, 2)
        hbox1.addLayout(vbox3_3, 2)




        #hbox2
        #----------------------FIRST COLUMN--------------------
        #First column elements of vbox4 for the hbox2:
        self.box4 = Box("HE12")
        vbox4.addWidget(self.box4)
        
        self.field3_1b = InfoField(name="Nachgärer Temp.-Sollwert [\N{DEGREE SIGN}C]")
        vbox4.addWidget(self.field3_1b)
        self.field3_2b = InfoField(name="Temp. Vorlauf Ng 1 [\N{DEGREE SIGN}C]")
        vbox4.addWidget(self.field3_2b)
        self.field3_3b = InfoField(name="Temp. Ng 1 [\N{DEGREE SIGN}C]")
        vbox4.addWidget(self.field3_3b)     

        #Settings for the vbox4 (First Column of the hbox2)
        vbox4.setAlignment(Qt.AlignTop)
        vbox4.setSpacing(5)                                            
        
        #----------------------SECOND COLUMN--------------------
        #Second column elements of vbox5 for the hbox2:
        self.box5 = Box("RW14")
        vbox5.addWidget(self.box5)

        self.field4_1 = InfoField(name="RW14 Auto Sollwert [%]")
        vbox5.addWidget(self.field4_1)
        self.field4_2 = InfoField(name="RW14 Hand Sollwert [%]")
        vbox5.addWidget(self.field4_2)
        self.field4_3 = InfoField(name="RW14 Pause Soll [min] ln")
        vbox5.addWidget(self.field4_3)
        self.field4_4 = InfoField(name="RW14 Run Soll [min] ln")
        vbox5.addWidget(self.field4_4)
        #Settings for the vbox5 (First Column of the hbox2)
        vbox5.setAlignment(Qt.AlignTop)
        vbox5.setSpacing(5)                    


        #----------------------FIFTH COLUMN--------------------
        #Second column elements of vbox6 for the hbox2:
        vbox3_3_2=QVBoxLayout()  # New QVBoxLayout
        self.led1 = SingleLed(name="Magentgasventill Fer 1", layout=vbox6)
        self.led2 = SingleLed(name="Magentgasventill Fer 2", layout=vbox6)
        
        #settings for the vbox6:
        vbox6.setAlignment(Qt.AlignTop)
        vbox6.setSpacing(5)   
        vbox6.setContentsMargins(0, 15, 10, 0)

        #Settings for the hbox2:
        hbox2.setAlignment(Qt.AlignTop)
        hbox2.setSpacing(10)
        hbox2.setContentsMargins(0, 10, 0, 0)

        #Add columns(vbox4, vbox5 vbox3_3(dummy)) to the hbox2
        hbox2.addLayout(vbox4, 1)
        hbox2.addLayout(vbox5, 1)
        hbox2.addLayout(vbox6, 1)
        hbox2.addLayout(vbox3_3_2, 1)  # use vbox3_3_2 instead of vbox3_3

        #Adding two horizontal layouts (hbox1, hbox2) to the layout of the page
        vbox.addLayout(hbox1, 50)
        vbox.addLayout(hbox2, 50)

        #Assigning page layout to the window
        self.setLayout(vbox)




    def updateAll(self, inputs: dict):
        """method to update all objects in current tab periodically after reading the values in different thread

        :param inputs: tag values
        :type inputs: dict
        """
        objectList = [
            self.box1,
            self.box2,
            self.box3,
            self.box4,
            self.box5,
            
            self.field1_1,
            self.field1_2,
            self.field1_3,

            self.field2_1,
            self.field2_2,
            self.field2_3,
            self.field2_4,
            self.field2_add,

            self.field3_1,
            self.field3_1a,
            self.field3_1b,

            self.field3_2,
            self.field3_2a,
            self.field3_2a,

            self.field3_3,
            self.field3_3a,
            self.field3_3b,

            self.field3_4,
            self.field3_4a,

            self.field4_1,
            self.field4_2,
            self.field4_3,
            self.field4_4,

            self.led1,
            self.led2
        ]

        for o in objectList:
            #iterate over an update method that should be added to all faceplate objects similar to box object
            o.update(inputs)


if __name__ == '__main__':
    app = QApplication([])
    window = QMainWindow()
    window.setWindowTitle("Page Test")
    page = Page()
    page.UI()
    window.setCentralWidget(page)
    window.show()
    app.exec_()
