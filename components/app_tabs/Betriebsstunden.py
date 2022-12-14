from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from ..test_element import InfoField
from ..test_element import InfoFieldDouble


def UI(self):
    #Main layout of the first tab 'Betriebsstunden"
    vbox1_1=QVBoxLayout()
    vbox1_2=QVBoxLayout()

    vbox2_1=QVBoxLayout()
    vbox2_2=QVBoxLayout()
    vbox2_3=QVBoxLayout()

    hbox1=QHBoxLayout()
    hbox2=QHBoxLayout()

    grid = QGridLayout()


    field1_1 = InfoFieldDouble(name = "HE11_BH",
                         layout = vbox1_1, dec_num = 2)
    field1_2 = InfoFieldDouble(name = "HE12_BH",
                         layout = vbox1_1, dec_num = 0)
    field1_3 = InfoFieldDouble(name = "HE21_BH",
                         layout = vbox1_2, dec_num = 0)
    field1_4 = InfoFieldDouble(name = "HE22_BH",
                         layout = vbox1_2, dec_num = 0)   


    field2_1 = InfoFieldDouble(name = "PU11_BH",
                         layout = vbox2_1, dec_num = 3)
    field2_2 = InfoFieldDouble(name = "PU12_BH",
                         layout = vbox2_1, dec_num = 4)
    field2_3 = InfoFieldDouble(name = "PU21_BH",
                         layout = vbox2_2)
    field2_4 = InfoFieldDouble(name = "PU22_BH",
                         layout = vbox2_2, dec_num = 4)       
    field2_5 = InfoFieldDouble(name = "PU31_BH",
                         layout = vbox2_3, dec_num = 4)   

    vbox2_3.setAlignment(Qt.AlignTop)

    hbox1.addLayout(vbox1_1)
    hbox1.addLayout(vbox1_2)

    hbox2.addLayout(vbox2_1)
    hbox2.addLayout(vbox2_2)
    hbox2.addLayout(vbox2_3)

    hbox1.setAlignment(Qt.AlignTop)
    hbox1.setSpacing(5)

    hbox2.setAlignment(Qt.AlignTop)
    hbox2.setSpacing(5)

    grid.setAlignment(Qt.AlignCenter)
    grid.setSpacing(50)

    grid.addLayout(hbox1, *[1,0])
    grid.addLayout(hbox2, *[1,1])
  

    #Assigning to the tab
    self.tab7.setLayout(grid)


if __name__=='__main__':
    UI()