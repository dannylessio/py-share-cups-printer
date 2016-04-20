from os.path import expanduser
import sys
import pickle
import os

home = expanduser("~")
pkl_file_path = os.path.join( home, '.print.conf.pkl' )


def configure():
	# Read abs path from stdin
    abs_path = input("Enter the server address that has a connected printer and a \"print -s\" server running")
    try:
        stored = { 'server_address' : abs_path }

        # Write this path on file in binary mode, Overwrites the file if it exists.
        f = open( pkl_file_path, "wb" )
        pickle.dump( stored, f )
        f.close()

        print("Cofiguration success.")

    except:
        print("Configuration error.")
        sys.exit(1)


def assert_configuration():
    try:
        f = open( pkl_file_path, "rb" )
        f.close()
    except:
        print("Please run -c option first.\n")
        sys.exit(1)