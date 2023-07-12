from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from ..widgets.infofield_dbl import InfoField, InfoFieldV2
from ..widgets.therm import ThermometerWidget
from ..widgets.schnecke import PlayButton
from ..widgets.gauge import Gauge
from .mixer_n_heater import BigMixer
import sys

from components.widgets import gauge


#TODO make cleanning and comments

class Mixer(QGroupBox):
    """Mixer set of elements for the Strasse 1 tab

    :param QGroupBox: _description_
    :type QGroupBox: _type_
    """
    
    def __init__(self, name, opcID=None):
        
        super().__init__(name) 
        self.opcName=name
        #Main laout of the mixer with 2x2 element position

        self.vbox = QVBoxLayout()
        self.vbox.setAlignment(Qt.AlignTop)
        self.hbox = QHBoxLayout()
        self.hbox.setAlignment(Qt.AlignVCenter)
        self.hbox1 = QHBoxLayout()
        self.hbox1.setAlignment(Qt.AlignTop)

        self.vbox.addLayout(self.hbox)
        self.vbox.addLayout(self.hbox1)

        #numerical data box contains 2 vertical boxes
        self.nm_1_column = QVBoxLayout()
        # print(self.nm_1_column.geometry())
        self.nm_2_column = QVBoxLayout()
        
        #Layout relation
        self.hbox.addLayout(self.nm_1_column)
        self.hbox.addLayout(self.nm_2_column)
        self.nm_1_column.setAlignment(Qt.AlignTop)
        self.nm_2_column.setAlignment(Qt.AlignTop)
                
        # Schnecke VBox
        schnecke_vbox = QVBoxLayout()
        schnecke_vbox.setAlignment(Qt.AlignTop)

        # schnecke_vbox.addStretch(1)
        self.schnecke_label = QLabel("Schnecke")
        self.schnecke_label.setAlignment(Qt.AlignCenter)
        schnecke_vbox.addWidget(self.schnecke_label)
        self.hbox.addLayout(schnecke_vbox)
        PlayButtonName=self.opcName+':Schnecke'
        self.playbutton = PlayButton(PlayButtonName)
        schnecke_vbox.addWidget(self.playbutton)
        schnecke_vbox.setAlignment(Qt.AlignVCenter)
        # schnecke_vbox.addStretch(1)  # Pushes the PlayButton up
        
        therm_layout = QVBoxLayout()
        thermometerName=self.opcName+':Thermometer'

        self.thermometer = ThermometerWidget(thermometerName) #add  self.name parameter in class thermometer
        therm_layout.addWidget(self.thermometer)
        therm_layout.setAlignment(Qt.AlignVCenter)
        self.hbox.addLayout(therm_layout)


        gaugeName=self.opcName+':gauge'
        self.gauge = Gauge(gaugeName) #add self.name parameter in class
        self.hbox1.addWidget(self.gauge)
        horizontalSpacer = QSpacerItem(75, 10, QSizePolicy.Minimum, QSizePolicy.Fixed) 
        self.hbox1.addItem(horizontalSpacer)
        
        bigMixerNamer=self.opcName+':bigMixer'
        self.big_mixer = BigMixer(bigMixerNamer) #add self.name parameter in class
        self.hbox1.addWidget(self.big_mixer)

        self.setLayout(self.vbox)


        #First (left) column content for the nm_1_column
        self.ch4 = InfoFieldV2(opcID=self.opcName,name = "CH4 [%]")
        self.co2 = InfoFieldV2(opcID=self.opcName,name = "CO2 [%]")
        self.H2 = InfoFieldV2(opcID=self.opcName,name = "H2 [ppm]")
        self.H2S = InfoFieldV2(opcID=self.opcName,name = "H2S [ppm]")

        self.nm_1_column.addWidget(self.ch4)
        self.nm_1_column.addWidget(self.co2)
        self.nm_1_column.addWidget(self.H2)
        self.nm_1_column.addWidget(self.H2S)
        
        #Second (right) column content for the nm_2_column
        self.Qgas = InfoFieldV2(opcID=self.opcName,name = "Qgas [l/min]")
        self.Qgas1 = InfoFieldV2(opcID=self.opcName,name = "Qgas [l]")
        self.pH = InfoFieldV2(opcID=self.opcName,name = "pH [-]")

        self.nm_2_column.addWidget(self.Qgas)
        self.nm_2_column.addWidget(self.Qgas1)
        self.nm_2_column.addWidget(self.pH)
    def update(self,inputs: dict):
        """method to update all objects in current tab periodically after reading the values in different thread

        :param inputs: tag values
        :type inputs: dict
        """
        objectList=[    #self.playbutton,
                        self.thermometer,
                        self.gauge,
                        self.big_mixer
                    ]


        for o in objectList:
            #iterate over an update method that should be added to all faceplate objects similar to box object
            o.update1(inputs)
        
        objectList2=[self.ch4,
                     self.co2,
                     self.H2,
                     self.H2S,
                     self.Qgas,
                     self.Qgas1,
                     self.pH]
    
        for i in objectList2:
            i.update(inputs)

if __name__ == "__main__":
    pass