 This is The EventManager Calls , That Manage Communication
 Between A The remote socket server and The Python
 applications
 Use it :
 from EventManager import *
  
 class EventDb(Event):
     event_type ='Db'
     
     def __init__(self, lines):
         self.dict =[]
         
     def parse(self):
         for line in lines:
             if ',' not in lines
                 raise EventFormatError(
                     "This is an EventDb Line, each line should  end\
                      with %s\n"%line
                     )
             key, value = line.split(',', 1)
             if key in self.dict:
                 self.dict[key].append(
                      value.decode('utf-8')
                     )
                
 Fire The event
 mgr =EventDBManager()
 mgr.event_klass =EventDb
 ahndler = EventHandler()
 callback =lambda x: print 'Dump Packet :%s'%x
 handler.events = [{'test', callback}]

 while True:
        mgr.serve()
        mgr.monitor(
               error=True ,
               file ='data.log'
        )

 Note:
 ----
 Each EventXManager is responsible of Each Event Class , so
 For Exemple If you are managing An remote asterisk socket
 The Event data parser should split line with ':' separator
 And when you are Managing a DataBase Socket , The remote
 socket can map like with any  format , so The EventDb
 that herit  from  Event  should be defined to mutch the
 format of data sent by the remote socket

 Note:
 Chaque EventXManager  est responsable de la definition de
 la class Event , Par Exemple si vous etes entrain de manager
 un Asterisk server , le Event doit parser en splitant par ':'
 et si vous etes enrain de manager une base de donnees via
 toujours un socket , le EventDb qui herit de Event doit
 etre defini afin de pouvoir correspondre avec le format
 des donnees envoye par le socket [tableaux, separateur,...]

 __autor__="Alioune Dia"
 __Date__ ="2012-11-21"
