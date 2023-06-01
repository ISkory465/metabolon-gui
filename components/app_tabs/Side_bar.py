from PyQt5.QtWidgets    import *
from PyQt5.QtCore       import Qt
from ..faceplates.facelpates_new   import InfoField
from ..faceplates.faceplate_mixer  import Mixer
from ..faceplates.faceplate_endlager import Endlager



class Page():

    def UI(self, window:QMainWindow):

        #Main layout of the first tab 'Straße 1"
        self.vbox=QVBoxLayout()


        #Tab is split into three horizontal boxes
        self.hbox1 = QHBoxLayout()
        self.hbox2 = QHBoxLayout()
        self.hbox3 = QHBoxLayout()

        
        #Layout relation
        self.vbox.addLayout(self.hbox1)
        self.vbox.addLayout(self.hbox2)
        self.vbox.addLayout(self.hbox3)
        self.vbox.setAlignment(Qt.AlignTop)
        
        self.hbox1.setAlignment(Qt.AlignLeft)


        window.sb_widget.setLayout(self.hbox1)

        
        # hbox1 Content
        self.label = InfoField(name = "CH4 [%]", 
                         layout = self.vbox)
        self.label2 = QLabel('Valera')
        self.hbox1.addWidget(self.label2)




if __name__=='__main__':
    pass