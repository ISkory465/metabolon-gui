from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from QLed import QLed

from components.widgets.leds import SingleLed, LedGroupBox
from ..widgets.infofield_dbl import InfoField


class Page(QWidget):

    def __init__(self) -> None:

        super().__init__()
        self.UI()

    def UI(self):
        
        # Main layout of the first tab 'Stoermeldungen Straße 1"
        grid = QGridLayout()

        # Layouts for the tab
        vbox1 = QVBoxLayout()
        vbox2 = QVBoxLayout()
        vbox3 = QVBoxLayout()
        vbox4 = QVBoxLayout()
        vbox5 = QVBoxLayout()
        vbox6 = QVBoxLayout()
        hbox1 = QHBoxLayout()
        hbox2 = QHBoxLayout()
        hbox3 = QHBoxLayout()
        hbox = QHBoxLayout()   


        led_l = LedGroupBox("", ["PU11 Antriebsstoerung +FE02",
                                 "PU11 Trockenlaufstoerung +FE02",
                                 "PU11 MaxDruckstoerung +FE02",
                                 "PU12 Antriebsstoerung +FE02",
                                 "PU12 Trockenlaufstoerung +FE02",
                                 "PU12 MaxDruckstoerung +FE02"], [QLed.Green] * 6)
        led_l.setFixedHeight(300)
        led_l.setFixedWidth(250)
        vbox1.addWidget(led_l)
        #Testing
        led_l.set_led_state(3, True)


        led_r = LedGroupBox("", ["RW11 Antriebsstoerung +FE03",
                                 "RW11 FU-Stoerung +FE03",
                                 "RW12 Antriebsstoerung +FE03",
                                 "RW12 FU-Stoerung +FE03",
                                 "RW13 Antriebsstoerung +FE03",
                                 "RW13 FU-Stoerung +FE03",
                                 "RW14 Antriebsstoerung +FE03",
                                 "RW14 FU-Stoerung +FE03"], [QLed.Green] * 8)
        led_r.setFixedHeight(300)
        led_r.setFixedWidth(250)
        vbox2.addWidget(led_r)
        #Testing
        led_r.set_led_state(2, True)
        led_r.set_led_state(4, True)

      
        # Elements of vbox3
        HE_leds = LedGroupBox("", ["HE11 MaxTemp Stoerung +FE02", "HE12 MaxTemp Stoerung +FE02"], [QLed.Green] * 2)
        HE_leds.setFixedHeight(100)
        HE_leds.setFixedWidth(250)
        vbox3.addWidget(HE_leds)


        # Elements of vbox4:        
        self.field1 = InfoField(name="DB84.TI15.FER1.SW", dec_num=4) 
        vbox4.addWidget(self.field1)
        self.led3 = SingleLed(name="DB84.TI15.GW.SW")
        vbox4.addWidget(self.led3)

        # Elements of vbox5: 
        self.field2 = InfoField(name="DB81.NIV.LI15.GW.Max", dec_num=4)
        vbox5.addWidget(self.field2)
        self.field3 = InfoField(name="DB81.NIV.LI15.GW.Mnn", dec_num=4)
        vbox5.addWidget(self.field3)

        # Elements of vbox6: 
        self.field4 = InfoField(name="DB81.NIV.LI15.GW.Mxx", dec_num=4)
        vbox6.addWidget(self.field4)

        # Layout settings 
        hbox.setAlignment(Qt.AlignCenter) 
        vbox6.setAlignment(Qt.AlignTop)
          
        # Layout relation 
        vbox3.addLayout(hbox1)
        vbox3.addLayout(hbox2)
        hbox3.addLayout(vbox5)
        hbox3.addLayout(vbox6)

        # Grid layout
        grid.addLayout(vbox1, 0, 0)
        grid.addLayout(vbox2, 0, 1)
        grid.addLayout(vbox3, 1, 0)
        grid.addLayout(vbox4, 2, 0)
        grid.addLayout(hbox3, 2, 1)
        
        # Grid settings        
        grid.setAlignment(Qt.AlignCenter)
        grid.setHorizontalSpacing(30)
        grid.setSpacing(20)
        grid.setVerticalSpacing(60)
        
        # Assigning to the tab
        self.setLayout(grid)
    
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