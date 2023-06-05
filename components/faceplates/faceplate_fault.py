import sys
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QHBoxLayout, QLabel, QGroupBox, QWidget
from PyQt5.QtCore import Qt

class FaultBox(QGroupBox):
    def __init__(self, name, opcID=None):
        super().__init__(name)
        self.name = name

        # Main layout for 2 horizontal boxes representing each row
        main_vbox = QVBoxLayout()
        # Two main horizontal layouts
        row2 = QHBoxLayout()

        main_vbox.addLayout(row2)

        label = QLabel("Stoerung Quittieren")
        label.setAlignment(Qt.AlignCenter)

        main_vbox.addWidget(label)

        parent_layout.addWidget(self)
        self.setLayout(main_vbox)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QWidget()
    layout = QVBoxLayout(window)
    fault_box = FaultBox("Quittieren", layout)
    window.show()
    sys.exit(app.exec_())
