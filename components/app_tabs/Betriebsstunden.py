from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt



def UI(self):
    #Main layout of the first tab 'Betriebsstunden"
    vbox=QVBoxLayout()
    

    #test element:
    hbox=QHBoxLayout()
    label = QLabel('Marina Betriebsstunden')
    
    hbox.addWidget(label)
    vbox.addLayout(hbox)
    vbox.setAlignment(Qt.AlignTop)
    

    #Assigning to the tab
    self.tab7.setLayout(vbox)


if __name__=='__main__':
    UI()