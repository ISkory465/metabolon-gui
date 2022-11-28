from PyQt5.QtWidgets import *
from ..faceplates import Box
from ..test_element import Mixer



def UI(self):
    #Main layout of the first tab 'Straße 1"
    vbox=QVBoxLayout()

    #Layout for each Mixer Object
    vbox1=QVBoxLayout()
    vbox2=QVBoxLayout()
    vbox2_2=QVBoxLayout()

    #Layout that contains two vertically stacked sets of the Radio buttons:
    vbox3=QVBoxLayout()
    vbox3_1=QVBoxLayout()
    vbox3_2=QVBoxLayout()
    vbox3_3=QVBoxLayout()
    vbox3_4=QVBoxLayout()

    #Dummy layout for adjusting positioning of the radio buttons
    vbox4=QVBoxLayout()

    #Contain Mixer Objects for vbox1 and vbox2 Layouts
    hbox=QHBoxLayout()

    #Contain Radio Buttons objects for vbox3 and vbox4
    hbox1=QHBoxLayout()
    

    #Add Mixer Objects
    mixer1 = Mixer("Fermenter")
    vbox1.addWidget(mixer1)

    mixer2 = Mixer("Nachgärer")
    vbox2.addWidget(mixer2)

    hbox.addLayout(vbox1, 30)
    hbox.addLayout(vbox2, 30)
    hbox.addLayout(vbox2_2, 40)

    #Assigning to the tab
    vbox.addLayout(hbox)
    

    #Add Radio Buttons Objects
    #Without 2nd position argument app crashes; opcid=None does not work properly; fix - change to defalt string.
    facePlate1=Box('HE11','A12CH2')
    vbox3.addWidget(facePlate1)
    facePlate2=Box('RW13','A15CH11')
    vbox3.addWidget(facePlate2)

    facePlate3=Box('PU11')
    vbox3_1.addWidget(facePlate3)
    facePlate4=Box('PU13')
    vbox3_1.addWidget(facePlate4)

    facePlate5=Box('RW11')
    vbox3_2.addWidget(facePlate5)
    facePlate6=Box('RW12')
    vbox3_2.addWidget(facePlate6)

    facePlate7=Box('AA11')
    vbox3_3.addWidget(facePlate7)
    facePlate8=Box('AA12')
    vbox3_3.addWidget(facePlate8)

    facePlate9=Box('AA13')
    vbox3_4.addWidget(facePlate9)
    facePlate10=Box('AA14')
    vbox3_4.addWidget(facePlate10)

    hbox1.addLayout(vbox3,15)
    hbox1.addLayout(vbox3_1,15)
    hbox1.addLayout(vbox3_2,15)
    hbox1.addLayout(vbox3_3,15)
    hbox1.addLayout(vbox3_4,15)
    hbox1.addLayout(vbox4,30)

    #Assigning to the tab
    vbox.addLayout(hbox1)
    self.tab1.setLayout(vbox)


if __name__=='__main__':
    UI()