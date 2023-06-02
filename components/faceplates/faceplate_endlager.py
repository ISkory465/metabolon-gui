from PyQt5.QtWidgets import QApplication, QGroupBox, QVBoxLayout, QHBoxLayout, QWidget
from .faceplate_therm import ThermometerWidget
from .faceplate_gauge import Gauge
from .faceplate_endlager_tank import EndlagerTank
import sys


class Endlager(QGroupBox):
    def __init__(self, name, layout, opcID=None):
        super().__init__(name)
        self.layout = layout

        # Main layout for 2 horizontal boxes representing each row
        main_vbox = QVBoxLayout()
        main_vbox.setSpacing(50)

        # Two main horizontal layouts
        row1 = QHBoxLayout()
        row2 = QHBoxLayout()


        main_vbox.addLayout(row1)
        main_vbox.addLayout(row2)

        # Create the endlager tank widget
        tank = EndlagerTank()
        tank.setLevel(50)

        # Create the thermometer widget
        thermometer = ThermometerWidget()
        thermometer.setTemperature(35)

        # Create the gauge widget
        gauge = Gauge()

        # Add the widgets to the rows
        row1.addWidget(tank)
        row1.addWidget(thermometer)
        row2.addWidget(gauge)

        self.layout.addWidget(self)
        self.setLayout(main_vbox)


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