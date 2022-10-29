from cmath import e
from logging import exception
import sys
from tkinter import E
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QObject, QThread, pyqtSignal,QTimer
import OpenOPC
import pywintypes
from OPC_Connection import OPC_Client

class Worker(QObject):
    finished = pyqtSignal()
    progress = pyqtSignal(list)
    #recieved = pyqtSignal(list)
    
    def __init__(self, x ):
      self.varList=x
      #self.client=client
      super().__init__()

    def run(self):
        """Long-running task."""
        #self.recieved.connect(self.rec)
        try:
            opc=OpenOPC.client()
            #print('client')   
            opc.connect("Matrikon.OPC.Simulation.1")
            if self.varList==[]:
                ls=['No Values']
                print(ls)
            else:
                ls=[]
                for x in self.varList:
                    n=opc[x]
                    #print(n)
                    ls.append(n)

            
            #print(self.x)
            self.progress.emit(ls)
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
        self.tabs.addTab(self.tab1,"First Tab")
        self.tabs.addTab(self.tab2,"Second Tab")
        self.tabs.addTab(self.tab3,"Last Tab")

        ###################Widgets###############
        vbox=QVBoxLayout()
        hbox=QHBoxLayout()
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
        self.tab1.setLayout(vbox)
        self.tab2.setLayout(hbox)
        self.tabs.currentChanged.connect(self.btnFunc2)

        mainLayout.addWidget(self.tabs)
        self.setLayout(mainLayout)
        self.opclist=['Random.Int4','Random.Int8']

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
        #ls=['Random.Int4','Random.Int8']
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

    def reportProgress(self, n):
        #print(n)
        try:
          x=self.tabs.currentIndex()

          #print(x)
          if x == 0:
            #self.opclist=['Random.Int4','Random.Int8']
            self.listWidget.clear()
            for i in n:
              self.listWidget.addItem(str(i))
          elif x==1:
            #self.opclist=['Random.Int1','Random.Real8']
            self.listWidget2.clear()
            for k in n:
              self.listWidget2.addItem(str(k))
        
        except:
            self.listWidget.addItem('No Values')
            #print(n)
    
    def btnFunc2(self):
        x=self.tabs.currentIndex()

        #print(x)
        if x == 0:
          self.opclist=['Random.Int4','Random.Int8']
          #self.listWidget.clear()
          #self.listWidget.addItems(self.opclist)
        elif x==1:
          self.opclist=['Random.Int1','Random.Real8']
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