import sys
from PyQt5.QtWidgets import *
# import OpenOPC
# import pywintypes
from PyQt5.QtCore import *
# pywintypes.datetime = pywintypes.TimeType


#app tabs import:
from components.app_tabs.Strasse_1                import Page as Strasse_1
from components.app_tabs.Steuerung_Strasse_1      import Page as St_Strasse_1
from components.app_tabs.Steuerung_Strasse_2      import Page as St_Strasse_2
from components.app_tabs.Fuetterung_Strasse_1     import Page as Fuet_Strasse_1
from components.app_tabs.Stoermeldungen_Strasse_1 import Page as St_Meld_1
from components.app_tabs.Stoermeldungen_Strasse_2 import Page as St_Meld_2
from components.app_tabs.Betriebsstunden          import Page as Betriebsstunden
from components.app_tabs.Fuetterung_Strasse_2     import Page as Fuet_Strasse_2

# Rework:
# import components.app_tabs.Fuetterung_Strasse_1 as Fuet_Strasse_1
# import components.app_tabs.Stoermeldungen_Strasse_2 as St_meld_Strasse_2


opcPrefix='SIMATIC 300-Station.CPU 315-2 DP.'
# class Worker(QObject):
#     finished = pyqtSignal()
#     progress = pyqtSignal(dict)
#     #recieved = pyqtSignal(list)
    
#     def __init__(self, x:dict):
#       self.varDict=x
#       #self.client=client
#       super().__init__()

#     def run(self):
#         """Long-running task."""
#         #self.recieved.connect(self.rec)
#         try:
#             opc=OpenOPC.client()
#             #print('client')   
#             opc.connect("OPC.SimaticNET")

#             if self.varDict=={}:
#                 results={'Result':'No Values'}
#                 print(results)
#             else:
#                 results={}
#                 keys=self.varDict.keys()
#                 for x in keys:
#                     #print(self.varDict[x])
#                     tagValues=opc[self.varDict[x]]
#                     #print(tagValues)
#                     #tagValues=str(tagValues)
#                     results[x]=tagValues
            
#             print(results)

            
#             #print(self.x)
#             self.progress.emit(results)
#             opc.close()
#             self.finished.emit()
#         except:
#             print('error')
#             x=['thread not working']
#             self.progress.emit(x)
#             self.finished.emit()

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
        self.page1 = Strasse_1()
        self.page1.UI(self)
        
        #Second Tab
        self.tab2 = QWidget()
        # self.tabs.addTab(self.tab2,"Strasse 2")
        # self.Tab_Strasse2()

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


        #OPC List update
        # self.tabs.currentChanged.connect(self.updateOPCList)

        #Default OPC list for the first tab --> to be changed
        self.opclist={'First Tag':'Random.Int4','Second Tag':'Random.Int8'}

        # Define the timer for periodic update of tags
        # self.timer = QTimer()
        # self.timer.setInterval(5000)
        # self.timer.timeout.connect(self.runLongTask)
        # self.timer.start()
        self.show()

                        
                
        mainLayout.addWidget(self.tabs)
        self.setLayout(mainLayout)




    """ def runLongTask(self):
        ""Create the Worker thread that runs periodically to update current list of OPC tags.""
        # Step 2: Create a QThread object
        self.thread = QThread()
        #x=[1,2,3]
        # Step 3: Create a worker object
        #results=['Random.Int4','Random.Int8']
        # self.worker = Worker(self.opclist)
        # Step 4: Move worker to the thread
        # self.worker.moveToThread(self.thread)

        # Step 5: Connect signals and slots
        
        #print('Heyyy')
        
        
        # self.thread.started.connect(self.worker.run)
        # self.worker.finished.connect(self.thread.quit)
        # self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        # self.worker.progress.connect(self.reportProgress)
        
        #print('Byee')
        # Step 6: Start the thread
        self.thread.start() """

    def updateOPCList(self):
        """Change the list of OPC tags depending on the active tab

        """
        x=self.tabs.currentIndex()
        global opcPrefix
        #print(x)
        if x == 0:
          self.opclist={'HE11.Hand':opcPrefix+'DB5.HE11.BF2','HE11.AUTO':opcPrefix+'DB5.HE11.BF3','HE11.AUS':opcPrefix+'DB5.HE11.BF4',
                        'HE12.Hand':opcPrefix+'DB5.HE12.BF2','HE12.AUTO':opcPrefix+'DB5.HE12.BF3','HE12.AUS':opcPrefix+'DB5.HE12.BF4',
                        'RW13.Hand':opcPrefix+'DB5.RW13.BF2','RW13.AUTO':opcPrefix+'DB5.RW13.BF3','RW13.AUS':opcPrefix+'DB5.RW13.BF4',
                        'RW14.Hand':opcPrefix+'DB5.RW14.BF2','RW14.AUTO':opcPrefix+'DB5.RW14.BF3','RW14.AUS':opcPrefix+'DB5.RW14.BF4',
                        'SC11.Hand':opcPrefix+'DB5.SC11.BF2','SC11.AUTO':opcPrefix+'DB5.SC11.BF3','SC11.AUS':opcPrefix+'DB5.SC11.BF4',
                        'Temp. Fer 1 (\N{DEGREE SIGN}C)':opcPrefix+'DB70.TI15_TMP_SK','Temp. Ng 1 [\N{DEGREE SIGN}C]':opcPrefix+'DB70.TI16_TMP_SK',
                        'Temp. Vorlauf Fer 1 (\N{DEGREE SIGN}C)':opcPrefix+'DB302.PT_100_FER1','Temp. Vorlauf Ng 1 [\N{DEGREE SIGN}C]':opcPrefix+'DB302.PT_100_NGA1',
                        'Magentgasventill Fer 1':opcPrefix+'A32_4','Magentgasventill Fer 2':opcPrefix+'A32_5',
                        'Fermenter Temp.-Sollwert (\N{DEGREE SIGN}C)':opcPrefix+'DB84.TI15_FER1.SW','RW13.SW_AKT [%]':opcPrefix+'DB10.RW13_SW.SW_AKT',
                        'RW11 Auto Sollwert [%]':opcPrefix+'DB10.RW11_SW.SW2','RW11 Hand Sollwert [%]':opcPrefix+'DB10.RW11_SW.SW1',
                        'RW11 Pause Soll [min] ln':opcPrefix+'DB30.RW11.SZ_PAU','RW11 Run Soll [min] ln':opcPrefix+'DB30.RW11.SZ_EIN',
                        'RW12 Auto Sollwert [%]':opcPrefix+'DB10.RW12_SW.SW2','RW12 Hand Sollwert [%]':opcPrefix+'DB10.RW12_SW.SW1',
                        'RW12 Pause Soll [min] ln':opcPrefix+'DB30.RW12.SZ_PAU','RW12 Run Soll [min] ln':opcPrefix+'DB30.RW12.SZ_EIN',
                        'RW13 Auto Sollwert [%]':opcPrefix+'DB10.RW13_SW.SW2','RW13 Hand Sollwert [%]':opcPrefix+'DB10.RW13_SW.SW1',
                        'RW13 Pause Soll [min] ln':opcPrefix+'DB30.RW13.SZ_PAU','RW13 Run Soll [min] ln':opcPrefix+'DB30.RW13.SZ_EIN',
                        'RW14 Auto Sollwert [%]':opcPrefix+'DB10.RW14_SW.SW2','RW14 Hand Sollwert [%]':opcPrefix+'DB10.RW14_SW.SW1',
                        'RW14 Pause Soll [min] ln':opcPrefix+'DB30.RW14.SZ_PAU','RW14 Run Soll [min] ln':opcPrefix+'DB30.RW14.SZ_EIN',
                        'Nachgärer Temp.-Sollwert [\N{DEGREE SIGN}C]':opcPrefix+'DB84.TI16_NGA1.SW'}

          
        elif x==1:
          self.opclist={'First Tag':'Random.Int1','Second Tag':'Random.Real8'}

    def reportProgress(self,tagValues:dict):
        """Defines the update of the tags after getting the new Values from the Worker thread

        :param tagValues: List of tags with the new tagValues
        :type tagValues: Dictionary
        """
        #print(tagValues)
        try:
          x=self.tabs.currentIndex()
          keys=tagValues.keys()
          #print(keys)
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
          #print(str(val1))  
          self.page3.updateAll(val1)

        except Exception as e:
            print('no tagValues')
            print(str(e))
            #self.listWidget.addItem('No Values')
            #print(tagValues)
          


def main():
    App=QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(App.exec_())

if __name__=='__main__':
    main()