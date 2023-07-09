import asyncio
from database.Database_Handler import DatabaseHandler
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QTimer
from ..widgets.infofield_dbl import InfoField

#TODO: fix issue with tuple index ouf of tange during update of database

class Page(QWidget):
    fields = {
        'HE11_BH': {
            'value': None,
            'table': 'opcdb78',
            'column': 'he11_bh'
        },
        'HE12_BH': {
            'value': None,
            'table': 'opcdb78',
            'column': 'he12_bh'
        },
        'HE21_BH': {
            'value': None,
            'table': 'opcdb78',
            'column': 'he21_bh'
        },
        # Add more fields as needed
    }
     
    def __init__(self) -> None:
        super().__init__()
        self.UI()
        db_handler = DatabaseHandler()
        #db_handler.insert_record('opcdb78', '10')
        
        self.setup_database_update()

    def UI(self):
        # Main layout of the first tab 'Betriebsstunden"
        grid = QGridLayout() 

        # Page has 2 horizontal boxes; hbox1 contains 2 vertical layouts vbox1_1 and vbox1_2:       
        hbox1 = QHBoxLayout()     
        vbox1_1 = QVBoxLayout()
        vbox1_2 = QVBoxLayout()

        # hbox2 contains 3 vertical layouts vbox2_1, vbox2_2 and vbox2_3:
        hbox2 = QHBoxLayout() 
        vbox2_1 = QVBoxLayout()
        vbox2_2 = QVBoxLayout()
        vbox2_3 = QVBoxLayout()

        # Layout relation 
        vbox2_3.setAlignment(Qt.AlignTop)

        hbox1.addLayout(vbox1_1)
        hbox1.addLayout(vbox1_2)

        hbox2.addLayout(vbox2_1)
        hbox2.addLayout(vbox2_2)
        hbox2.addLayout(vbox2_3)

        # Layout settings 
        hbox1.setAlignment(Qt.AlignTop)
        hbox1.setSpacing(5)

        hbox2.setAlignment(Qt.AlignTop)
        hbox2.setSpacing(5)

        grid.setAlignment(Qt.AlignCenter)
        grid.setSpacing(50)


        # Elements of vbox1_*:
        self.field1_1 = InfoField(name="HE11_BH", dec_num=2)
        vbox1_1.addWidget(self.field1_1)
        self.field1_2 = InfoField(name="HE12_BH", dec_num=0)
        vbox1_1.addWidget(self.field1_2)
        self.field1_3 = InfoField(name="HE21_BH", dec_num=0)
        vbox1_2.addWidget(self.field1_3)
        self.field1_4 = InfoField(name="HE22_BH", dec_num=0)
        vbox1_2.addWidget(self.field1_4)

        # Elements of vbox2_*:
        self.field2_1 = InfoField(name="PU11_BH", dec_num=3)
        vbox2_1.addWidget(self.field2_1)
        self.field2_2 = InfoField(name="PU12_BH", dec_num=4)
        vbox2_1.addWidget(self.field2_2)
        self.field2_3 = InfoField(name="PU21_BH")
        vbox2_2.addWidget(self.field2_3)
        self.field2_4 = InfoField(name="PU22_BH", dec_num=4)
        vbox2_2.addWidget(self.field2_4)
        self.field2_5 = InfoField(name="PU31_BH", dec_num=4)
        vbox2_3.addWidget(self.field2_5)
    
        
        # Assign the field values to the fields dictionary
        self.fields['HE11_BH']['value'] = self.field1_1.getValue()
        self.fields['HE12_BH']['value'] = self.field1_2.getValue()
        self.fields['HE21_BH']['value'] = self.field1_3.getValue()
        print(self.fields)
    
        # Grid layout  
        grid.addLayout(hbox1, 1, 0)
        grid.addLayout(hbox2, 1, 1)

        # Assigning to the tab
        self.setLayout(grid)
        
       

    def update_fields(self):
        # Iterate over the fields dictionary
        for field_name, field_info in self.fields.items():
            # Get the current value of the field
            field_value = field_info['value']
            value = field_value.getValue()
            # Call the update_database method to update the value in the database
            self.update_database(field_info['table'], field_info['column'], value, field_name)
    
    def insert_fields(self):
    # Create a dictionary to hold the column-value pairs
        record = {}

    # Iterate over the fields dictionary
        for field_name, field_info in self.fields.items():
            # Get the current value of the field
            field_value = field_info['value']
            value = field_value

             # Add the column-value pair to the record dictionary
            record[field_info['column']] = value
            print(record)

             # Call the insert_record method to insert the record into the database
            self.db_handler.insert_record(field_info['table'], record)
    
    
    def setup_database_update(self):
        # Instantiate the DatabaseHandler
        self.db_handler = DatabaseHandler()

        # Create a QTimer for periodic updates
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.insert_fields)
        self.timer.start(0.3 * 60 * 1000)  # 5 minutes in milliseconds
        
    def setup_database_insert(self):
        # Instantiate the DatabaseHandler
        self.db_handler = DatabaseHandler()

        # Create a QTimer for periodic updates
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_fields)
        self.timer.start(0.3 * 60 * 1000)  # 5 minutes in milliseconds    

    def update_database(self, field_name, value, table_name, column_name):
        # Perform the database update asynchronously
        asyncio.ensure_future(self.db_handler.update_record(table_name, column_name, value, f"{field_name} = %s"))
        

    def closeEvent(self, event):
        # Stop the timer and close the database connection when the UI is closed
        self.timer.stop()
        self.db_handler.close_connection()
        super().closeEvent(event)

    

    def updateAll(self, inputs: dict):
        """method to update all objects in current tab periodically after reading the values in different thread

        :param inputs: tag values
        :type inputs: dict
        """
        objectList = [
            self.field1_1,
            self.field1_2,
            self.field1_3,
            self.field1_4,

            self.field2_1,
            self.field2_2,
            self.field2_3,
            self.field2_4,
            self.field2_5
        ]

        for o in objectList:
            # iterate over an update method that should be added to all faceplate objects similar to box object
            o.update(inputs)
        

if __name__=='__main__':
    
    pass
