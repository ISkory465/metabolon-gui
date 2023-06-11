from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from QLed import QLed

from ..test_element import Box
from ..test_element import InfoField
from ..test_element import SingleLed
from ..test_element import Led_6
from ..test_element import Led_8


class Page():

    def UI(self,window:QMainWindow):

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
        window.tab7.setLayout(grid) 
    def updateAll(self,inputs: dict):
        """method to update all objects in current tab periodically after reading the values in different thread

        :param inputs: tag values
        :type inputs: dict
        """
        objectList=[self.led_l,
                    self.led_r
                    
                    ]


        for o in objectList:
            #iterate over an update method that should be added to all faceplate objects similar to box object
            o.update(inputs)
      
if __name__=='__main__':
    pass