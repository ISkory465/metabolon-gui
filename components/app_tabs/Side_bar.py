from PyQt5.QtWidgets    import *
from PyQt5.QtCore       import Qt
from components.faceplates.faceplate_side_bar import SideBarFaceplate




class SideBar(QWidget):

    def __init__(self):
        super().__init__()
        self.setMinimumWidth(200)

        self.sb_layout = QVBoxLayout()
        self.sb_layout.setAlignment(Qt.AlignTop)
        
        #COntent of the Control Panel
        self.content = SideBarFaceplate(name="Control Panel", layout=self.sb_layout)

        self.sb_layout.addWidget(self.content)

        self.setLayout(self.sb_layout)


        

        
    def addWidget(self, widget):
        self.sb_layout.addWidget(widget)



# if __name__ == '__main__':
#     app = QApplication([])
#     window = QMainWindow()
#     window.setWindowTitle("Page Test")
#     page = Page()
#     page.UI(window)
#     window.show()
#     app.exec_()
