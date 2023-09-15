from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

class ValveLabelWidget(QWidget):
    def __init__(self, label="", sizeH=60, sizeW=30):
        super().__init__()
        self.valve = ValveWidget(sizeH, sizeW)
        self.valvename = label
        self.opcName=label
        self.valve.status = 2
        #self.setContentsMargins(0, 50, 0, 0)
        self.__drawvalve()

    def setStatus(self, value):
        self.valve.status = value
        self.valve.update()
    def update1(self,val:dict):
        try:
          Auf:bool
          error:bool
          Auf=val[self.opcName+':Auf']
          error=val[self.opcName+':error']

          if error:
            self.setStatus(2)
          elif Auf:
            self.setStatus(1)
          else:
            self.setStatus(0)
          #print('If Statement done')
        except Exception as e:
          print('Exception raised')
          #print(val[self.opcName])
          print(str(e))

    def __drawvalve(self):
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.label = QLabel(self.valvename)
        self.layout.setAlignment(Qt.AlignCenter)

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.valve)


class ValveWidget(QWidget):
    def __init__(self, sizeH=40, sizeW=20):
        super().__init__()
        self.setMinimumSize(sizeH, sizeW)
        self.valvesizeH = sizeH
        self.valvesizeW = sizeW
        self.status = 2

    def setStatus(self, value):
        self.status = value
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.black,  2, Qt.SolidLine))

        if self.status == 0:
            valvecolor = Qt.blue
        elif self.status == 1:
            valvecolor = Qt.green
        elif self.status == 2:
            valvecolor = Qt.red

        painter.setBrush(QBrush(valvecolor, Qt.SolidPattern))

        points = [
            QPoint(8,0),
            QPoint(8,self.valvesizeW),
            QPoint(self.valvesizeH,0),
            QPoint(self.valvesizeH,self.valvesizeW)
            ]
        poly = QPolygon(points)
        painter.drawPolygon(poly)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QWidget()

    # Create a QVBoxLayout
    layout = QVBoxLayout()
    window.setLayout(layout)

    # Create the valve widget
    valve1 = ValveWidget()
    valve2 = ValveLabelWidget("Test Name", 40, 20)

    # Add the valve widget to the layout
    layout.addWidget(valve1)
    layout.addWidget(valve2)

    window.show()

    valve1.setStatus(2)
    valve2.setStatus(1)

    sys.exit(app.exec_())