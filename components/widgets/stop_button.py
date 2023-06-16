# Importing necessary modules
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel
from PyQt5.QtGui import QFont

class STOPButton(QWidget):
    """STOPButton is a custom QWidget that represents a toggleable STOP/STOPPED button.
    The button's style changes based on its current state.
    """
    
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.setup_ui()

    def setup_ui(self):
        # Set widget title
        self.setWindowTitle('STOP Button')

        # Initialize label
        self.label = QLabel(self.name)

        # Initialize button
        self.button = QPushButton('STOP')
        self.button.setCheckable(True)  # Make the button checkable
        self.button.setChecked(False)  # Set the initial state to 'OFF'
        self.button.setMinimumHeight(27)  # Height adjustments
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
            self.button.setText('STOPPED')
            self.button.setStyleSheet('''
                QPushButton { 
                    color: black; 
                    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                                    stop: 0 #ff0000, stop: 0.4 #ff6666,
                                                    stop: 0.5 #ff6666, stop: 1.0 #ff0000);
                    border: 2px solid black; 
                    border-radius: 5px;
                }
            ''')
        else:
            self.button.setText('STOP')
            self.button.setStyleSheet('''
                QPushButton { 
                    color: red; 
                    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                                    stop: 0 #eeeeee, stop: 0.4 #e4e4e4,
                                                    stop: 0.5 #dddddd, stop: 1.0 #d4d4d4);
                    border: 2px solid black; 
                    border-radius: 5px;
                }
            ''')

    def on_button_click(self):
        """Handle button click event."""
        self.update_button_style()

        # TODO: Call stopping function with the current state
        # state = self.button.isChecked()  # True if button is 'ON', False if 'OFF'
