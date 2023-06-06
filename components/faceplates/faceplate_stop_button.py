import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel
from PyQt5.QtGui import QFont



class STOPButton(QWidget):
    
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.initUI()

    def initUI(self):
        self.setWindowTitle('STOP Button')
        
        # Email notification label
        self.label = QLabel(self.name)

        # Create the on/off button
        self.button = QPushButton('STOP', self)
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

    # def update_button_style(self):
    #     if self.button.isChecked():
    #         self.button.setText('STOPPED')
    #         self.button.setStyleSheet('QPushButton { color: black; background-color: red; }')
    #         # Do something when the button is turned on
    #     else:
    #         self.button.setText('STOP')
    #         self.button.setStyleSheet('QPushButton { color: red; }')
    #         # Do something when the button is turned off

    def update_button_style(self):
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

    def on_off_clicked(self):
        self.update_button_style()
        state = self.button.isChecked()  # True if button is 'ON', False if 'OFF'
        #add stopping function

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    window = STOPButton("Stop 1")
    window.show()
    sys.exit(app.exec_())
