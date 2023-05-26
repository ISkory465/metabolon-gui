from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from ..facelpates_new import InfoField, ToggleButton, Futter1, Feststoffbtn


class Page():

  def UI(self,window:QMainWindow):
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
      self.futter1 = Futter1(buttonName="DB60.FES2.VW.FES", sollwert11='Feststoff Sollwert [kg/d]',solwert12='Feststoff Istwert [kg/d]', solwert21='Feststoff Sollwert [kg/Zyklus]',solwert22='Feststoff Istwert [kg/Zyklus]', layout=self.vbox1)
      self.futter2 = Futter1(buttonName="DB60.FLU2.VW.FLU", sollwert11='Feststoff Sollwert [l/d]', solwert12='Feststoff Istwert [l/d]',  solwert21='Feststoff Sollwert [l/Zyklus]', solwert22='Feststoff Istwert [l/Zyklus]', layout=self.vbox1)
      self.futter3 = Futter1(buttonName="DB60.MAI2.VW.MAI", sollwert11='Maische Sollwert [l/d]',   solwert12='Maische Istwert [l/d]',    solwert21='Maische Sollwert [l/Zyklus]',   solwert22='Maische Istwert [l/Zyklus]', layout=self.vbox1)
      self.futterungszyKlein = InfoField(name ='Futterungszyklein/Tag', layout = self.vbox2)
      self.b50Flusw = InfoField(name ='DB50.MAIFLU2.FLUSW', layout = self.vbox3)
      self.db50Fluw = InfoField(name ='DB50.MAIFLU2.FLUW', layout =self.vbox3)

      #----------------------Second Part of the Tab--------------------
      self.feststoff1 = Feststoffbtn(firstElement="Gesamteintrag Feststoff 1 [kg]", 
                                     secondElement="Gesamteintrag Feststoff 2 [kg]", 
                                     thirdElement="Gesamteintrag Feststoff 3 [kg]",
                                     fourthElement="Gesamteintrag Feststoff 4 [kg]", 
                                     fifthElement="Gesamteintrag Feststoff 5 [kg]",
                                     sixthElement="Gesamteintrag Feststoff 6 [kg]",
                                       layout=self.vbox4)
      self.feststoff1Nobtn = InfoField(name ='Gesamteintrag Feststoff 7 [kg]', layout = self.vbox4)

      self.feststoff2 = Feststoffbtn(firstElement="Gesamteintrag Fluessigkeit 1 [l]", 
                                     secondElement="Gesamteintrag Fluessigkeit 2 [l]", 
                                     thirdElement="Gesamteintrag Fluessigkeit 3 [l]",
                                     fourthElement="Gesamteintrag Fluessigkeit 4 [l]", 
                                     fifthElement="Gesamteintrag Fluessigkeit 5 [l]",
                                     sixthElement="Gesamteintrag Fluessigkeit 6 [l]",
                                       layout=self.vbox5)
      self.feststoff3 = Feststoffbtn(firstElement="Gesamteintrag Maische 1 [l]", 
                                     secondElement="Gesamteintrag Maische 2 [l]", 
                                     thirdElement="Gesamteintrag Maische 3 [l]",
                                     fourthElement="Gesamteintrag Maische 4 [l]", 
                                     fifthElement="Gesamteintrag Maische 5 [l]",
                                     sixthElement="Gesamteintrag Maische 6 [l]",
                                       layout=self.vbox6)
      self.feststoff2Nobtn = InfoField(name ='Gesamteintrag Maische 7 [l]', layout = self.vbox6)
      self.feststoff3Nobtn = InfoField(name ='Feststoff Gesamteintrag [kg]', layout = self.vbox7)
      self.feststoff4Nobtn = InfoField(name ='Fluessigkeit Gesamteintrag [l]', layout = self.vbox7)
      self.feststoff5Nobtn = InfoField(name ='Maische Gesamteintrag [l]', layout = self.vbox7)
      #----------------------Layout Settings---------------------------
      #settings for the vbox1:
      self.vbox1.setAlignment(Qt.AlignTop)
      self.vbox1.setSpacing(10)   
      self.vbox1.setContentsMargins(0, 0, 0, 0)
      #settings for the vbox2:
      self.vbox2.setAlignment(Qt.AlignTop)
      self.vbox2.setSpacing(10)   
      self.vbox2.setContentsMargins(0, 0, 0, 0)
      #settings for the vbox3:
      self.vbox3.setAlignment(Qt.AlignTop)
      self.vbox3.setSpacing(10)  
      self.vbox3.setContentsMargins(0, 0, 0, 0)
      
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
      self.vbox7.setSpacing(10)   
      self.vbox7.setContentsMargins(0, 0, 0, 0)

      #Settings for the hbox1:
      self.hbox1.setAlignment(Qt.AlignTop)
      self.hbox1.setSpacing(10)
      self.hbox1.setContentsMargins(0, 0, 0, 0)
      self.hbox1.addLayout(self.vbox1, 1)
      self.hbox1.addLayout(self.vbox2, 1) 
      self.hbox1.addLayout(self.vbox3, 1) 
      
      #Settings for the hbox2:
      self.hbox2.setAlignment(Qt.AlignTop)
      self.hbox2.setSpacing(10)
      self.hbox2.setContentsMargins(0, 20, 20, 0)
      self.hbox2.addLayout(self.vbox4, 1)
      self.hbox2.addLayout(self.vbox5, 1)
      self.hbox2.addLayout(self.vbox6, 1)
      self.hbox2.addLayout(self.vbox7, 1)

      #Adding two horizontal layouts (hbox1, hbox2) to the layout of the page
      self.vbox.addLayout(self.hbox1, 50)
      self.vbox.addLayout(self.hbox2, 50)

      #Assigning to the tab
      window.tab9.setLayout(self.vbox)

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