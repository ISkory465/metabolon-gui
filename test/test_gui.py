import sys
from PyQt5.QtWidgets import *
import app_tabs.Strasse_1 as Strasse1


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Metabolon Station")
        self.setGeometry(350,150,900,600)
        # self.UI()
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
        self.tabs.addTab(self.tab4,"Steuerung Strasse 2")
        # valera.Tab_Steuerung_Strasse2(self)
                
        mainLayout.addWidget(self.tabs)
        self.setLayout(mainLayout)

    µ


def main():
    App=QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(App.exec_())

if __name__=='__main__':
    main()