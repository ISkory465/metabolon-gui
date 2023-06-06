# Importing necessary modules
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt


class EmailButton(QWidget):
    """
    EmailButton is a custom QWidget that represents a toggleable on/off button.
    This button is used to control whether email notifications are on or off.
    """
    
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        # Set widget title
        self.setWindowTitle('Email Button')

        # Initialize label
        self.label = QLabel("Email Notifications ON/OFF")
        self.label.setAlignment(Qt.AlignCenter) # Moving the label to the center

        # Initialize button
        self.button = QPushButton('OFF')
        self.button.setCheckable(True)  # Make the button checkable
        self.button.setChecked(False)  # Set the initial state to 'OFF'
        self.button.clicked.connect(self.on_button_click)  # Connect the button's clicked signal to the handler

        # Set font for the button
        font = QFont()
        font.setBold(True)
        self.button.setFont(font)

        # Update button style for the first time
        self.update_button_style()

        # Create a layout and add widgets to it
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)

        # Set layout for this widget
        self.setLayout(layout)

    def update_button_style(self):
        """Update the text and style of the button based on its current state."""
        if self.button.isChecked():
            self.button.setText('ON')
            self.button.setStyleSheet('QPushButton { color: green; }')
        else:
            self.button.setText('OFF')
            self.button.setStyleSheet('QPushButton { color: red; }')

    def on_button_click(self):
        """Handle button click event."""
        self.update_button_style()

        # TODO: Call email function with the current state
        # state = self.button.isChecked()  # True if button is 'ON', False if 'OFF'

