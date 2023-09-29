from tkinter.font import names
import OpenOPC
import time

import pywintypes
from PyQt5.QtWidgets import *
import OpenOPC
from PyQt5.QtCore import *
pywintypes.datetime = pywintypes.TimeType

class OPC_Client:
  #client=Variable
  #serverList=list
  def __init__(self):
    self.client=OpenOPC.client()
    self.serverList=self.client.servers()

  
  def servernames(self):
    names=self.serverList
    return names
  

  def start_connection(self,x):
    try:
      self.client.connect(x)
    except:
      print('Connection unsuccessful')
  
  def close_connection(self):
    self.client.close()
  
  def listValues(self):
    list1=self.client.list()
    return list1

  def listValues2(self,l):
    list1=self.client.list(l)
    return list1
  
  def R(self,parameter):
    #string1=prefix+"."+parameter
    value=self.client[parameter]
    return value
  
  def Wr(self,parameter,value):
    self.client.write(parameter,value)

  def getInfo(self):
    infoList=self.client.info()
    infoDict=dict(infoList)
    return infoDict


  

  


class Worker(QObject):
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
            #print('client')   
            opc.connect("OPC.SimaticNET")

            if self.varDict=={}:
                results={'Result':'No Values'}
                print(results)
            else:
                results={}
                keys=self.varDict.keys()
                for x in keys:
                    #print(self.varDict[x])
                    tagValues=opc[self.varDict[x]]
                    #print(tagValues)
                    #tagValues=str(tagValues)
                    results[x]=tagValues
            
            #print(results)

            
            #print(self.x)
            self.progress.emit(results)
            opc.close()
            self.finished.emit()
        except:
            print('error')
            x=['thread not working']
            #self.progress.emit(x)
            self.finished.emit()


