import socket
import ssl
import sys

port = 443
hostname = sys.argv[1]

context = ssl.create_default_context() 
with socket.create_connection((hostname, port)) as sock:
    with context.wrap_socket(sock, server_hostname=hostname) as ssock:
        print(ssock.version())


