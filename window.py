from ast import Try
from http import client
import imp
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QObject, QThread, pyqtSignal,QTimer
import OpenOPC
import pywintypes
from OPC_Connection import OPC_Client

pywintypes.datetime = pywintypes.TimeType

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
                    print(n)
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
        self.setGeometry(100,100,800,600)
        self.setWindowTitle('Elementary OPC Test with Multithreading')
        self.UI()
        
    def UI(self):
        self.listWidget=QListWidget(self)
        self.listWidget.move(90,80)
        self.editor=QTextEdit(self)
        self.editor.move(90,300)
        self.editor2=QTextEdit(self)
        self.editor2.move(350,300)
        #################################################################
       
        self.nameLabel=QLineEdit(self)
        #self.nameLabel.setText('Hello')
        self.nameLabel.setPlaceholderText('Enter Value')
        self.nameLabel.move(100,20)
        btnList=QPushButton("List Servers",self)
        btnList.move(100,50)
        btnList.clicked.connect(self.listServers)
        btnListO=QPushButton("List Options",self)
        btnListO.move(200,50)
        btnListO.clicked.connect(self.listOptions)
        btnAdd=QPushButton("Connect",self)
        btnAdd.move(350,80)
        btnAdd.clicked.connect(self.funcConnect)
        btnDelete=QPushButton("Delete",self)
        btnDelete.move(350,110)
        btnDelete.clicked.connect(self.funcDelete)
        btnGet=QPushButton("Get",self)
        btnGet.move(350,140)
        btnGet.clicked.connect(self.funcGet)
        btnDot=QPushButton('.+',self)
        btnDot.move(350,170)
        btnDot.clicked.connect(self.funcDot)
        btnClose=QPushButton('Close',self)
        btnClose.move(350,200)
        btnClose.clicked.connect(self.funcClose)
        btnCreateList=QPushButton('Creat OPC Tags list',self)
        btnCreateList.move(90,270)
        #self.opcList=[]
        btnCreateList.clicked.connect(self.funcCreate)
        self.opcList=[]


        self.timer = QTimer()
        self.timer.setInterval(10000)
        self.timer.timeout.connect(self.runLongTask)
        self.timer.start()

        self.show()
        
    def funcCreate(self):
        val=self.listWidget.currentItem().text()
        self.opcList.append(val)
        self.editor.setText(str(self.opcList))
        #print(self.opcList)
        #self.opcList.addItems(items)
        #ls=list[self.listWidget.selectedItems()]
        

    def runLongTask(self):
        """Long-running task in 5 steps."""
        # Step 2: Create a QThread object
        self.thread = QThread()
        #x=[1,2,3]
        # Step 3: Create a worker object
        #ls=['Random.Int4','Random.Int8']
        self.worker = Worker(self.opcList)
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
            self.editor2.setText(str(n))
        except:
            self.editor2.setText('No Values')

    def listServers(self):
        self.client1=OPC_Client()
        list1=self.client1.servernames()
        self.listWidget.addItems(list1)
        self.flag=0
    
    def listOptions(self):
        x=self.nameLabel.text()
        #print(x)
        if self.flag==0:
            val=self.client1.listValues()
            self.flag=1
        else:
            val=self.client1.listValues2(x)
        
        self.listWidget.addItems(val)
    
    def funcConnect(self):
        val=self.listWidget.currentItem().text()
        self.client1.start_connection(val)
        
    def funcClose(self):
        
        self.client1.close_connection()


    def funcDelete(self):
        #id=self.listWidget.currentRow()
        self.listWidget.clear()
    
    def funcGet(self):
        val=self.listWidget.currentItem().text()
        self.nameLabel.setText(val)
        #print(val)
    def funcDot(self):
        val=self.listWidget.currentItem().text()
        text=self.nameLabel.text()+'.'+val
        self.nameLabel.setText(text)



def main():
    App = QApplication(sys.argv)
    window =Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()



