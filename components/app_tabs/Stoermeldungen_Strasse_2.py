from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

from ..faceplates.faceplates_new import Led_6
from ..faceplates.faceplates_new import Led_8


class Page(QWidget):

    def __init__(self) -> None:

        super().__init__()
        self.UI()

    def UI(self):

        #Main layout of the first tab 'Störmeldungen Straße 2"
        grid = QGridLayout()

        #Page has 1 horizontal box:
        hbox=QHBoxLayout()    
        hbox.setAlignment(Qt.AlignCenter)

        #Horizontal hbox contains 2 vertical layouts
        vbox1=QVBoxLayout()
        vbox2=QVBoxLayout()

       
        #Elements of vbox1 and vbox2 for the hbox:
        self.led_l = Led_6(name="PU21 Antriebsstörung +FE02\
                            ,PU21 Trockenlaufstörung +FE02\
                            ,PU21 MaxDruckstörung +FE02\
                            ,PU22 Antriebsstörung +FE02\
                            ,PU22 Trockenlaufstörung +FE02\
                            ,PU22 MaxDruckstörung +FE02", layout=vbox1)
        self.led_r = Led_8(name="RW21 Antriebsstörung +FE03,RW21 FU-Störung +FE03\
                            ,RW22 Antriebsstörung +FE03\
                            ,RW22 FU-Störung +FE03\
                            ,RW23 Antriebsstörung +FE03\
                            ,RW23 FU-Störung +FE03\
                            ,RW24 Antriebsstörung +FE03\
                            ,RW24 FU-Störung +FE03", layout=vbox2)

        #Grid layout  
        grid.addLayout(vbox1, *[0,0])
        grid.addLayout(vbox2, *[0,1])

        #Grid settings
        grid.setAlignment(Qt.AlignCenter)
        grid.setHorizontalSpacing(30)
        grid.setSpacing(20)
        grid.setVerticalSpacing(60)
        
        #Assigning to the tab
        self.setLayout(grid) 
      
if __name__=='__main__':
    pass