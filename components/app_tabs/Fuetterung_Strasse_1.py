from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from ..faceplates.futter import *
from ..widgets.infofield_dbl import InfoField

#TODO: Correct design of buttons, correct some aspects of layout

class Page(QWidget):

    def __init__(self) -> None:

        super().__init__()
        self.UI()


    def UI(self):
        
        #Main layout of the tab 'Fuettrung_Strasse_1"
        self.vbox=QVBoxLayout()
        
        #Page has 2 horizontal boxes:
        self.hbox1=QHBoxLayout()
        self.hbox2=QHBoxLayout()

        #First horizontal hbox1 contains Three vertical layouts
        self.vbox1=QVBoxLayout()
        self.vbox2=QVBoxLayout()
        self.vbox3=QVBoxLayout()

        #Second horizontal hbox2 contains Two vertical layouts
        self.vbox4=QVBoxLayout()
        self.vbox5=QVBoxLayout()    
        self.vbox6=QVBoxLayout()
        self.vbox7=QVBoxLayout()
        
      #hbox1
        #----------------------FIRST Part of the Tab--------------------
        #Elements of vbox1 for the hbox1:
        self.futter1 = Futter1(buttonName="DB50.FES1.VW.FES", sollwert11='Feststoff Sollwert [kg/d]',solwert12='Feststoff Istwert [kg/d]', solwert21='Feststoff Sollwert [kg/Zyklus]',solwert22='Feststoff Istwert [kg/Zyklus]')
        self.vbox1.addWidget(self.futter1)
        self.futter2 = Futter1(buttonName="DB50.FLU1.VW.FLU", sollwert11='Feststoff Sollwert [l/d]', solwert12='Feststoff Istwert [l/d]',  solwert21='Feststoff Sollwert [l/Zyklus]', solwert22='Feststoff Istwert [l/Zyklus]')
        self.vbox1.addWidget(self.futter2)
        self.futter3 = Futter1(buttonName="DB50.MAI.VW.MAI", sollwert11='Maische Sollwert [l/d]',   solwert12='Maische Istwert [l/d]',    solwert21='Maische Sollwert [l/Zyklus]',   solwert22='Maische Istwert [l/Zyklus]')
        self.vbox1.addWidget(self.futter3)
        
        self.futterungszyKlein = InfoField(name ='Futterungszyklein/Tag')
        self.vbox2.addWidget(self.futterungszyKlein)
        self.b50Flusw = InfoField(name ='DB50.MAIFLU1.FLUSW')
        self.vbox3.addWidget(self.b50Flusw)
        self.db50Fluw = InfoField(name ='DB50.MAIFLU1.FLUW')
        self.vbox3.addWidget(self.db50Fluw)

        #----------------------Second Part of the Tab--------------------
        self.feststoff1 = Feststoffbtn(firstElement="Gesamteintrag Feststoff 1 [kg]", 
                                      secondElement="Gesamteintrag Feststoff 2 [kg]", 
                                      thirdElement="Gesamteintrag Feststoff 3 [kg]",
                                      fourthElement="Gesamteintrag Feststoff 4 [kg]", 
                                      fifthElement="Gesamteintrag Feststoff 5 [kg]",
                                      sixthElement="Gesamteintrag Feststoff 6 [kg]",
                                      )
        self.vbox4.addWidget(self.feststoff1)
        self.feststoff1Nobtn = InfoField(name ='Gesamteintrag Feststoff 7 [kg]')
        self.vbox4.addWidget(self.feststoff1Nobtn)

        self.feststoff2 = Feststoffbtn(firstElement="Gesamteintrag Fluessigkeit 1 [l]", 
                                      secondElement="Gesamteintrag Fluessigkeit 2 [l]", 
                                      thirdElement="Gesamteintrag Fluessigkeit 3 [l]",
                                      fourthElement="Gesamteintrag Fluessigkeit 4 [l]", 
                                      fifthElement="Gesamteintrag Fluessigkeit 5 [l]",
                                      sixthElement="Gesamteintrag Fluessigkeit 6 [l]",
                                      )
        self.vbox5.addWidget(self.feststoff2)
        self.feststoff3 = Feststoffbtn(firstElement="Gesamteintrag Maische 1 [l]", 
                                      secondElement="Gesamteintrag Maische 2 [l]", 
                                      thirdElement="Gesamteintrag Maische 3 [l]",
                                      fourthElement="Gesamteintrag Maische 4 [l]", 
                                      fifthElement="Gesamteintrag Maische 5 [l]",
                                      sixthElement="Gesamteintrag Maische 6 [l]",
                                      )
        self.vbox6.addWidget(self.feststoff3)
        
        self.feststoff2Nobtn = InfoField(name ='Gesamteintrag Maische 7 [l]')
        self.feststoff3Nobtn = InfoField(name ='Feststoff Gesamteintrag [kg]')
        self.feststoff4Nobtn = InfoField(name ='Fluessigkeit Gesamteintrag [l]')
        self.feststoff5Nobtn = InfoField(name ='Maische Gesamteintrag [l]')

        self.vbox6.addWidget(self.feststoff2Nobtn)
        self.vbox7.addWidget(self.feststoff3Nobtn)
        self.vbox7.addWidget(self.feststoff4Nobtn)
        self.vbox7.addWidget(self.feststoff5Nobtn)


        #----------------------Layout Settings---------------------------
        #settings for the vbox1:
        self.vbox1.setAlignment(Qt.AlignTop)
        self.vbox1.setSpacing(0)   
        self.vbox1.setContentsMargins(0, 0, 0, 0)
        #settings for the vbox2:
        self.vbox2.setAlignment(Qt.AlignTop)
        self.vbox2.setSpacing(0)   
        self.vbox2.setContentsMargins(0, 10, 0, 0)
        #settings for the vbox3:
        self.vbox3.setAlignment(Qt.AlignTop)
        self.vbox3.setSpacing(0)  
        self.vbox3.setContentsMargins(0, 10, 0, 0)
        
        #settings for the vbox4:
        self.vbox4.setAlignment(Qt.AlignTop)
        self.vbox4.setSpacing(10)   
        self.vbox4.setContentsMargins(0, 0, 0, 0)
        #settings for the vbox5:
        self.vbox5.setAlignment(Qt.AlignTop)
        self.vbox5.setSpacing(10)   
        self.vbox5.setContentsMargins(0, 0, 0, 0)
        #settings for the vbox6:
        self.vbox6.setAlignment(Qt.AlignTop)
        self.vbox6.setSpacing(10)   
        self.vbox6.setContentsMargins(0, 0, 0, 0)
        #settings for the vbox7:
        self.vbox7.setAlignment(Qt.AlignTop)
        self.vbox7.setSpacing(5)   
        self.vbox7.setContentsMargins(0, 8, 0, 0)

        #Settings for the hbox1:
        self.hbox1.setAlignment(Qt.AlignTop)
        self.hbox1.setSpacing(10)
        self.hbox1.setContentsMargins(0, 0, 0, 0)
        self.hbox1.addLayout(self.vbox1, 1)
        self.hbox1.addLayout(self.vbox2, 1) 
        self.hbox1.addLayout(self.vbox3, 1) 
        
        #Settings for the hbox2:
        self.hbox2.setAlignment(Qt.AlignTop)
        self.hbox2.setSpacing(0)
        self.hbox2.setContentsMargins(0, 20, 0, 0)
        self.hbox2.addLayout(self.vbox4, 1)
        self.hbox2.addLayout(self.vbox5, 1)
        self.hbox2.addLayout(self.vbox6, 1)
        self.hbox2.addLayout(self.vbox7, 1)

        #Adding two horizontal layouts (hbox1, hbox2) to the layout of the page
        self.vbox.addLayout(self.hbox1, 50)
        self.vbox.addLayout(self.hbox2, 50)

        #Assigning to the tab
        self.setLayout(self.vbox)

    def updateAll(self,inputs: dict):
        """method to update all objects in current tab periodically after reading the values in different thread

        :param inputs: tag values
        :type inputs: dict
        """
        objectList=[self.futter1,
                    self.futter2,
                    self.futter3,
                    self.futterungszyKlein,
                    self.b50Flusw,
                    self.db50Fluw,
                    self.feststoff1,
                    self.feststoff1Nobtn,
                    self.feststoff2,
                    self.feststoff2Nobtn,
                    self.feststoff3,
                    self.feststoff3Nobtn,
                    self.feststoff4Nobtn,
                    self.feststoff5Nobtn]


        for o in objectList:
            #iterate over an update method that should be added to all faceplate objects similar to box object
            o.update(inputs)

if __name__=='__main__':
    pass