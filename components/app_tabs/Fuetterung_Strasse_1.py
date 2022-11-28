from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt



def UI(self):
    #Main layout of the first tab 'Straße 1"
    vbox=QVBoxLayout()
    

    #test element:
    hbox=QHBoxLayout()
    label = QLabel('Adilkhan')
    
    hbox.addWidget(label)
    vbox.addLayout(hbox)
    vbox.setAlignment(Qt.AlignTop)

    #Assigning to the tab
    self.tab5.setLayout(vbox)


if __name__=='__main__':
    UI()