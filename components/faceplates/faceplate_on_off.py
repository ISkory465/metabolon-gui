# Importing necessary modules
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

# Importing necessary components
from .faceplates_new import InfoField, InfoFieldDouble, Box


class OnOffButton(QWidget):
    """
    A Widget that represents an On/Off button with a label.
    """
    
    def __init__(self):
        super().__init__()

        # Widget's title
        self.setWindowTitle('On/Off Button')

        # Setting up User Interface
        self.initUI()
    
    def initUI(self):
        # Creating a label
        self.label = QLabel("User input")
        self.label.setAlignment(Qt.AlignCenter) # Moving the label to the center

        # Creating the On/Off button
        self.button = QPushButton('Locked', self) # Default state
        self.button.setCheckable(True)  # Making button checkable
        self.button.clicked.connect(self.on_off_clicked)  # Connecting button click event to the handler

        # Setting up the font for the button
        font = QFont()
        font.setBold(True)
        self.button.setFont(font)

        # Setting initial button style
        self.update_button_style()

        # Creating a layout and adding widgets to it
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)

        # Setting the layout for this widget
        self.setLayout(layout)

    def update_button_style(self):
        """
        Updates the style of the button based on its state.
        """
        if self.button.isChecked():
            self.button.setText('Unlocked')
            self.button.setStyleSheet('QPushButton { color: green; }')
        else:
            self.button.setText('Locked')
            self.button.setStyleSheet('QPushButton { color: red; }')

    def on_off_clicked(self):
        """
        Event handler for button click event. 
        Toggles the state of the button and updates the button style.
        """
        self.update_button_style()

        # Getting the current state of the button
        state = self.button.isChecked()  # True if button is 'ON', False if 'OFF'

        # Updating the state of all info fields and boxes by locking/unlocking them
        InfoField.set_all_states(state)
        InfoFieldDouble.set_all_states(state)
        Box.set_all_states(state)


