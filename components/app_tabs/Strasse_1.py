from tkinter import N
from unicodedata import name
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from ..test_element import Box
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
    mixer1 = Mixer(name="Fermenter", layout=vbox1)
    # vbox1.addWidget(mixer1)

    mixer2 = Mixer(name="Nachgärer", layout=vbox2)
    # vbox2.addWidget(mixer2)

    hbox.addLayout(vbox1, 1)
    hbox.addLayout(vbox2, 1)
    hbox.addLayout(vbox2_2, 2)
    hbox.setAlignment(Qt.AlignTop)
    hbox.setSpacing(5)

    #Assigning to the tab
    vbox.addLayout(hbox)
    

    #Add Radio Buttons Objects
    #Without 2nd position argument app crashes; opcid=None does not work properly; fix - change to defalt string.
    box1=Box(name='HE11', layout=vbox3, opcID='A12CH2')
    box2=Box(name='RW13',layout=vbox3, opcID='A15CH11')  
    box3=Box(name='PU11', layout=vbox3_1)   
    box4=Box(name='PU13', layout=vbox3_1)   
    box5=Box(name='RW11', layout=vbox3_2)    
    box6=Box(name='RW12', layout=vbox3_2)

    box7=Box(name='AA11', layout=vbox3_3)    
    box8=Box(name='AA12', layout=vbox3_3)    
    box9=Box(name='AA13', layout=vbox3_4)   
    box10=Box(name='AA14', layout=vbox3_4)
    

    hbox1.addLayout(vbox3,15)
    hbox1.addLayout(vbox3_1,15)
    hbox1.addLayout(vbox3_2,15)
    hbox1.addLayout(vbox3_3,15)
    hbox1.addLayout(vbox3_4,15)
    hbox1.addLayout(vbox4,30)
    hbox1.setAlignment(Qt.AlignBottom)
    hbox1.setSpacing(5)

    #Assigning to the tab
    vbox.addLayout(hbox1)
    self.tab1.setLayout(vbox)


if __name__=='__main__':
    UI()