import sys
from time import sleep
import OpenOPC

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)
from PyQt5.QtCore import QObject, QThread, pyqtSignal
import pywintypes

# Snip...
pywintypes.datetime = pywintypes.TimeType

# Step 1: Create a worker class
class Worker(QObject):
    finished = pyqtSignal()
    progress = pyqtSignal(int)
    def __init__(self, x:dict):
      self.varDict=x
      #self.client=client
      super().__init__()
    
    def run(self):
        """Long-running task."""
        
        opc=OpenOPC.client()
        #print('client')   
        opc.connect("OPC.SimaticNET")
        print("Connection acquired")
        print(opc.info())
        if self.varDict=={}:
                results={'Result':'No Values'}
                print(results)
        else:
                results={}
                keys=self.varDict.keys()
                for x in keys:
                    print(self.varDict[x])
                    tagValues=opc[self.varDict[x]]
                    print(tagValues)
                    #tagValues=str(tagValues)
                    results[x]=tagValues
        print(results)
        for i in range(20):
            sleep(1)
            self.progress.emit(i + 1)
        opc.close()
        print("Connection closed")

        self.finished.emit()

class Window(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.clicksCount = 0
        self.setupUi()

    def setupUi(self):
        self.setWindowTitle("Freezing GUI")
        self.resize(300, 150)
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        # Create and connect widgets
        self.clicksLabel = QLabel("Counting: 0 clicks", self)
        self.clicksLabel.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.stepLabel = QLabel("Long-Running Step: 0")
        self.stepLabel.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.countBtn = QPushButton("Click me!", self)
        self.countBtn.clicked.connect(self.countClicks)
        self.longRunningBtn = QPushButton("Long-Running Task!", self)
        self.longRunningBtn.clicked.connect(self.runLongTask)
        # Set the layout
        layout = QVBoxLayout()
        layout.addWidget(self.clicksLabel)
        layout.addWidget(self.countBtn)
        layout.addStretch()
        layout.addWidget(self.stepLabel)
        layout.addWidget(self.longRunningBtn)
        self.centralWidget.setLayout(layout)

    def countClicks(self):
        self.clicksCount += 1
        self.clicksLabel.setText(f"Counting: {self.clicksCount} clicks")    
    def reportProgress(self, n):
        self.stepLabel.setText(f"Long-Running Step: {n}")

    def runLongTask(self):
        # Step 2: Create a QThread object
        self.thread = QThread()
        # Step 3: Create a worker object
        opcPrefix='SIMATIC 300-Station.CPU 315-2 DP.'
        opclist={'HE11.Hand':opcPrefix+'DB5.HE11.BF2','HE11.AUTO':opcPrefix+'DB5.HE11.BF3','HE11.AUS':opcPrefix+'DB5.HE11.BF4',
                        'HE12.Hand':opcPrefix+'DB5.HE12.BF2','HE12.AUTO':opcPrefix+'DB5.HE12.BF3','HE12.AUS':opcPrefix+'DB5.HE12.BF4',
                        'RW13.Hand':opcPrefix+'DB5.RW13.BF2','RW13.AUTO':opcPrefix+'DB5.RW13.BF3','RW13.AUS':opcPrefix+'DB5.RW13.BF4',
                        'RW14.Hand':opcPrefix+'DB5.RW14.BF2','RW14.AUTO':opcPrefix+'DB5.RW14.BF3','RW14.AUS':opcPrefix+'DB5.RW14.BF4',
                        'SC11.Hand':opcPrefix+'DB5.SC11.BF2','SC11.AUTO':opcPrefix+'DB5.SC11.BF3','SC11.AUS':opcPrefix+'DB5.SC11.BF4',
                        'Temp. Fer 1 (\N{DEGREE SIGN}C)':opcPrefix+'DB70.TI15_TMP_SK','Temp. Ng 1 [\N{DEGREE SIGN}C]':opcPrefix+'DB70.TI16_TMP_SK',
                        'Temp. Vorlauf Fer 1 (\N{DEGREE SIGN}C)':opcPrefix+'DB302.PT_100_FER1','Temp. Vorlauf Ng 1 [\N{DEGREE SIGN}C]':opcPrefix+'DB302.PT_100_NGA1'}
                       
        '''
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
        '''
        self.worker = Worker(opclist)
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

        # Final resets
        self.longRunningBtn.setEnabled(False)
        self.thread.finished.connect(
            lambda: self.longRunningBtn.setEnabled(True)
        )
        self.thread.finished.connect(
            lambda: self.stepLabel.setText("Long-Running Step: 0")
        )


app = QApplication(sys.argv)
win = Window()
win.show()
sys.exit(app.exec())