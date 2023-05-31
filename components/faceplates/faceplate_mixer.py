from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from .facelpates_new import InfoField
from .faceplate_therm import ThermometerWidget
from .faceplate_playbtn import PlayButton
from .faceplate_gauge import Gauge
from .faceplate_big_mixer import BigMixer

from QLed import QLed


class Mixer(QGroupBox):
    """Mixer set of elements for the Strasse 1 tab

    :param QGroupBox: _description_
    :type QGroupBox: _type_
    """
    
    def __init__(self, name, layout, opcID=None):
        
        super().__init__(name) 
        self.layout = layout

        #Main laout of the mixer with 2x2 element position
        self.grid = QGridLayout()
        

        # [0.0] -----------------------------------------
        #Numerical Fileds layout for [0,0] grid position
        self.numerical_data = QHBoxLayout()

        #numerical data box contains 2 vertical boxes
        self.nm_1_column = QVBoxLayout()
        self.nm_2_column = QVBoxLayout()
        
        #Layout relation
        self.numerical_data.addLayout(self.nm_1_column)
        self.numerical_data.addLayout(self.nm_2_column)
        self.numerical_data.setAlignment(Qt.AlignLeft)
        self.nm_1_column.setAlignment(Qt.AlignTop)
        self.nm_2_column.setAlignment(Qt.AlignTop)
        self.grid.addLayout(self.numerical_data, *[0,0])

        self.thermometer = ThermometerWidget() #add  self.name parameter in class termometer
        self.thermometer.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed) 
        # self.grid.addWidget(self.thermometer, *[0,2], alignment=Qt.AlignLeft)
        self.grid.addWidget(self.thermometer, *[0,2], alignment=Qt.AlignLeft)

        self.playbutton = PlayButton()
        self.playbutton.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed) 
        # self.spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.grid.addWidget(self.playbutton, *[0,1], alignment=Qt.AlignLeft)
        # self.grid.addItem(self.spacer, *[0,1])

        self.gauge = Gauge() #add self.name parameter in class
        self.gauge.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed) 
        self.grid.addWidget(self.gauge, *[1,0])

        self.big_mixer = BigMixer() #add self.name parameter in class
        self.big_mixer.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred) 
        self.grid.addWidget(self.big_mixer, 1, 1, 2, 3)


        self.layout.addWidget(self)
        self.setLayout(self.grid)


        
        # self.grid.addWidget(QLabel('  '), *[1,1])




        #First (left) column content for the nm_1_column
        self.ch4 = InfoField(name = "CH4 [%]", 
                         layout = self.nm_1_column)
        self.co2 = InfoField(name = "CO2 [%]", 
                         layout = self.nm_1_column)
        self.H2 = InfoField(name = "H2 [ppm]", 
                         layout = self.nm_1_column)
        self.H2S = InfoField(name = "H2S [ppm]", 
                         layout = self.nm_1_column)
        
        #Second (right) column content for the nm_2_column
        self.Qgas = InfoField(name = "Qgas [l/min]", 
                         layout = self.nm_2_column)
        self.Qgas1 = InfoField(name = "CH4 [%]", 
                         layout = self.nm_2_column)
        self.pH = InfoField(name = "pH [-]", 
                         layout = self.nm_2_column)



