# py-share-cups-printer
Python package with command line tool that simplify the sharing of a cups printer.
<br>It works on port 8090.

# Installation and Configuration:

Install it with pip:
```
pip install py-share-cups-printer
```

This provides the 'print' comman line tool that integrates both client and server implementations.
<br>Start the server ( on the machine that has cups and a printer connected ):
```
print -s
```
Note that this command can be executed when the OS starts up, and the daemon will be always active.

<br>
After that every client that has py-share-cups-printer installed can connect to this Server.
<br>A one-time configuration is needed before start:
```
print -c
```
This will ask for the Server IP address (local or global).

# Usage
On every configured machine, printing a document on a Server printer becomes easy:
```
print file_name
```

# Contribute
Fell free to contribute to this project.






  
