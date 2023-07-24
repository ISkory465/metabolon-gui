import psycopg2
from configparser import ConfigParser
import os

class ConfigDB:
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    @staticmethod
    def credential(filename=os.path.join(BASE_DIR, 'database', 'database.ini'), section='postgresql'):
        # Create a parser
        parser = ConfigParser()
        # Read the configuration
        parser.read(filename)
        db = {}
        if parser.has_section(section):
            params = parser.items(section)
            for param in params:
                db[param[0]] = param[1]
        else: 
            raise Exception('Section {0} is not found in the {1} file.' 
                            .format(section, filename))  
        return db

