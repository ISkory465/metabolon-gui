# Import necessary modules from PyQt5
from PyQt5.QtWidgets import QWidget, QVBoxLayout
from PyQt5.QtCore import Qt

# Import necessary components
from components.faceplates.faceplate_side_bar import SideBarFaceplate

class SideBar(QWidget):
    """
    SideBar is a QWidget that holds the sidebar of the application. 
    It contains the content of the Control Panel and any additional widgets added to it.
    """

    def __init__(self):
        super().__init__()

        # Set minimum width for the SideBar to make sure it is not compressed
        self.setMinimumWidth(400)

        # Create a QVBox main layout for SideBar
        self.sb_layout = QVBoxLayout()
        self.sb_layout.setAlignment(Qt.AlignTop)

        # Create the content of the Control Panel
        self.content = SideBarFaceplate(name="Control Panel", layout=self.sb_layout)

        # Add the side bar faceplate to the SideBar's layout
        self.sb_layout.addWidget(self.content)

        # Set the layout for the SideBar
        self.setLayout(self.sb_layout)