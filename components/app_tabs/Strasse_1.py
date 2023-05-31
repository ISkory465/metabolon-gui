from PyQt5.QtWidgets    import *
from PyQt5.QtCore       import Qt
from ..faceplates.facelpates_new   import Box
from ..faceplates.faceplate_mixer  import Mixer
from ..faceplates.faceplate_endlager import Endlager



class Page():

    def UI(self,window:QMainWindow):

        #Main layout of the first tab 'Straße 1"
        self.vbox=QVBoxLayout()


        #Tab is split into three horizontal boxes
        self.hbox1 = QHBoxLayout()
        self.hbox2 = QHBoxLayout()
        self.hbox3 = QHBoxLayout()

        #First horizontal hbox1 layout contains three vertical boxes
        self.vbox1_1 = QVBoxLayout()
        self.vbox1_2 = QVBoxLayout()
        self.vbox1_3 = QVBoxLayout()

        #Layout relation
        self.vbox.addLayout(self.hbox1)
        self.vbox.addLayout(self.hbox2)
        self.vbox.addLayout(self.hbox3)
        self.vbox.setAlignment(Qt.AlignTop)
        self.hbox1.addLayout(self.vbox1_1)
        self.hbox1.addLayout(self.vbox1_2)
        self.hbox1.addLayout(self.vbox1_3)
        self.hbox1.setAlignment(Qt.AlignLeft)


        window.tab1.setLayout(self.vbox)

        
        # hbox1 Content
        self.mixer1 = Mixer(name="Fermenter", layout = self.vbox1_1)
        self.mixer2 = Mixer(name="Nachgärer", layout = self.vbox1_2)
        self.endlager = Endlager(name="Endlager", layout = self.vbox1_3)




if __name__=='__main__':
    pass