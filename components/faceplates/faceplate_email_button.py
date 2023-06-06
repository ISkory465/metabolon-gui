import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel
from PyQt5.QtGui import QFont



class EmailButton(QWidget):
    
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Email Button')
        
        # Email notification label
        self.label = QLabel("Email Notifications ON/OFF")

        # Create the on/off button
        self.button = QPushButton('OFF', self)
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
        layout.addWidget(self.label)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def update_button_style(self):
        if self.button.isChecked():
            self.button.setText('ON')
            self.button.setStyleSheet('QPushButton { color: green; }')
            # Do something when the button is turned on
        else:
            self.button.setText('OFF')
            self.button.setStyleSheet('QPushButton { color: red; }')
            # Do something when the button is turned off

    def on_off_clicked(self):
        self.update_button_style()
        state = self.button.isChecked()  # True if button is 'ON', False if 'OFF'
        #add email function

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = EmailButton()
    window.show()
    sys.exit(app.exec_())
