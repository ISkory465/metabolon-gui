from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from ..faceplates.facelpates_new import Box
from ..faceplates.facelpates_new import InfoField


class Page():

    def UI(self, window:QMainWindow):
        
        #Main layout of the first tab 'Steuerung_Strasse_2"
        vbox=QVBoxLayout()
        
        #Page has 2 horizontal boxes:
        hbox1=QHBoxLayout()
        hbox2=QHBoxLayout()

        #First horizontal hbox1 contains Three vertical layouts
        vbox1=QVBoxLayout()
        vbox2=QVBoxLayout()
        vbox3=QVBoxLayout()
        vbox3_3_1=QVBoxLayout() #Empty buffer to shift layout for hbox1

        #Second horizontal hbox2 contains Two vertical layouts
        vbox4=QVBoxLayout()
        vbox5=QVBoxLayout()    
        vbox3_3_2=QVBoxLayout() #Empty buffer to shift layout for hbox2




        #hbox1
        #----------------------FIRST COLUMN--------------------
        #First column elements of vbox1 for the hbox1:

        self.box1 = Box("HE21", vbox1)
        
        self.field1_1 = InfoField(name = "Fermenter Temp.-Sollwert [\N{DEGREE SIGN}C]",
                            layout = vbox1)
        self.field1_2 = InfoField(name = "D8400.HZG_REG.SZ_HE21",
                            layout = vbox1)
        self.field1_3 = InfoField(name = "Temp. Vorlauf Fer 2 [\N{DEGREE SIGN}C]",
                            layout = vbox1)
        self.field1_4 = InfoField(name = "Temp. Fer 2 [\N{DEGREE SIGN}C]",
                            layout = vbox1)
        self.field1_5 = InfoField(name = "Temp. Fer 2 [\N{DEGREE SIGN}C]",
                            layout = vbox1)


        #Settings for the vbox1 (First Column of the hbox1)
        vbox1.setAlignment(Qt.AlignTop)
        vbox1.setSpacing(5)
        
    #----------------------SECOND COLUMN--------------------
        #Second column elements of vbox1 for the hbox1:
        self.box2 = Box("SC23", vbox2)
        
        self.field2_1 = InfoField(name = "RW23 Pause Soll [min] ln", 
                            layout = vbox2)
        self.field2_2 = InfoField(name = "RW23 Run Soll [min] ln", 
                            layout = vbox2)
        self.field2_3 = InfoField(name = "RW23 Auto Sollwert [%]", 
                            layout = vbox2)
        self.field2_4 = InfoField(name = "RW23 Hand Soll [min] ln", 
                            layout = vbox2)

        #Settings for the vbox2 (First Column of the hbox1)
        vbox2.setAlignment(Qt.AlignTop)
        vbox2.setSpacing(5)

    #----------------------THRD COLUMN--------------------
        #Third column elements of vbox3 for the hbox1:
        self.box3 = Box("SC21", vbox3)

        #Settings for the vbox3 (Third Column of the hbox1)
        vbox3.setAlignment(Qt.AlignTop)
        vbox3.setSpacing(5)

        #Settings for the hbox1:
        hbox1.setAlignment(Qt.AlignTop)
        hbox1.setSpacing(10)
        hbox1.addLayout(vbox1, 1)
        hbox1.addLayout(vbox2, 1)
        hbox1.addLayout(vbox3, 1)
        hbox1.addLayout(vbox3_3_1, 2) # vbox3_3_1 is used here


        #hbox2
        #----------------------FIRST COLUMN--------------------
        #First column elements of vbox4 for the hbox2:
        self.box4 = Box("HE22", vbox4)
        
        self.field3_1 = InfoField(name = "Nachgärer Temp.-Sollwert [\N{DEGREE SIGN}C]", 
                            layout = vbox4)
        self.field3_2 = InfoField(name = "Temp. Vorlauf Ng 2 [\N{DEGREE SIGN}C]", 
                            layout = vbox4)
        self.field3_3 = InfoField(name = "Temp. Ng 2 [\N{DEGREE SIGN}C]", 
                            layout = vbox4)     

        #Settings for the vbox4 (First Column of the hbox2)
        vbox4.setAlignment(Qt.AlignTop)
        vbox4.setSpacing(5)                                            
        
        #----------------------SECOND COLUMN--------------------
        #Second column elements of vbox5 for the hbox2:
        self.box5 = Box("RW24", vbox5)

        self.field4_1 = InfoField(name = "RW24 Pause Soll [min] ln", 
                            layout = vbox5)
        self.field4_2 = InfoField(name = "RW24 Run Soll [min] ln", 
                            layout = vbox5)
        self.field4_3 = InfoField(name = "RW24 Auto Sollwert [%]", 
                            layout = vbox5)
        self.field4_4 = InfoField(name = "RW24 Hand Soll [min] ln", 
                            layout = vbox5)                                                
    
        #Settings for the vbox5 (First Column of the hbox2)
        vbox5.setAlignment(Qt.AlignTop)
        vbox5.setSpacing(5)                    

        #Settings for the hbox2:
        hbox2.setAlignment(Qt.AlignTop)
        hbox2.setSpacing(10)
        hbox2.setContentsMargins(0, 20, 0, 0)

        #Add columns(vbox4, vbox5 vbox3_3_2(dummy)) to the hbox2
        hbox2.addLayout(vbox4,1)
        hbox2.addLayout(vbox5,1)
        hbox2.addLayout(vbox3_3_2, 2) # vbox3_3_2 is used here



        #Adding two horizontal layouts (hbox1, hbox2) to the layout of the page
        vbox.addLayout(hbox1, 50)
        vbox.addLayout(hbox2, 50)

        #Assigning page layout to the window
        window.tab4.setLayout(vbox)
        

    def updateAll(self,inputs: dict):
        """method to update all objects in current tab periodically after reading the values in different thread

        :param inputs: tag values
        :type inputs: dict
        """
        objectList=[self.box1,
                    self.field1_1,
                    self.field1_2,
                    self.field1_3,
                    self.field1_4,
                    self.field1_5,

                    self.box2,
                    self.field2_1,
                    self.field2_2,
                    self.field2_3,
                    self.field2_4,

                    self.box3,

                    self.box4,
                    self.field3_1,
                    self.field3_2,
                    self.field3_3,

                    self.box5,
                    self.field4_1,
                    self.field4_2,
                    self.field4_3,
                    self.field4_4, ]


        for o in objectList:
            #iterate over an update method that should be added to all faceplate objects similar to box object
            o.update(inputs)
        

if __name__=='__main__':
    pass