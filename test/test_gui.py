import sys
from PyQt5.QtWidgets import *
from faceplates import Box
from test_element import Mixer




class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Metabolo Station")
        self.setGeometry(350,150,600,600)
        self.UI()

    def UI(self):
        mainLayout=QVBoxLayout()
        self.tabs =QTabWidget()

        self.tab1=QWidget()
        self.tab2=QWidget()
        self.tab3=QWidget()
        self.tabs.addTab(self.tab1,"Straße 1")
        self.tabs.addTab(self.tab2,"Straße 2")
        self.tabs.addTab(self.tab3,"Steuerung Straße 1")



        #Main layout of the first tab 'Straße 1"
        vbox=QVBoxLayout()

        #Layout for each Mixer Object
        vbox1=QVBoxLayout()
        vbox2=QVBoxLayout()
        vbox2_2=QVBoxLayout()

        #Layout that contains two vertically stacked sets of the Radio buttons:
        vbox3=QVBoxLayout()

        #Dummy layout for adjusting positioning of the radio buttons
        vbox4=QVBoxLayout()

        #Contain Mixer Objects for vbox1 and vbox2 Layouts
        hbox=QHBoxLayout()

        #Contain Radio Buttons objects for vbox3 and vbox4
        hbox1=QHBoxLayout()
        



        mixer1 = Mixer("Fermenter")
        vbox1.addWidget(mixer1)

        mixer2 = Mixer("Nachgärer")
        vbox2.addWidget(mixer2)

        hbox.addLayout(vbox1, 30)
        hbox.addLayout(vbox2, 30)
        hbox.addLayout(vbox2_2, 40)
        vbox.addLayout(hbox)
        
        
    
    
        facePlate1=Box('HE11','A12CH2')
        vbox3.addWidget(facePlate1)
        facePlate2=Box('RW13','A15CH11')
        vbox3.addWidget(facePlate2)

        hbox1.addLayout(vbox3,25)
        hbox1.addLayout(vbox4,75)


        vbox.addLayout(hbox1)
        self.tab1.setLayout(vbox)



        # self.tab2.setLayout(hbox)
 





        mainLayout.addWidget(self.tabs)
        self.setLayout(mainLayout)
        self.opclist=['Random.Int4','Random.Int8']


        self.show()


def main():
    App=QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())

if __name__=='__main__':
    main()