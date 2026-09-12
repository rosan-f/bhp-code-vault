import sys
import socket
import threading


HEX_FILTER = ''.join(
    [chr(i) if len(repr(chr(i))) == 3 else '.' for i in range(256)]
)

def hexdump(src, length=16, show=True):
    if isinstance(src, bytes):
        src = src.decode()

    result = list()
    for i in range(0, len(src), length):
        word = str(src[i:i+length])

        printable = word.translate(HEX_FILTER)
        hexa = ' '.join([f'{ord(c):02X}' for c in word])
        hexwidht = length*3
        result.append(f'{i:04X} {hexa:<{hexwidht}} {printable}')

    if show:
        for line in result:
            print(line)

    else:
        return result


def receive_from(connection):
    buffer = b""
    connection.settimeout(5)
    try:
        while True:
            data = connection.recv(4096)
            if not data:
                break
            buffer += data
    except Exception as e:
        pass
    return buffer