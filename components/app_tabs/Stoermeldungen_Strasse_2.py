from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt



def UI(self):
    #Main layout of the first tab 'Störmeldungen Straße 2"
    vbox=QVBoxLayout()
    

    #test element:
    hbox=QHBoxLayout()
    label = QLabel('Marina')
    
    hbox.addWidget(label)
    vbox.addLayout(hbox)
    vbox.setAlignment(Qt.AlignTop)

    #Assigning to the tab
    self.tab6.setLayout(vbox)


if __name__=='__main__':
    UI()