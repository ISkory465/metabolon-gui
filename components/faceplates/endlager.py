from PyQt5.QtWidgets import QApplication, QGroupBox, QVBoxLayout, QHBoxLayout, QWidget, QSpacerItem, QSizePolicy
from PyQt5.QtCore import Qt
from ..widgets.therm_endlager import EndThermometerWidget
from ..widgets.gauge import Gauge
from ..widgets.endlager_tank import EndlagerTank
import sys

# TODO: add documentation and make sure it works properly, make gauge smaller

class Endlager(QGroupBox):
    def __init__(self, name, opcID=None):
        super().__init__(name)
        self.opcName=name
        # Main layout for 2 horizontal boxes representing each row
        main_vbox = QVBoxLayout()
        main_vbox.setSpacing(10)
        main_vbox.setAlignment(Qt.AlignTop)

        # Two main horizontal layouts
        row1 = QHBoxLayout()
        row2 = QHBoxLayout()
        row1.setAlignment(Qt.AlignTop)

        # Add two horizontal to main layout
        main_vbox.addLayout(row1)
        # main_vbox.addItem(verticalSpacer1)
        main_vbox.addLayout(row2)

        # Create the endlager tank widget
        tankName=self.opcName + ':Tank'
        self.tank = EndlagerTank(tankName)
        self.tank.setLevel(50)

        # Create the thermometer widget
        thermometerName=self.opcName+':Thermometer'

        self.thermometer = EndThermometerWidget(thermometerName)
        self.thermometer.setTemperature(35)

        # Create the gauge widget
        gaugeName=self.opcName+':gauge'
        self.gauge = Gauge(gaugeName)
        self.gauge.setFixedSize(100,100)

        # Add the widgets to the rows
        row1.addWidget(self.tank)
        row1.addWidget(self.thermometer)
        row2.addWidget(self.gauge)

        # Add all the elements to the main layout and set it as the default layout
        self.setLayout(main_vbox)
    def update(self,inputs: dict):
        """method to update all objects in current tab periodically after reading the values in different thread

        :param inputs: tag values
        :type inputs: dict
        """
        objectList=[    #self.playbutton,
                        self.tank,
                        self.gauge,
                        self.thermometer
                    ]


        for o in objectList:
            #iterate over an update method that should be added to all faceplate objects similar to box object
            o.update1(inputs)
        

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Create a layout and group box for testing
    layout = QVBoxLayout()
    group_box = Endlager("Endlager", layout)

    # Create a main window and set the layout
    main_window = QWidget()
    main_window.setLayout(layout)

    main_window.show()

    sys.exit(app.exec_())
