from tkinter.font import names
import OpenOPC
import time

import pywintypes

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


  

  




