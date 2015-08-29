#-*- coding:utf-8 -*-
import time, threading
from SocketServer import TCPServer, BaseRequestHandler
import traceback
from PythonSocketBBS import SocketServerBBS

def loop(a):
    print 'thread is running...'
    # 
    time.sleep(1)
    a.serve_forever()
    print 'thread ended.'

def socketMethod():
    print 'Method is running...'
    hostname=""
    port=9996
    print port
    a=SocketServerBBS.PythonChatServer((hostname,port),SocketServerBBS.RequestHandler)
    t = threading.Thread(target=loop,args=(a,))
    t.start()
    while 1:
        time.sleep(1)
        b=SocketServerBBS.Sclose()
        print b
        print (1==b)
        if (1==b):
            print 'close'
            a.shutdown()
            a.server_close()
            break
    # t.join()
    print 'Method ended.'

if __name__ == "__main__":
    socketMethod()