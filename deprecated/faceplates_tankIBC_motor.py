from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QApplication, QGroupBox, QSizePolicy
from PyQt5.QtGui import QPainter, QColor, QPen, QBrush
from ..components.faceplates.faceplate_tankibc import TankIBC
from ..components.faceplates.faceplate_motor import MotorWidget, MotorLabelWidget
import sys



class TankMotor(QGroupBox):
    def __init__(self, nameTank, nameMotor, modeMotor, maxTank, minTank, opcID=None):
        super().__init__(nameTank)

        # Remove margins
        self.setContentsMargins(0, 0, 0, 0)

        # Set fixed size
        self.setFixedSize(200, 300)

        # Main layout for 2 horizontal boxes representing each row
        main_vbox = QVBoxLayout()
        main_vbox.setSpacing(0)  # Adjust the spacing between rows
        main_vbox.setContentsMargins(0, 0, 0, 0)  # Remove contents margins

        # Two main horizontal layouts
        row1 = QHBoxLayout()
        row2 = QHBoxLayout()
        row1.setContentsMargins(0, 0, 0, 0)  # Remove contents margins
        row2.setContentsMargins(0, 0, 0, 0)  # Remove contents margins

        main_vbox.addLayout(row1)
        main_vbox.addLayout(row2)
        main_vbox.setSpacing(0)

        # Create motor widget
        motor = MotorLabelWidget(nameMotor, size=60)  # Adjust the size of the motor widget
        motor.set_mode(modeMotor)

        # Create tankIBC
        tankIBC = TankIBC(nameTank, max_level=maxTank, min_level=minTank)

        # Add the widgets to the rows
        row1.addWidget(motor)
        row2.addWidget(tankIBC)

        self.setLayout(main_vbox)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Create a layout and group box for testing
    layout = QVBoxLayout()
    group_box = TankMotor(name="Tank", maxTank=100, minTank=20, modeMotor="idle")

    layout.addWidget(group_box)  # Add the tank widget to your main UI layout

    # Create a main window and set the layout
    main_window = QWidget()
    main_window.setLayout(layout)

    main_window.show()

    sys.exit(app.exec_())

