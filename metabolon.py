import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

#app tabs import:
from components.app_tabs.Strasse_1                import Page as Strasse_1
from components.app_tabs.Strasse_2                import Page as Strasse_2
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
        self.setGeometry(350,100,1200,600)
        self.Tabs_UI()

        # Center the window on the screen.
        self.center_on_screen()


    def center_on_screen(self):

        # get the rectangle specifying the geometry of the main window
        qr = self.frameGeometry()

        # figure out the screen resolution
        cp = QDesktopWidget().availableGeometry().center()

        # move rectangle's center point into the center of the screen
        qr.moveCenter(cp)

        # top left of rectangle becomes top left of window centering it
        self.move(qr.topLeft())


    def Tabs_UI(self):

        # Side Bar
        self.side_bar = SideBar()

        # main parent tab widget
        self.tabs = QTabWidget()

        # self.tabs contains three tabs: 
        self.innerTabs1 = QTabWidget()
        self.innerTabs2 = QTabWidget()
        self.innerTabs3 = QTabWidget()

        # Add the inner QTabWidgets to the outer QTabWidget
        self.tabs.addTab(self.innerTabs1, "Straße 1")
        self.tabs.addTab(self.innerTabs2, "Straße 2")
        self.tabs.addTab(self.innerTabs3, "Statistik")

        # Hide the tab bar of the outer QTabWidget so only the inner tab bars are visible
        self.tabs.tabBar().setVisible(True)


        # <--self.innerTabs1-->
        #Page instances for the import to the self.innerTabs1
        self.strasse_1 = Strasse_1()
        self.steu_strasse_1 = St_Strasse_1()
        self.fuet_strasse_1 = Fuet_Strasse_1()
        self.steu_meld_starsse_1 = St_Meld_1()

        # Tabs connection to the self.innerTabs1:
        self.innerTabs1.addTab(self.strasse_1,              "Übersicht")       #old name: "Strasse 1"
        self.innerTabs1.addTab(self.steu_strasse_1,         "Steuerung")       #old name: "Steuerung Strasse 1"
        self.innerTabs1.addTab(self.fuet_strasse_1,         "Fütterung")       #old name: "Fütterung Straße 1"
        self.innerTabs1.addTab(self.steu_meld_starsse_1,    "Störmeldungen")   #old name: "Störmeldungen Straße 1"


        # <--self.innerTabs2-->
        #Page instances for the import to the self.innerTabs2
        self.strasse_2 = Strasse_2()
        self.steu_strasse_2 = St_Strasse_2()
        self.fuet_strasse_2 = Fuet_Strasse_2()
        self.steu_meld_starsse_2 = St_Meld_2()

        # Tabs connection to the self.innerTabs2:      
        self.innerTabs2.addTab(self.strasse_2,              "Übersicht")        #old name: "Strasse 2"
        self.innerTabs2.addTab(self.steu_strasse_2,         "Steuerung")        #old name: "Steuerung Strasse 2"
        self.innerTabs2.addTab(self.fuet_strasse_2,         "Fütterung")        #old name: "Fütterung Straße 2"
        self.innerTabs2.addTab(self.steu_meld_starsse_2,    "Störmeldungen")    #old name: "Störmeldungen Straße 2"


        # <--self.innerTabs3-->
        #Page instances for the import to the self.innerTabs3
        self.betrieb = Betriebsstunden()

        # Tab connection to the self.innerTabs3:
        self.innerTabs3.addTab(self.betrieb, "Betriebsstunden")


        # Create a central widget to hold the mainLayout
        central_widget = QWidget()
        central_layout = QHBoxLayout()
        central_layout.addWidget(self.tabs, 1) # 1 stretch factor
        central_layout.addWidget(self.side_bar, 0) # 0 stretch factor
        central_widget.setLayout(central_layout)

        # Set the central widget for the main window
        self.setCentralWidget(central_widget)

        # Display the content of the central_widget
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    # app.setStyle('Fusion')
    window = Window()
    sys.exit(app.exec_())


#TODO Swap all german umlauts in the strings to a simplified form