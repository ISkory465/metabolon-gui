from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from ..faceplates import Box
from ..test_element import InfoField



def UI(self):
    
    #Main layout of the first tab 'Steuerung_Strasse_2"
    vbox=QVBoxLayout()
    
    #Page has 2 horizontal boxes:
    hbox1=QHBoxLayout()
    hbox2=QHBoxLayout()

    #First horizontal hbox1 contains Three vertical layouts
    vbox1=QVBoxLayout()
    vbox2=QVBoxLayout()
    vbox3=QVBoxLayout()
    vbox3_3=QVBoxLayout() #Empty buffer to shift layout

    #Second horizontal hbox2 contains Two vertical layouts
    vbox4=QVBoxLayout()
    vbox5=QVBoxLayout()    




    #hbox1
    #----------------------FIRST COLUMN--------------------
    #First column elements of vbox1 for the hbox1:
    faceplate1 = Box("HE21")
    vbox1.addWidget(faceplate1)
    faceplate1.setFixedHeight(120)
    faceplate1.setFixedWidth(190)

    field1_1 = InfoField(name = "Fermenter Temp.-Sollwert (\N{DEGREE SIGN}C)",
                         layout = vbox1)
    field1_2 = InfoField(name = "D8400.HZG_REG.SZ_HE21",
                         layout = vbox1)
    field1_3 = InfoField(name = "Temp. Vorlauf Fer 2 (\N{DEGREE SIGN}C)",
                         layout = vbox1)
    field1_4 = InfoField(name = "Temp. Fer 2 (\N{DEGREE SIGN}C)",
                         layout = vbox1)
    field1_5 = InfoField(name = "Temp. Fer 2 (\N{DEGREE SIGN}C)",
                         layout = vbox1)

    #Settings for the vbox1 (First Column of the hbox1)
    vbox1.setAlignment(Qt.AlignTop)
    vbox1.setSpacing(5)
     
#----------------------SECOND COLUMN--------------------
    #Second column elements of vbox1 for the hbox1:
    faceplate2 = Box("SC23")
    faceplate2.setFixedHeight(120)
    faceplate2.setFixedWidth(190)
    vbox2.addWidget(faceplate2)

    field2_1 = InfoField(name = "RW23 Pause Soll [min] ln", 
                         layout = vbox2)
    field2_2 = InfoField(name = "RW23 Run Soll [min] ln", 
                         layout = vbox2)
    field2_3 = InfoField(name = "RW23 Auto Sollwert [%]", 
                         layout = vbox2)
    field2_4 = InfoField(name = "RW23 Hand Soll [min] ln", 
                         layout = vbox2)

    #Settings for the vbox2 (First Column of the hbox1)
    vbox2.setAlignment(Qt.AlignTop)
    vbox2.setSpacing(5)

#----------------------THRD COLUMN--------------------
    #Third column elements of vbox3 for the hbox1:
    faceplate3 = Box("SC21")
    faceplate3.setFixedHeight(120)
    faceplate3.setFixedWidth(190)
    vbox3.addWidget(faceplate3)

    #Settings for the vbox3 (Third Column of the hbox1)
    vbox3.setAlignment(Qt.AlignTop)
    vbox3.setSpacing(5)

    #Settings for the hbox1:
    hbox1.setAlignment(Qt.AlignTop)
    hbox1.setSpacing(10)
    hbox1.addLayout(vbox1, 1)
    hbox1.addLayout(vbox2, 1)
    hbox1.addLayout(vbox3, 1)
    hbox1.addLayout(vbox3_3, 2)




    #hbox2
    #----------------------FIRST COLUMN--------------------
    #First column elements of vbox4 for the hbox2:
    faceplate4 = Box("HE22")
    faceplate4.setFixedHeight(120)
    faceplate4.setFixedWidth(190)
    vbox4.addWidget(faceplate4)
    
    field3_1 = InfoField(name = "Nachgärer Temp.-Sollwert [\N{DEGREE SIGN}C]", 
                         layout = vbox4)
    field3_2 = InfoField(name = "Temp. Vorlauf Ng 2 [\N{DEGREE SIGN}C]", 
                         layout = vbox4)
    field3_3 = InfoField(name = "Temp. Ng 2 [\N{DEGREE SIGN}C]", 
                         layout = vbox4)     

    #Settings for the vbox4 (First Column of the hbox2)
    vbox4.setAlignment(Qt.AlignTop)
    vbox4.setSpacing(5)                                            
    
    #----------------------SECOND COLUMN--------------------
    #Second column elements of vbox5 for the hbox2:
    faceplate5 = Box("RW24")
    faceplate5.setFixedHeight(120)
    faceplate5.setFixedWidth(190)
    vbox5.addWidget(faceplate5)

    field4_1 = InfoField(name = "RW24 Pause Soll [min] ln", 
                         layout = vbox5)
    field4_2 = InfoField(name = "RW24 Run Soll [min] ln", 
                         layout = vbox5)
    field4_3 = InfoField(name = "RW24 Auto Sollwert [%]", 
                         layout = vbox5)
    field4_4 = InfoField(name = "RW24 Hand Soll [min] ln", 
                         layout = vbox5)                                                
  
    #Settings for the vbox5 (First Column of the hbox2)
    vbox5.setAlignment(Qt.AlignTop)
    vbox5.setSpacing(5)                    

    #Settings for the hbox2:
    hbox2.setAlignment(Qt.AlignTop)
    hbox2.setSpacing(10)
    hbox2.setContentsMargins(0, 20, 0, 0)

    #Add columns(vbox4, vbox5 vbox3_3(dummy)) to the hbox2
    hbox2.addLayout(vbox4,1)
    hbox2.addLayout(vbox5,1)
    hbox2.addLayout(vbox3_3, 2)





    #Adding two horizontal layouts (hbox1, hbox2) to the layout of the page
    vbox.addLayout(hbox1, 50)
    vbox.addLayout(hbox2, 50)

    #Assigning page layout to the tab
    self.tab4.setLayout(vbox)
    


if __name__=='__main__':
    UI()