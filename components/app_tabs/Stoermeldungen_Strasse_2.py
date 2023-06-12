from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from QLed import QLed

from components.widgets.leds import LedGroupBox


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

        
        led_l = LedGroupBox("", ["PU21 Antriebsstörung +FE02", "PU21 Trockenlaufstörung +FE02",
                                 "PU21 MaxDruckstörung +FE02", "PU22 Antriebsstörung +FE02",
                                 "PU22 Trockenlaufstörung +FE02", "PU22 MaxDruckstörung +FE02"], [QLed.Green] * 6)
        led_l.setFixedHeight(300)
        led_l.setFixedWidth(250)
        vbox1.addWidget(led_l)
        # Testing
        led_l.set_led_state(5, True)
        
        
        led_r = LedGroupBox("", ["RW21 Antriebsstörung +FE03", "RW21 FU-Störung +FE03",
                                 "RW22 Antriebsstörung +FE03", "RW22 FU-Störung +FE03",
                                 "RW23 Antriebsstörung +FE03", "RW23 FU-Störung +FE03",
                                 "RW24 Antriebsstörung +FE03", "RW24 FU-Störung +FE03"], [QLed.Green] * 8)
        led_r.setFixedHeight(300)
        led_r.setFixedWidth(250)
        vbox2.addWidget(led_r)
        # Testing
        led_r.set_led_state(2, True)
        led_r.set_led_state(4, True)

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