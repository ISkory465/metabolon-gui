import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import json
# Database Worker and Handler classes import
from database.WorkerLog import *
from database.Database_Handler import DatabaseHandler

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

from opc.OPC_Connection                           import Worker

with open('opc\opcList.JSON') as json_file:
  tags = json.load(json_file)

# Connectiong OpcList of sensors 
with open('database\opcSensorList.json') as json_sensors_file:
  sensor_dict= json.load(json_sensors_file)
class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Metabolon Station")
        self.setGeometry(350,100,1200,600)
        self.Tabs_UI()
        self.setup_database_update()
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
        # Update OPC list when outer tab index changes 
        self.tabs.currentChanged.connect(self.updateOPCList)

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
        
        # Update OPC list when inner tab index changes 
        global tags
        self.opclist=tags['Strasse1']
        self.innerTabs1.currentChanged.connect(self.updateOPCList)
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

        # Update OPC list when inner tab index changes 

        self.innerTabs2.currentChanged.connect(self.updateOPCList)
        # <--self.innerTabs3-->
        #Page instances for the import to the self.innerTabs3
        self.betrieb = Betriebsstunden()

        # Tab connection to the self.innerTabs3:
        self.innerTabs3.addTab(self.betrieb, "Betriebsstunden")
        
        # Update OPC list when inner tab index changes 

        self.innerTabs3.currentChanged.connect(self.updateOPCList)

        # Create a central widget to hold the mainLayout
        central_widget = QWidget()
        central_layout = QHBoxLayout()
        central_layout.addWidget(self.tabs, 1) # 1 stretch factor
        central_layout.addWidget(self.side_bar, 0) # 0 stretch factor
        central_widget.setLayout(central_layout)

        # Set the central widget for the main window
        self.setCentralWidget(central_widget)

        # Define the timer for periodic update of tags
        self.timer = QTimer()
        self.timer.setInterval(4000)
        self.timer.timeout.connect(self.runLongTask)
        self.timer.start() # Remove comment to run OPC update

        # Display the content of the central_widget
        self.show()
    
    def runSensorLog(self):
        #Create the Worker thread that runs periodically to update current list of OPC tags.""
        # Step 2: Create a QThread object
        global sensor_dict
        self.thread1 = QThread()
        #x=[1,2,3]
        # Step 3: Create a worker object
        #results=['Random.Int4','Random.Int8']
        self.workerLog = WorkerLog(sensor_dict)
        # Step 4: Move worker to the thread
        self.workerLog.moveToThread(self.thread1)

        # Step 5: Connect signals and slots
        
        self.thread1.started.connect(self.workerLog.run)
        self.workerLog.finished.connect(self.thread1.quit)
        self.workerLog.finished.connect(self.workerLog.deleteLater)
        self.thread1.finished.connect(self.thread1.deleteLater)
        
        # Step 6: Start the thread
        self.thread1.start() 
    
    def setup_database_update(self):
        # Instantiate the DatabaseHandler
        self.db_handler = DatabaseHandler()

        # Create a QTimer for periodic updates
        self.timer1 = QTimer(self)
        self.timer1.timeout.connect(self.runSensorLog)
        self.timer1.start(60000)  # 1 minute in milliseconds


    def runLongTask(self):
        #Create the Worker thread that runs periodically to update current list of OPC tags.""
        # Step 2: Create a QThread object
        self.thread = QThread()
        # Step 3: Create a worker object
        self.worker = Worker(self.opclist)
        # Step 4: Move worker to the thread
        self.worker.moveToThread(self.thread)

        # Step 5: Connect signals and slots        
        
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.worker.progress.connect(self.reportProgress)
        # Step 6: Start the thread
        self.thread.start() 

    def updateOPCList(self):
        """Change the list of OPC tags depending on the active tab

        """
        outer_index=self.tabs.currentIndex()
        inner_index1=self.innerTabs1.currentIndex()
        inner_index2=self.innerTabs2.currentIndex()
        inner_index3=self.innerTabs3.currentIndex()

        global tags
        #print(x)
        if outer_index == 0:
          if inner_index1==0:
            self.opclist=tags['Strasse1']#Change to actaul Tab
          elif inner_index1==1:
            self.opclist=tags['Steurung1']
          elif inner_index1==2:
            self.opclist=tags['Futter1']
          elif inner_index1==3:
            self.opclist=tags['Stoermeldungen_Strasse_1']

        elif outer_index==1:
          if inner_index2==0:
            self.opclist=tags['Strasse2']#Change to actaul Tab
          elif inner_index2==1:
            self.opclist=tags['Steurung2']
          elif inner_index2==2:
            self.opclist=tags['Futter2']
          elif inner_index2==3:
            self.opclist=tags['Stoermeldungen_Strasse_2']

        
        elif outer_index==2:
          if inner_index3==0:
            self.opclist=tags['Betriebsstunden']
          

    def reportProgress(self,tagValues:dict):
        """Defines the update of the tags after getting the new Values from the Worker thread

        :param tagValues: List of tags with the new tagValues
        :type tagValues: Dictionary
        """
        #print(tagValues)
        #try:
        outer_index=self.tabs.currentIndex()
        inner_index1=self.innerTabs1.currentIndex()
        inner_index2=self.innerTabs2.currentIndex()
        inner_index3=self.innerTabs3.currentIndex()

        keys=tagValues.keys()
        val1={} #Values Dictionary to update steu_strasse_1
        val2={} #Values Dictionary to update steu_meld_starsse_1
        val3={} #Values Dictionary to update steu_strasse_2
        val4={} #Values Dictionary to update steu_meld_starsse_2
        val5={} #Values Dictionary to update Betriebsstunden
        val6={} #Values Dictionary to update Futter1
        val7={} #Values Dictionary to update Futter2
        val8={}
        val9={}
        val10={}

        if outer_index == 0:
          if inner_index1==0:
            for i in keys:
              val8[i]=tagValues[i]
            self.strasse_1.updateAll(val8)  
          elif inner_index1==1:
            for i in keys:
              val1[i]=tagValues[i]
            self.steu_strasse_1.updateAll(val1)  
          elif inner_index1==2:
            for i in keys:
              val6[i]=tagValues[i]
            self.fuet_strasse_1.updateAll(val6)
          elif inner_index1==3:
            for k in keys:
              val2[k]=tagValues[k]
            self.steu_meld_starsse_1.updateAll(val2)  
        
        elif outer_index==1:
          if inner_index2==0:
            for i in keys:
              val9[i]=tagValues[i]
            self.strasse_2.updateAll(val9) 
          elif inner_index2==1:
            for i in keys:
              val3[i]=tagValues[i]
            self.steu_strasse_2.updateAll(val3)
          elif inner_index2==2:
            for i in keys:
              val7[i]=tagValues[i]
            self.fuet_strasse_2.updateAll(val7)  
          elif inner_index1==3:
            for k in keys:
              val4[k]=tagValues[k]
            self.steu_meld_starsse_2.updateAll(val4)  
        elif outer_index==2:
          for c in keys:
            val5[c]=tagValues[c]
          self.betrieb.updateAll(val5)
       
        for i in keys:
          val10[i]=tagValues[i]
        self.side_bar.updateAll(val10)

          
if __name__ == '__main__':

    app = QApplication(sys.argv)
    # app.setStyle('Fusion')
    window = Window()
    sys.exit(app.exec_())


#TODO Swap all german umlauts in the strings to a simplified form