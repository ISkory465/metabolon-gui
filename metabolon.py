import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

#app tabs import:
from components.app_tabs.Strasse_1                import Page as Strasse_1
from components.app_tabs.Steuerung_Strasse_1      import Page as St_Strasse_1
from components.app_tabs.Steuerung_Strasse_2      import Page as St_Strasse_2
from components.app_tabs.Fuetterung_Strasse_1     import Page as Fuet_Strasse_1
from components.app_tabs.Stoermeldungen_Strasse_1 import Page as St_Meld_1
from components.app_tabs.Stoermeldungen_Strasse_2 import Page as St_Meld_2
from components.app_tabs.Betriebsstunden          import Page as Betriebsstunden
from components.app_tabs.Fuetterung_Strasse_2     import Page as Fuet_Strasse_2
from components.app_tabs.Side_bar                 import SideBar




class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Metabolon Station")
        self.setGeometry(350,100,1200,800)
        self.Tabs_UI()

    def Tabs_UI(self):

        # Side Bar
        self.side_bar = SideBar()

        self.tabs = QTabWidget()

        # First Tab
        self.tab1 = QWidget()
        self.tabs.addTab(self.tab1,"Strasse 1")
        self.page1 = Strasse_1()
        self.page1.UI(self)
        
        #Second Tab
        self.tab2 = QWidget()
        # self.tabs.addTab(self.tab2,"Strasse 2")
        # self.page2 = Strasse_2()
        # self.page2.UI(self)
        
        #Third Tab
        self.tab3 = QWidget()
        self.tabs.addTab(self.tab3,"Steuerung Strasse 1")
        self.page3 = St_Strasse_1()
        self.page3.UI(self)
        
        #Fourth Tab
        self.tab4 = QWidget()
        self.tabs.addTab(self.tab4,"Steuerung Strasse 2")
        self.page4 = St_Strasse_2()
        self.page4.UI(self)

        #Fifth Tab
        self.tab5 = QWidget()
        self.tabs.addTab(self.tab5,"Fütterung Straße 1")
        self.page5 = Fuet_Strasse_1()
        self.page5.UI(self)

        #Sixth Tab
        self.tab6 = QWidget()
        self.tabs.addTab(self.tab6,"Störmeldungen Straße 1")
        self.page6 = St_Meld_1()
        self.page6.UI(self)

        #Seventh Tab
        self.tab7 = QWidget()
        self.tabs.addTab(self.tab7,"Störmeldungen Straße 2")
        self.page7 = St_Meld_2()
        self.page7.UI(self)

        #Eighth Tab
        self.tab8 = QWidget()
        self.tabs.addTab(self.tab8,"Betriebsstunden")
        self.page8 = Betriebsstunden()
        self.page8.UI(self)
        
        #Ninth Tab
        self.tab9 = QWidget()
        self.tabs.addTab(self.tab9,"Fütterung Straße 2")
        self.page9 = Fuet_Strasse_2()
        self.page9.UI(self)
        
        # Create a central widget to hold the mainLayout
        central_widget = QWidget()
        central_layout = QHBoxLayout()
        central_layout.addWidget(self.tabs)
        central_layout.addWidget(self.side_bar)
        central_widget.setLayout(central_layout)

        # Set the central widget for the main window
        self.setCentralWidget(central_widget)

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
