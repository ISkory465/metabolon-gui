import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt5.QtGui import QFont
from .faceplates_new import InfoField, InfoFieldDouble, Box



class OnOffButton(QWidget):
    
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('On/Off Button')
        
        # InfoField.set_all_states(False)

        # Create the on/off button
        self.button = QPushButton('Locked', self)
        self.button.setCheckable(True)  # Make the button checkable

        # Set the initial state to 'OFF'
        self.button.setChecked(False)
        self.button.clicked.connect(self.on_off_clicked)  # Connect the button's clicked signal to the handler

        # Customize the font for the button
        font = QFont()
        font.setBold(True)
        self.button.setFont(font)

        self.update_button_style()  # Set the initial button style

        # Create a layout and add the button to it
        layout = QVBoxLayout()
        layout.addWidget(self.button)

        self.setLayout(layout)

    def update_button_style(self):
        if self.button.isChecked():
            self.button.setText('Unlocked')
            self.button.setStyleSheet('QPushButton { color: green; }')
            # Do something when the button is turned on
        else:
            self.button.setText('Locked')
            self.button.setStyleSheet('QPushButton { color: red; }')
            # Do something when the button is turned off

    def on_off_clicked(self):
        self.update_button_style()
        state = self.button.isChecked()  # True if button is 'ON', False if 'OFF'
        InfoField.set_all_states(state)
        InfoFieldDouble.set_all_states(state)
        Box.set_all_states(state)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = OnOffButton()
    window.show()
    sys.exit(app.exec_())
