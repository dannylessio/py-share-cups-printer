import socket
import pickle
import os
from .tools import pkl_file_path

def print_client( file_name ):
	
	if os.path.isfile( file_name ) is False:
		print( "File does not exist" )
		return False

	# read from pickle
	f = open( pkl_file_path, "rb")
	readed = pickle.load( f )
	f.close()

	# get server address from pickle
	server_address = readed['server_address']

	# send the file
	file = open( file_name, "rb")
	sock = socket.socket()
	sock.connect(( server_address, 8090 ))

	while True:
	    chunk = file.read( 65536 )
	    if not chunk:
	        break  # EOF
	    sock.sendall( chunk )

	print("Successfully sent to the server.")
	return True