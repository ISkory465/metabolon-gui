from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from ..test_element import InfoField, ToggleButton, Futter1


class Page():

  def UI(self,window:QMainWindow):
      #Main layout of the tab 'Fuettrung_Strasse_1"
      vbox=QVBoxLayout()
      
      #Page has 2 horizontal boxes:
      hbox1=QHBoxLayout()
      hbox2=QHBoxLayout()

      #First horizontal hbox1 contains Three vertical layouts
      vbox1=QVBoxLayout()
      vbox2=QVBoxLayout()
      vbox3=QVBoxLayout()

      #Second horizontal hbox2 contains Two vertical layouts
      vbox4=QVBoxLayout()
      vbox5=QVBoxLayout()    
      vbox6=QVBoxLayout()
      
    #hbox1
      #----------------------FIRST Part of the Tab--------------------
      #Elements of vbox1 for the hbox1:
      futter1 = Futter1(buttonName="DB60.FES2.VW.FES", sollwert11='Feststoff Sollwert [kg/d]',solwert12='Feststoff Istwert [kg/d]', solwert21='Feststoff Sollwert [kg/Zyklus]',solwert22='Feststoff Istwert [kg/Zyklus]', layout=vbox1)
      futter2 = Futter1(buttonName="DB60.FES2.VW.FES", sollwert11='Feststoff Sollwert [l/d]', solwert12='Feststoff Istwert [l/d]',  solwert21='Feststoff Sollwert [l/Zyklus]', solwert22='Feststoff Istwert [l/Zyklus]', layout=vbox1)
      futter3 = Futter1(buttonName="DB60.FES2.VW.FES", sollwert11='Maische Sollwert [l/d]',   solwert12='Maische Istwert [l/d]',    solwert21='Maische Sollwert [l/Zyklus]',   solwert22='Maische Istwert [l/Zyklus]', layout=vbox1)
      futterungszyKlein = InfoField(name ='Futterungszyklein/Tag', layout = vbox2)
      db50Flusw = InfoField(name ='DB50.MAILFLU1.FLUSW', layout = vbox3)
      db50Fluw = InfoField(name ='DB50.MAILFLU1.FLUW', layout = vbox3)

      #----------------------Second Part of the Tab--------------------
      

      #----------------------Layout Settings---------------------------
      #settings for the vbox1:
      vbox1.setAlignment(Qt.AlignTop)
      vbox1.setSpacing(10)   
      vbox1.setContentsMargins(0, 0, 0, 0)
      #settings for the vbox2:
      vbox2.setAlignment(Qt.AlignTop)
      vbox2.setSpacing(10)   
      vbox2.setContentsMargins(0, 0, 0, 0)
      #settings for the vbox3:
      vbox3.setAlignment(Qt.AlignTop)
      vbox3.setSpacing(10)  
      vbox3.setContentsMargins(0, 0, 0, 0)

      #Settings for the hbox1:
      hbox1.setAlignment(Qt.AlignTop)
      hbox1.setSpacing(10)
      hbox1.setContentsMargins(0, 0, 0, 0)
      hbox1.addLayout(vbox1, 1)
      hbox1.addLayout(vbox2, 1) 
      hbox1.addLayout(vbox3, 1) 
      

      #Adding two horizontal layouts (hbox1, hbox2) to the layout of the page
      vbox.addLayout(hbox1, 50)
      vbox.addLayout(hbox2, 50)

      #Assigning to the tab
      window.tab5.setLayout(vbox)


if __name__=='__main__':
    pass