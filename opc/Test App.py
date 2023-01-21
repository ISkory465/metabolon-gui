import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QObject, QThread, pyqtSignal,QTimer
import OpenOPC
import pywintypes
from faceplates import Box
from Test_Tab import St as St_Strasse_1

pywintypes.datetime = pywintypes.TimeType


class Worker(QObject):
    finished = pyqtSignal()
    progress = pyqtSignal(dict)
    #recieved = pyqtSignal(list)
    
    def __init__(self, x):
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
                    n=opc[self.varDict[x]]
                    #n=str(n)
                    results[x]=n
            
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
        self.setWindowTitle("Tab Widget")
        self.setGeometry(350,150,600,600)
        self.UI()

    def UI(self):
        mainLayout=QVBoxLayout()
        self.tabs =QTabWidget()

        self.tab1=QWidget()
        self.tab2=QWidget()
        self.tab3=QWidget()
        self.tabs.addTab(self.tab1,"Steuerung Straße 1")
        self.tabs.addTab(self.tab2,"Steuerung Straße 2")
        #self.tabs.addTab(self.tab3,"Last Tab")
        self.tab3 = QWidget()
        self.tabs.addTab(self.tab3,"Steuerung Strasse 1")
        self.st=St_Strasse_1()
        self.st.UI(self)
        ###################Widgets###############
        vbox=QVBoxLayout()
        vbox1=QVBoxLayout()
        vbox2=QVBoxLayout()
        hbox=QHBoxLayout()
        hbox2=QHBoxLayout()
        self.text=QLabel("Hello Python")
        self.btn1=QPushButton("First Tab")
        self.listWidget=QListWidget(self)
        self.listWidget2=QListWidget(self)

        #self.btn1.clicked.connect(self.btnFunc)
        self.btn2 =QPushButton("Second Tab")
        self.btn2.clicked.connect(self.btnFunc2)

        vbox.addWidget(self.text)
        vbox.addWidget(self.listWidget)
        
        #vbox.addWidget(self.btn1)
        hbox.addWidget(self.btn2)
        hbox.addWidget(self.listWidget2)
        #self.facePlate1=Box('HE11','DB5.HE11')
        #vbox1.addWidget(self.facePlate1)
        #self.facePlate2=Box('RW13','DB5.RW13')
       # vbox1.addWidget(self.facePlate2)
        hbox2.addLayout(vbox1,25)
        hbox2.addLayout(vbox2,75)
        vbox.addLayout(hbox2)
        self.tab1.setLayout(vbox)
        self.tab2.setLayout(hbox)
        self.tabs.currentChanged.connect(self.btnFunc2)
        #self.facePlate1.radioBtn1.clicked.connect(self.facePlate1.write)
        mainLayout.addWidget(self.tabs)
        self.setLayout(mainLayout)
        self.opclist={'First Tag':'Random.Int4','Second Tag':'Random.Int8'}

        self.timer = QTimer()
        self.timer.setInterval(10000)
        self.timer.timeout.connect(self.runLongTask)
        self.timer.start()
        self.show()
    
    
    def runLongTask(self):
        """Long-running task in 5 steps."""
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

    def reportProgress(self,n):
        #print(n)
        try:
          x=self.tabs.currentIndex()
          keys=n.keys()
          print(keys)
          val1={}
          val2={}

          #print(x)
          if x == 0:
            self.listWidget.clear()
            for i in keys:
              self.listWidget.addItem(str(n[i]))
              val1[i]=n[i]
              
          elif x==1:
            #self.opclist=['Random.Int1','Random.Real8']
            self.listWidget2.clear()
            for k in keys:
              self.listWidget2.addItem(str(n[k]))
              val2[k]=n[k]

          #self.facePlate1.update(val1)
          #self.facePlate2.update(val2)

        except:
            self.listWidget.addItem('No Values')
            #print(n)
    
    def btnFunc2(self):
        x=self.tabs.currentIndex()

        #print(x)
        if x == 0:
          #self.opclist={'First Tag':'Random.Int1',self.facePlate1.name+'.Hand':'Random.Boolean',self.facePlate1.name+'.AUS':'Bucket Brigade.Boolean',self.facePlate1.name+'.AUTO':'Square Waves.Boolean'}
            pass
          #self.listWidget.clear()
          #self.listWidget.addItems(self.opclist)
        elif x==1:
          self.opclist={'First Tag':'Random.Int1','Second Tag':'Random.Real8'}
          #self.listWidget2.clear()
          #self.listWidget2.addItems(self.opclist)
        
        self.runLongTask()

        

        #self.text.setText("Button is active")


def main():
    App=QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())

if __name__=='__main__':
    main()


#tags1={'Hand':'DB5.HE11.BF.Mano','Aus':'DB5.HE11.BF.Aus','Auto':'DB5.HE11.BF.Auto'}
