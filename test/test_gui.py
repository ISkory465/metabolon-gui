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



        ###################Widgets###############
        vbox=QVBoxLayout()


        vbox1=QVBoxLayout()
        vbox2=QVBoxLayout()

        hbox=QHBoxLayout()
        hbox1=QHBoxLayout()
        hbox2=QHBoxLayout()



        mixer1 = Mixer("Fermenter")
        vbox.addWidget(mixer1)

        mixer2 = Mixer("Nachgärer")
        vbox.addWidget(mixer2)

        # hbox1.addLayout(vbox, 50)
        # hbox1.addLayout(vbox, 50)
        # hbox1.addLayout()
        
    
    
        facePlate1=Box('HE11','A12CH2')
        vbox1.addWidget(facePlate1)
        facePlate2=Box('RW13','A15CH11')
        vbox1.addWidget(facePlate2)

        hbox2.addLayout(vbox1,25)
        hbox2.addLayout(vbox2,75)


        vbox.addLayout(hbox2)
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