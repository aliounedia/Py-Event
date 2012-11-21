from EventManager import *
class EventDb(Event):
    event_type ='Db'

    def __init__(self, lines):
        Event.__init__(self,lines)
        self.parse()
        # :) To match The fake date Files:)

    def parse(self):
        for line in self.lines:
         if  ',' in line:
             raise EventFormatError(
                 "No ',' For Db Inline "%line
                 )
         key, value = line.split(',', 1)
         self.args.append(
                  (key, value.decode('utf-8'))
                 )
         if key in self.kwargs:
            self.kwargs[k].append(line)
         else :
             self.kwargs[k]=line

class EventFake(Event):
    def __init__(self, lines):
        Event.__init__(self,lines)
        self.parse()
        # :) To match The fake date Files:)
        self.name ='test'
        self.args =lines
        
    def parse(self):
         return self.lines
        
         
host, port = 'localhost', 8085                
mgr =EventManager(host, port)
mgr.event_cls =EventFake
handler = EventHandler()


def callback(*args, **kwargs):
    print 'callbackargs', args
    print 'callbackkwargs', kwargs
     
handler.events = {'test': callback}
handler.register(mgr)

while True:
    mgr.serve()
    mgr.monitor(
           error=True ,
           file ='data.log'
    )
