import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

# from faceplates_new import InfoField, Box
from .faceplates_new import InfoField, Box



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

        # Create InfoField instances and add them to row1
        self.fackel_fer1 = InfoField(name="Fackel Ein \nFer1 [mbar]", layout=col1, buttonSymbol=1)
        self.fackel_fer2 = InfoField(name="Fackel Ein \nFer2 [mbar]", layout=col1, buttonSymbol=1)
        self.fackel_s = InfoField(name="[s]", layout=col1)

        # Create

        # Fackel controls
        self.fackel_controls = Box("Fackel", layout=col2, horizontal_spacing=10, width=100)

        # Add the group box to parent layout
        layout.addWidget(self)






if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Create a layout and group box for testing
    layout = QVBoxLayout()
    group_box = FackelBox("Fackel", layout)

    # Create a main window and set the layout
    main_window = QWidget()
    main_window.setLayout(layout)

    main_window.show()

    sys.exit(app.exec_())