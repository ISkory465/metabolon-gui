from PyQt5.QtWidgets    import *
from PyQt5.QtCore       import Qt

from components.faceplates.faceplate_gauge import Gauge

class SideBar(QWidget):
    def __init__(self):
        super().__init__()
        self.setMinimumWidth(200)

        self.gauge = Gauge()

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.layout.addWidget(self.gauge)

    def addWidget(self, widget):
        self.layout.addWidget(widget)



if __name__ == '__main__':
    app = QApplication([])
    window = QMainWindow()
    window.setWindowTitle("Page Test")
    page = Page()
    page.UI(window)
    window.show()
    app.exec_()
