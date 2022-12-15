import sys
from PyQt5.QtWidgets import *
import OpenOPC
import pywintypes
from PyQt5.QtCore import QObject, QThread, pyqtSignal,QTimer
pywintypes.datetime = pywintypes.TimeType


#app tabs import:
import components.app_tabs.Strasse_1 as Strasse1
from components.app_tabs.Steuerung_Strasse_1 import St as St_Strasse_1
import components.app_tabs.Steuerung_Strasse_2 as St_Strasse_2
import components.app_tabs.Fuetterung_Strasse_1 as Fuet_Strasse_1
import components.app_tabs.Stoermeldungen_Strasse_2 as St_meld_Strasse_2
import components.app_tabs.Betriebsstunden as Betriebsstunden

class Worker(QObject):
    finished = pyqtSignal()
    progress = pyqtSignal(dict)
    #recieved = pyqtSignal(list)
    
    def __init__(self, x:dict):
      self.varDict=x
      #self.client=client
      super().__init__()

    def run(self):
        """Long-running task."""
        #self.recieved.connect(self.rec)
        try:
            opc=OpenOPC.client()
            #print('client')   
            opc.connect("Matrikon.OPC.Simulation.1")

            if self.varDict=={}:
                results={'Result':'No Values'}
                print(results)
            else:
                results={}
                keys=self.varDict.keys()
                for x in keys:
                    tagValues=opc[self.varDict[x]]
                    #tagValues=str(tagValues)
                    results[x]=tagValues
            
            #print(results)

            
            #print(self.x)
            self.progress.emit(results)
            opc.close()
            self.finished.emit()
        except:
            print('error')
            x=['thread not working']
            self.progress.emit(x)
            self.finished.emit()

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
        # self.tabs.addTab(self.tab1,"Strasse 1")
        # Strasse1.UI(self)

        #Second Tab
        self.tab2 = QWidget()
        # self.tabs.addTab(self.tab2,"Strasse 2")
        # self.Tab_Strasse2()

        #Third Tab
        self.tab3 = QWidget()
        self.tabs.addTab(self.tab3,"Steuerung Strasse 1")
        self.st=St_Strasse_1()
        self.st.UI(self)

        #Fourth Tab
        self.tab4 = QWidget()
        self.tabs.addTab(self.tab4,"Steuerung Strasse 2")
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

        #OPC List update
        self.tabs.currentChanged.connect(self.updateOPCList)
        #Default OPC list for the first tab --> to be changed
        self.opclist={'First Tag':'Random.Int4','Second Tag':'Random.Int8'}
        # Define the timer for periodic update of tags
        self.timer = QTimer()
        self.timer.setInterval(10000)
        #self.timer.timeout.connect(self.runLongTask)
        #self.timer.start()
        #self.show()

                        
                
        mainLayout.addWidget(self.tabs)
        self.setLayout(mainLayout)

    def runLongTask(self):
        """Create the Worker thread that runs periodically to update current list of OPC tags."""
        # Step 2: Create a QThread object
        self.thread = QThread()
        #x=[1,2,3]
        # Step 3: Create a worker object
        #results=['Random.Int4','Random.Int8']
        self.worker = Worker(self.opclist)
        # Step 4: Move worker to the thread
        self.worker.moveToThread(self.thread)

        # Step 5: Connect signals and slots
        
        #print('Heyyy')
        
        
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.worker.progress.connect(self.reportProgress)
        
        #print('Byee')
        # Step 6: Start the thread
        self.thread.start()

    def updateOPCList(self):
        """Change the list of OPC tags depending on the active tab

        """
        x=self.tabs.currentIndex()

        #print(x)
        #if x == 0:
          #self.opclist={'First Tag':'Random.Int1',self.facePlate1.name+'.Hand':'Random.Boolean',self.facePlate1.name+'.AUS':'Bucket Brigade.Boolean',self.facePlate1.name+'.AUTO':'Square Waves.Boolean'}

          
        #elif x==1:
          #self.opclist={'First Tag':'Random.Int1','Second Tag':'Random.Real8'}

    def reportProgress(self,tagValues:dict):
        """Defines the update of the tags after getting the new Values from the Worker thread

        :param tagValues: List of tags with the new tagValues
        :type tagValues: Dictionary
        """
        #print(tagValues)
        try:
          x=self.tabs.currentIndex()
          keys=tagValues.keys()
          print(keys)
          val1={}
          val2={}

          #print(x)
          if x == 0:
            #self.listWidget.clear()
            for i in keys:
              #self.listWidget.addItem(str(tagValues[i]))
              val1[i]=tagValues[i]
              
          elif x==1:
            #self.opclist=['Random.Int1','Random.Real8']
            #self.listWidget2.clear()
            for k in keys:
              #self.listWidget2.addItem(str(tagValues[k]))
              val2[k]=tagValues[k]

          self.st.updateAll(val2)

        except:
            print('no tagValues')
            #self.listWidget.addItem('No Values')
            #print(tagValues)
          


def main():
    App=QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(App.exec_())

if __name__=='__main__':
    main()