from PyQt5.QtWidgets import *
from faceplates import Box
from test_element import Mixer


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


    #----------------------FIRST COLUMN--------------------
    #First column elements of vbox1 for the hbox1:
    faceplate1 = Box("HE21")
    vbox1.addWidget(faceplate1)

    label1 = QLabel("\nFermenter Temp.-Sollwert (\N{DEGREE SIGN}C)")
    vbox1.addWidget(label1)

    #Fermenter Temperature value
    temp1 = QSpinBox(self) #uses integers; for floats use QDoubleSpinBox

    #Check range of values in LabView
    temp1.setMinimum(10)
    temp1.setMaximum(100)

    temp1.setButtonSymbols(2)
    temp1.setMaximumSize(35, 20)

    vbox1.addWidget(temp1)


    #<------------------------------->
    label2 = QLabel("\nD8400.HZG_REG.SZ_HE21")
    vbox1.addWidget(label2)

    # #Fermenter Temperature value
    val1 = QSpinBox(self) #uses integers; for floats use QDoubleSpinBox

    # #Check range of values in LabView
    val1.setMinimum(10)
    val1.setMaximum(100)

    val1.setButtonSymbols(2)
    val1.setMaximumSize(35, 20)

    vbox1.addWidget(val1)


   #<------------------------------->
    label3 = QLabel("\nTemp. Vorlauf Fer 2 (\N{DEGREE SIGN}C)")
    vbox1.addWidget(label3)

    #Temperature value2
    temp2 = QSpinBox(self) #uses integers; for floats use QDoubleSpinBox

    #Check range of values in LabView
    temp2.setMinimum(10)
    temp2.setMaximum(100)

    temp2.setButtonSymbols(2)
    temp2.setMaximumSize(35, 20)

    vbox1.addWidget(temp2)

    #<------------------------------->
    label4 = QLabel("\nTemp. Fer 2 (\N{DEGREE SIGN}C)")
    vbox1.addWidget(label4)

    #Temperature value3
    temp3 = QSpinBox(self) #uses integers; for floats use QDoubleSpinBox

    #Check range of values in LabView
    temp3.setMinimum(20)
    temp3.setMaximum(100)
    temp3.setValue(25)
    
    temp3.setButtonSymbols(2)
    temp3.setMaximumSize(35, 20)

    vbox1.addWidget(temp3)  


    #<------------------------------->
    
    label5 = QLabel("\nTemp. Fer 2 (\N{DEGREE SIGN}C)")
    vbox1.addWidget(label5)

    #RW23 Paause Soll
    val2 = QSpinBox(self) #uses integers; for floats use QDoubleSpinBox

    #Check range of values in LabView
    val2.setMinimum(10)
    val2.setMaximum(10)
    
    val2.setButtonSymbols(2)
    val2.setMaximumSize(35, 20)

    vbox1.addWidget(val2) 

#----------------------SECOND COLUMN--------------------

    #Second column elements of vbox1 for the hbox1:
    faceplate2 = Box("rw23")
    vbox2.addWidget(faceplate2)

    label6 = QLabel("\nFermenter Temp.-Sollwert (\N{DEGREE SIGN}C)")
    vbox2.addWidget(label6)

    #Fermenter Temperature value
    temp4 = QSpinBox(self) #uses integers; for floats use QDoubleSpinBox

    #Check range of values in LabView
    temp4.setMinimum(10)
    temp4.setMaximum(100)

    temp4.setButtonSymbols(2)
    temp4.setMaximumSize(35, 20)

    vbox2.addWidget(temp4)


#----------------------THRD COLUMN--------------------

    #Third column elements of vbox1 for the hbox1:
    faceplate3 = Box("rw23")
    vbox3.addWidget(faceplate3)

    label7 = QLabel("\nFermenter Temp.-Sollwert (\N{DEGREE SIGN}C)")
    vbox3.addWidget(label7)



    hbox1.addLayout(vbox1, 20)
    hbox1.addLayout(vbox2, 20)
    hbox1.addLayout(vbox3, 10)
    hbox1.addLayout(vbox3_3,40)


    hbox2.addLayout(vbox4,30)
    hbox2.addLayout(vbox5,30)


    vbox.addLayout(hbox1, 50)
    vbox.addLayout(hbox2, 50)
    self.tab4.setLayout(vbox)
    #-----------------------------------------
    #-----------------------------------------
    #-----------------------------------------
    #-----------------------------------------



    # #SC21 Radio
    # label3 = QLabel("SC21")
    # layout.addWidget(label3, 0, 2)
    
    # radio_b7 = QRadioButton("Hand")
    # radio_b8 = QRadioButton("Aus")
    # radio_b8.setChecked(True)
    # radio_b9 = QRadioButton("Auto")
    
    # layout.addWidget(radio_b7, 1, 2)
    # layout.addWidget(radio_b8, 2, 2)
    # layout.addWidget(radio_b9, 3, 2)

    # #Set all widgets in the Tab_Steuerung_Strasse2 to the tab 4
    # self.tab4.setLayout(layout)




if __name__=='__main__':
    UI()