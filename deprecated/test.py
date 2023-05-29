from PyQt5.QtWidgets import QWidget, QLabel
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QSpacerItem, QSizePolicy
from PyQt5.QtGui import QPainter, QColor, QPen, QFont, QFontMetrics
from PyQt5.QtCore import Qt, QRectF, QPoint, QRect, pyqtSignal
from PyQt5.QtWidgets import QPushButton

class ParentWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 400, 300)  # Set the size of the parent widget

        # Create the child widget (in this example, a QLabel)
        child_widget = QLabel(self)
        child_widget.setText("Child Widget")
        child_widget.setGeometry(200, 50, 200, 100)  # Set the position and size of the child widget

if __name__ == '__main__':
    app = QApplication(sys.argv)
    parent = ParentWidget()
    parent.show()
    sys.exit(app.exec_())