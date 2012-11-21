## This is The EventManager Calls , That Manage Communication
## Between A The remote socket server and The Python
## applications
## Use it :
## from EventManager import *
##  
## class EventDb(Event):
##     event_type ='Db'
##     
##     def __init__(self, lines):
##         self.dict =[]
##         
##     def parse(self):
##         for line in lines:
##             if ',' not in lines
##                 raise EventFormatError(
##                     "This is an EventDb Line, each line should  end\
##                      with %s\n"%line
##                     )
##             key, value = line.split(',', 1)
##             if key in self.dict:
##                 self.dict[key].append(
##                      value.decode('utf-8')
##                     )
##                
## Fire The event
## mgr =EventDBManager()
## mgr.event_klass =EventDb
## ahndler = EventHandler()
## callback =lambda x: print 'Dump Packet :%s'%x
## handler.events = [{'test', callback}]
##
## while True:
##        mgr.serve()
##        mgr.monitor(
##               error=True ,
##               file ='data.log'
##        )
##
## Note:
## ----
## Each EventXManager is responsible of Each Event Class , so
## For Exemple If you are managing An remote asterisk socket
## The Event data parser should split line with ':' separator
## And when you are Managing a DataBase Socket , The remote
## socket can map like with any  format , so The EventDb
## that herit  from  Event  should be defined to mutch the
## format of data sent by the remote socket
##
## Note:
## Chaque EventXManager  est responsable de la definition de
## la class Event , Par Exemple si vous etes entrain de manager
## un Asterisk server , le Event doit parser en splitant par ':'
## et si vous etes enrain de manager une base de donnees via
## toujours un socket , le EventDb qui herit de Event doit
## etre defini afin de pouvoir correspondre avec le format
## des donnees envoye par le socket [tableaux, separateur,...]

## __autor__="Alioune Dia"
## __Date__ ="2012-11-21"

import socket, time, threading 
class EventErrorFormat(Exception):
    def __init__(self, name, args):
      self.name =name
      self.args =args
      
      
    def __repr__(self):
      return self.name

class EventHandler(object):
    def __init__(self, events =None):
      self.events =events or None
      self.register_lock =threading.Lock()
      
    def register(self, mgr):
      
      with self.register_lock:
            self.mgr =mgr
            self.mgr.events_handler.append(self)
            
    def unregister(self, mgr):
      with self.register_lock: 
            self.mgr.events_handler.remove(self)
            
    def __len__(self):
      return len(self.events)

    def __repr(self):
      return  "\n".join(
            [ (name, callback) for name, callback in
                          self.events ])
    def __get__(self, name, default =None):
      return self.events.get(name, default)

    def __del__(self, name):
      del self.events[name]

    def is_empty(self):
      return not  len(self.vents)
       
class Event(object):
    def __init__(self, lines):
      self.name         =None
      self.lines        =lines
      self.args         =None
      self.kwargs       =None
      self.error_type   =None
      self.erro_details =None

    def __repr__(self):
      return "name | " % self.name 

class EventManager(object):
    def __init__(self,host, port):
     self.host = host
     self.port = port
     self.events =[]
     self.events_handler =[]
     self.events_error   =[]
     self.event_cls  =None
     self.boot()

    def boot(self):
     _sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     _sock.connect((self.host,self.port))
     self._sock = _sock.makefile ()
     _sock.close ()

    def serve(self):
     lines = []
     for line in self._sock :
         if not line :break
         lines.append(line)
     
     if lines:
         print 'lines', lines
         event = self.event_cls(lines)
         self.events.append(event)
         self.events_dispatch(event)

    def events_dispatch(self, event):
      for handler in self.events_handler:
            callback = handler.__get__(event.name, None)
            print 'Event Name' , event.name
            print 'Event args' , "\n".join(event.args)
            print  'Event callbackl', callback
            try:
                callback(event.name, event.args , event.kwargs)
            except Exception, why:
                event.error_type   =type(why)
                event.error_details=str(why)
                self.events_error.append(event)

    def __len__(self):
      return len(self.events)

    def monitor(self, error=True, file ='log.txt'):
      if hasattr(self, "events_error") and len(self.events_error):
          if not error: return
          t =time.time()
          with open(file, 'a') as log :
              while self.events_error:
                   event = self.events_error.pop()
                   error_name, error_type, error_details = event.name , event.error_type, event.error_details
                   log.write(
                        "time :%s , event.name :%s, event.error_type :%s , event.error_details :%s\n"%
                        (t, error_name, error_type,error_details))
          
            
         
         


