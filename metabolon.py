import sys
from PyQt5.QtWidgets import *

#app tabs import:
import components.app_tabs.Strasse_1 as Strasse1
import components.app_tabs.Steuerung_Strasse_2 as St_Strasse_2
import components.app_tabs.Fuetterung_Strasse_1 as Fuet_Strasse_1
import components.app_tabs.Stoermeldungen_Strasse_2 as St_meld_Strasse_2
import components.app_tabs.Betriebsstunden as Betriebsstunden


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Metabolon Station")
        self.setGeometry(350,150,900,600)
        self.Tabs_UI()

    def Tabs_UI(self):
        mainLayout = QVBoxLayout()
        self.tabs = QTabWidget()

        #first Tab
        self.tab1 = QWidget()
        self.tabs.addTab(self.tab1,"Strasse 1")
        Strasse1.UI(self)

        #Second Tab
        self.tab2 = QWidget()
        # self.tabs.addTab(self.tab2,"Strasse 2")
        # self.Tab_Strasse2()

        #Third Tab
        self.tab3 = QWidget()
        # self.tabs.addTab(self.tab3,"Steuerung Strasse 1")
        # self.Tab_Steuerung_Strasse1()

        #Fourth Tab
        self.tab4 = QWidget()
        self.tabs.addTab(self.tab4,"Steuµerung Strasse 2")
        St_Strasse_2.UI(self)

        #Fifth Tab
        self.tab5 = QWidget()
        self.tabs.addTab(self.tab5,"Fütterung Straße 1")
        Fuet_Strasse_1.UI(self)

        #Sixth Tab
        self.tab6 = QWidget()
        self.tabs.addTab(self.tab6,"Störmeldungen Straße 2")
        St_meld_Strasse_2.UI(self)

        #Seventh Tab
        self.tab7 = QWidget()
        self.tabs.addTab(self.tab7,"Betriebsstunden")
        Betriebsstunden.UI(self)
                        
                
        mainLayout.addWidget(self.tabs)
        self.setLayout(mainLayout)




def main():
    App=QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(App.exec_())

if __name__=='__main__':
    main()