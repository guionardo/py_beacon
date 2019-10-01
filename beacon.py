# Python beacon
# UDP responder to broadcast

import json
import socket
import sys
import time
from pprint import pprint

import netifaces

UDP_PORT = 37020
hostname = socket.gethostname()
BEACON = "beacon" in sys.argv


def get_ips():
    ips = []
    for interface in netifaces.interfaces():
        if interface != 'lo' and netifaces.AF_INET in netifaces.ifaddresses(interface):
            for ip in netifaces.ifaddresses(interface)[netifaces.AF_INET]:
                if ip['addr'] not in ('127.0.0.1', '0.0.0.0'):
                    ips.append(ip['addr'])

    # pprint(ips)
    return ips


def run_beacon():
    print(f"Beacon - listening on {UDP_PORT} UDP port")
    print(f"I´m {hostname}:{ips}")
    me = json.dumps({
        "beacon": hostname,
        "ips": ips
    })
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
    client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    client.bind(("", UDP_PORT))
    while True:
        data, addr = client.recvfrom(1024)
        if data:
            print(f"ping from {addr}")
            sent = client.sendto(me.encode('ascii'), addr)
            print(f"Responding {me}")


def run_client():
    print(f"Beacon - searching in {UDP_PORT} UDP port: ", end='')
    server = socket.socket(
        socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    # Set a timeout so the socket does not block
    # indefinitely when trying to receive data.

    server.bind(("", 44444))
    found = False
    t0 = time.time()
    while not found and time.time()-t0 < 10:
        print('.', end='')
        server.settimeout(0.2)
        server.sendto(b"hi", ('<broadcast>', UDP_PORT))
        server.settimeout(1)
        try:
            data, addr = server.recvfrom(1024)
            print(str({'data': data, 'addr': addr}))
            found = True
        except:
            pass

    if not found:
        print('Beacon not found!')


ips = get_ips()

if BEACON:
    run_beacon()
else:
    run_client()
