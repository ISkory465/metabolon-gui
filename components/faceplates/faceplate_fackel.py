import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

# from faceplates_new import InfoField, Box
from components.faceplates.faceplates_new import InfoField, Box

class Indicator(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAlignment(Qt.AlignCenter)
        self.setStyleSheet("border: 1px solid black; background-color: blue;")  # Default idle state
        self.setFixedSize(20, 100)  # Change this according to your desired size

    def set_state(self, state):
        if state == 'active':
            self.setStyleSheet("border: 1px solid black; background-color: green;")
        elif state == 'idle':
            self.setStyleSheet("border: 1px solid black; background-color: blue;")
        elif state == 'error':
            self.setStyleSheet("border: 1px solid black; background-color: red;")
        else:
            print(f'Unknown state: {state}')


class FackelBox(QGroupBox):
    def __init__(self, name, layout, opcID=None):
        super().__init__(name)

        main_vbox = QHBoxLayout()  # Main layout
        self.setLayout(main_vbox)

        # Two main horizontal layouts
        col1 = QVBoxLayout()
        col2 = QVBoxLayout()
        col3 = QVBoxLayout()

        main_vbox.addLayout(col1)
        main_vbox.addLayout(col2)
        main_vbox.addLayout(col3)

        # Create InfoField instances and add them to row1
        self.fackel_fer1 = InfoField(name="Fackel Ein \nFer1 [mbar]", layout=col1, buttonSymbol=1)
        self.fackel_fer2 = InfoField(name="Fackel Ein \nFer2 [mbar]", layout=col1, buttonSymbol=1)
        self.fackel_s = InfoField(name="[s]", layout=col1)

        # Create fackel indicator
        self.indicator = Indicator()
        col2.addWidget(self.indicator)


        # Fackel controls
        self.fackel_controls = Box("Control mode", layout=col3, horizontal_spacing=10, width=100)

        # Add the group box to parent layout
        layout.addWidget(self)






if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Create a layout and group box for testing
    layout = QVBoxLayout()
    group_box = FackelBox("Fackel", layout)

    group_box.indicator.set_state('active')  # or 'idle' or 'error'


    # Create a main window and set the layout
    main_window = QWidget()
    main_window.setLayout(layout)

    main_window.show()

    sys.exit(app.exec_())