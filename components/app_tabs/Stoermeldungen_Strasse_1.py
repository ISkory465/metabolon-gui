from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from QLed import QLed

<<<<<<< HEAD
from ..test_element import Box
from ..test_element import InfoField
from ..test_element import SingleLed
from ..test_element import Led_6
from ..test_element import Led_8
=======
from ..test_element import *
>>>>>>> Garaeva


class Page():

<<<<<<< HEAD
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
=======
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
        led_l = Led_6(name="PU11 Antriebsstörung +FE02\
                            ,PU11 Trockenlaufstörung +FE02\
                            ,PU11 MaxDruckstörung +FE02\
                            ,PU12 Antriebsstörung +FE02\
                            ,PU12 Trockenlaufstörung +FE02\
                            ,PU12 MaxDruckstörung +FE02", layout=vbox1)
        #Elements of vbox2                            
        led_r = Led_8(name="RW11 Antriebsstörung +FE03\
                            ,RW11 FU-Störung +FE03\
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
>>>>>>> Garaeva
        grid.setAlignment(Qt.AlignCenter)
        grid.setHorizontalSpacing(30)
        grid.setSpacing(20)
        grid.setVerticalSpacing(60)
        
        #Assigning to the tab
        window.tab6.setLayout(grid)
<<<<<<< HEAD
        #self.addWidget(self.tab6)

 
      
=======
    
>>>>>>> Garaeva

if __name__=='__main__':
    pass