import sys
import argparse
from .print_server import print_server
from .print_client import print_client
from .tools import configure
from .tools import assert_configuration


def main():

    # If one argument is given and it is different to -s or -c 
    # than start the client
    if len(sys.argv) > 1:
        file_name = str(sys.argv[1])
        print( "file_name", file_name )
        if file_name != "-c" and file_name != "-s":
            assert_configuration()
            print_client( file_name=file_name )
            sys.exit(0)

    # Configure parser
    parser = argparse.ArgumentParser()

    parser.add_argument('-c', action='store_true', default=False,
                        dest='configure',
                        help='[ CLIENT ] Set the server address')

    parser.add_argument('-s', action='store_true', default=False,
                        dest='launch_server',
                        help='[ SERVER ] Launch the listener server')

    parser.add_argument('-v', '--version', action='version', version='%(prog)s 0.1')

    # if no args are given, show help
    if len(sys.argv) < 2:
        parser.print_help()
        sys.exit(0)

    # If there are some options, parse them
    options = parser.parse_args()

    # Chech if the parsed options are True
    if options.configure is True:
        configure()
        sys.exit(0)

    if options.launch_server is True:
        print_server()
        sys.exit(0)


if __name__ == "__main__":
    main()
