'''
    Simple socket server using threads
'''

import socket
import socketserver
import sys
from threading import Thread
import cups

class service( socketserver.BaseRequestHandler ):

    def handle( self ):
        f = open('toPrint', 'wb')

        while True:
            self.data = self.request.recv( 65536 )
            if not self.data:
                break
            
            f.write( self.data )

            print("{} wrote:".format( self.client_address ))
            print( self.data )
            
            #self.request.sendall( self.data )
        f.close()
        # stampo
        conn = cups.Connection()
        printers = conn.getPrinters()
        conn.printFile(list(printers.keys())[0], 'toPrint', 'Title of the print', {})


class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass


def print_server():
    HOST = socket.gethostbyname(socket.gethostname())
    PORT = 8090

    server = ThreadedTCPServer(( HOST, PORT ), service )
    server.serve_forever()