
from   socket import *
class Fake(object):
     def __init__(
         self, host, port, max , fake =open('FakeDATA.txt')):
         self.host =host
         self.port =port
         self.max  =max or 20
         self.fake =fake
         self.main()

     def main(self):
        s = socket(AF_INET, SOCK_STREAM)
        s.bind((self.host, self.port))
        s.listen(self.max)
        while True:
            conn, (remotehost, remoteport) = s.accept()
            print('connection from', remotehost, remoteport)
            #conn.send('test')
            for line in  self.fake.readlines():
                print 'line', line 
                conn.send(line.encode('utf-8'))
            conn.close()

if __name__=="__main__":
    host, port, max , fake = '', 8085 , 20, open('FakeDATA.txt')
    print 'Fake server is running '
    Fake(host, port, max , fake )
         

