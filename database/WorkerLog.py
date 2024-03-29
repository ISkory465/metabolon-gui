import sys
from PyQt5.QtWidgets import *
import OpenOPC
import pywintypes
from PyQt5.QtCore import *
pywintypes.datetime = pywintypes.TimeType
import json
from database.Database_Handler import DatabaseHandler

class WorkerLog(QObject):
    finished = pyqtSignal()
    progress = pyqtSignal(dict)
    #recieved = pyqtSignal(list)
    
    def __init__(self, x:dict):
      self.varDict=x
      #self.client=client
      super().__init__()

    def run(self):
        """Long-running task."""
        #self.recieved.connect(self.rec)
        try:
            opc=OpenOPC.client() 
            opc.connect("OPC.SimaticNET")

            if self.varDict=={}:
                results={'Result':'No Values'}
                print(results)
            else:
                results={}
                keys=self.varDict.keys()
                db = DatabaseHandler()
                for x in keys:
                    #print(self.varDict[x])
                    tagValues=opc[self.varDict[x]]
                    results[x]=tagValues
            #print(results)
            db.insert_record('logging', results)   
            print(results)
            opc.close()
            self.finished.emit()
        except Exception as e:
            print('error in DB')
            print(str(e))
            x=['thread not working']
            self.finished.emit()