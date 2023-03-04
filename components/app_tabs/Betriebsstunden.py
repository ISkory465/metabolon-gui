from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from ..test_element import InfoField
from ..test_element import InfoFieldDouble

class Page():

    def UI(self, window:QMainWindow):
        
        #Main layout of the first tab 'Betriebsstunden"
        vbox1_1=QVBoxLayout()
        vbox1_2=QVBoxLayout()

        vbox2_1=QVBoxLayout()
        vbox2_2=QVBoxLayout()
        vbox2_3=QVBoxLayout()

        hbox1=QHBoxLayout()
        hbox2=QHBoxLayout()

        grid = QGridLayout()


        self.field1_1 = InfoFieldDouble(name = "HE11_BH",
                            layout = vbox1_1, dec_num = 2)
        self.field1_2 = InfoFieldDouble(name = "HE12_BH",
                            layout = vbox1_1, dec_num = 0)
        self.field1_3 = InfoFieldDouble(name = "HE21_BH",
                            layout = vbox1_2, dec_num = 0)
        self.field1_4 = InfoFieldDouble(name = "HE22_BH",
                            layout = vbox1_2, dec_num = 0)   


        self.field2_1 = InfoFieldDouble(name = "PU11_BH",
                            layout = vbox2_1, dec_num = 3)
        self.field2_2 = InfoFieldDouble(name = "PU12_BH",
                            layout = vbox2_1, dec_num = 4)
        self.field2_3 = InfoFieldDouble(name = "PU21_BH",
                            layout = vbox2_2)
        self.field2_4 = InfoFieldDouble(name = "PU22_BH",
                            layout = vbox2_2, dec_num = 4)       
        self.field2_5 = InfoFieldDouble(name = "PU31_BH",
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
        window.tab8.setLayout(grid)



    def updateAll(self,inputs: dict):
        """method to update all objects in current tab periodically after reading the values in different thread

        :param inputs: tag values
        :type inputs: dict
        """
        objectList=[self.field1_1,
                    self.field1_2,
                    self.field1_3,
                    self.field1_4,

                    self.field2_1,
                    self.field2_2,
                    self.field2_3,
                    self.field2_4,
                    self.field2_5]


        for o in objectList:
            #iterate over an update method that should be added to all faceplate objects similar to box object
            o.update(inputs)
        

if __name__=='__main__':
    pass