# py_beacon
Python network service discovery

## Usage

On discoverable:

``` shell
python beacon.py beacon
```

``` shell
Beacon - listening on 37020 UDP port
I´m NT-04267:['10.0.75.1', '192.168.17.140', '169.254.179.151', '172.17.249.129']

ping from ('10.0.75.1', 44444)
Responding {"beacon": "NT-04267", "ips": ["10.0.75.1", "192.168.17.140", "169.254.179.151", "172.17.249.129"]}
```

On finder:

``` shell
python beacon.py
```

``` shell
Beacon - searching in 37020 UDP port: ......{'data': b'{"beacon": "NT-04267", "ips": ["10.0.75.1", "192.168.17.140", "169.254.179.151", "172.17.249.129"]}', 'addr': ('10.0.75.1', 37020)}
```