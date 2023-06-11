from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from QLed import QLed

from ..test_element import *


class Page():

    def UI(self,window:QMainWindow):
        
        #Main layout of the first tab 'Störmeldungen Straße 1"
        grid = QGridLayout()

        #Layouts for the tab
        vbox1=QVBoxLayout()
        vbox2=QVBoxLayout()
        vbox3=QVBoxLayout()
        vbox4=QVBoxLayout()
        vbox5=QVBoxLayout()
        vbox6=QVBoxLayout()
        hbox1=QHBoxLayout()
        hbox2=QHBoxLayout()
        hbox3=QHBoxLayout()
        hbox=QHBoxLayout()   

        #Elements of vbox1
        self.led_l = Led_6(name="PU11 Antriebsstörung +FE02\
                            ,PU11 Trockenlaufstörung +FE02\
                            ,PU11 MaxDruckstörung +FE02\
                            ,PU12 Antriebsstörung +FE02\
                            ,PU12 Trockenlaufstörung +FE02\
                            ,PU12 MaxDruckstörung +FE02", layout=vbox1)
        #Elements of vbox2                            
        self.led_r = Led_8(name="RW11 Antriebsstorung +FE03,RW11 FU-Störung +FE03\
                            ,RW12 Antriebsstörung +FE03\
                            ,RW12 FU-Störung +FE03\
                            ,RW13 Antriebsstörung +FE03\
                            ,RW13 FU-Störung +FE03\
                            ,RW14 Antriebsstörung +FE03\
                            ,RW14 FU-Störung +FE03", layout=vbox2)
      
        #Elements of hbox1 and hbox2:
        self.led1 = Led(name="HE11 MaxTemp Störung +FE02", layout=hbox1)
        self.led2 = Led(name="HE12 MaxTemp Störung +FE02", layout=hbox2)

        #Elements of vbox4:        
        self.field1 = InfoFieldDouble(name = "DB84.TI15.FER1.SW",
                            layout = vbox4, dec_num = 4) 
        self.led3 = Led_DA(name="DB84.TI15.GW.SW", layout=vbox4) 

        #Elements of vbox5: 
        self.field2 = InfoFieldDouble(name = "DB81.NIV.LI15.GW.Max",
                            layout = vbox5, dec_num = 4)
        self.field3 = InfoFieldDouble(name = "DB81.NIV.LI15.GW.Mnn",
                            layout = vbox5, dec_num = 4)

        #Elements of vbox6: 
        self.field4 = InfoFieldDouble(name = "DB81.NIV.LI15.GW.Mxx",
                            layout = vbox6, dec_num = 4)

        #Layout settings 
        hbox.setAlignment(Qt.AlignCenter) 
        vbox6.setAlignment(Qt.AlignTop)
          
        #Layout relation 
        vbox3.addLayout(hbox1)
        vbox3.addLayout(hbox2)
        hbox3.addLayout(vbox5)
        hbox3.addLayout(vbox6)

        #Grid layout
        grid.addLayout(vbox1, *[0,0])
        grid.addLayout(vbox2, *[0,1])
        grid.addLayout(vbox3, *[1,0])
        grid.addLayout(vbox4, *[2,0])
        grid.addLayout(hbox3, *[2,1])
        
        #Grid settings        
        grid.setAlignment(Qt.AlignCenter)
        grid.setHorizontalSpacing(30)
        grid.setSpacing(20)
        grid.setVerticalSpacing(60)
        
        #Assigning to the tab
        window.tab6.setLayout(grid)
    
    def updateAll(self,inputs: dict):
        """method to update all objects in current tab periodically after reading the values in different thread

        :param inputs: tag values
        :type inputs: dict
        """
        objectList=[self.led_l,
                    self.led_r,
                    
                    self.led1,
                    self.led2,
                    self.led3,

                    self.field1,
                    self.field2,
                    self.field3,
                    self.field4
                    ]


        for o in objectList:
            #iterate over an update method that should be added to all faceplate objects similar to box object
            o.update(inputs)
if __name__=='__main__':
    pass