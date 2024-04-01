import sys
from messages import *


def get_ip_type(hostname):
    addr = socket.getaddrinfo(hostname, None)[0][4][0]
    try:
        socket.inet_pton(socket.AF_INET6, addr)
        return socket.AF_INET6
    except socket.error:
        pass

    try:
        socket.inet_pton(socket.AF_INET, addr)
        return socket.AF_INET
    except socket.error:
        pass

    return None


if len(sys.argv) < 4:
    print("Usage: python client.py <host> <port> <command> <...args>")
    exit()

host = str(sys.argv[1]).strip()
port = int(sys.argv[2])
cmd = str(sys.argv[3]).strip()

if not (cmd in COMMANDS.keys()):
    print("Invalid command. Commands:")
    [print("\t", i) for i in COMMANDS.keys()]

ip_type = get_ip_type(host)
if not ip_type:
    print("Invalid ip!")
    exit()

s = socket.socket(
    ip_type,
    socket.SOCK_DGRAM,
)
s.settimeout(60)

try:
    s.connect((host, port))
except Exception as e:
    print(e)
    s.close()
    exit()

COMMANDS[cmd](s, sys.argv)

s.shutdown(1)
s.close()
