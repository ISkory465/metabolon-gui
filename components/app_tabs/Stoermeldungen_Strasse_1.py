from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from QLed import QLed

from ..test_element import Box
from ..test_element import InfoField
from ..test_element import SingleLed
from ..test_element import Led_6
from ..test_element import Led_8


class Page():

    def UI(self, window:QMainWindow):
        #Main layout of the first tab 'Störmeldungen Straße 2"
        grid = QGridLayout()
        vbox1=QVBoxLayout()
        vbox2=QVBoxLayout()

        #test element:
        hbox=QHBoxLayout()

        board_layout = QFormLayout()
        
    
        #label = QLabel('Marina')

        hbox.setAlignment(Qt.AlignCenter)
        # vbox1.setAlignment(Qt.AlignCenter)
        # vbox2.setAlignment(Qt.AlignCenter)
        #hbox.addWidget(label)

        #Second column elements of vbox6 for the hbox2:

        led_l = Led_6(name="PU21 Antriebsstörung +FE02\
                            ,PU21 Trockenlaufstörung +FE02\
                            ,PU21 MaxDruckstörung +FE02\
                            ,PU22 Antriebsstörung +FE02\
                            ,PU22 Trockenlaufstörung +FE02\
                            ,PU22 MaxDruckstörung +FE02", layout=vbox1)
        led_r = Led_8(name="RW21 Antriebsstörung +FE03\
                            ,RW21 FU-Störung +FE03\
                            ,RW22 Antriebsstörung +FE03\
                            ,RW22 FU-Störung +FE03\
                            ,RW23 Antriebsstörung +FE03\
                            ,RW23 FU-Störung +FE03\
                            ,RW24 Antriebsstörung +FE03\
                            ,RW24 FU-Störung +FE03", layout=vbox2)

        

        #hbox.addLayout(vbox1,2)
        #hbox.addLayout(vbox2,1)

        
        #vbox1.add

        #board_layout.addRow(vbox1)
        #board_layout.addRow(vbox2)
        #grid.setContentsMargins(10,10,20,20)
        grid.addLayout(vbox1, *[0,0])
        grid.addLayout(vbox2, *[0,1])

    #grid.addWidget(led1)
        #grid.addWidget(led2)


        #self.sliderframe = QFrame(self.tab6)
        #self.sliderframe.setFixedHeight(450)
        #self.sliderframe.setFixedWidth(90)
        #self.sliderframe.setStyleSheet("border: 1px solid grey; background: 0%;")
        #self.sliderframe.setGeometry(200, 100, 450, 200)

        #grid.addLayout(hbox, *[0,0])
        
        
        #grid.setSpacing(10)
        grid.setAlignment(Qt.AlignCenter)
        grid.setHorizontalSpacing(30)
        grid.setSpacing(20)
        grid.setVerticalSpacing(60)
        
        #Assigning to the tab
        window.tab6.setLayout(grid)
        #self.addWidget(self.tab6)

 
      

if __name__=='__main__':
    UI()