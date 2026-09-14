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

def proxy_habdler(client_socket, remote_host, remote_port, receive_first):
    remote_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    remote_socket.connect((remote_host, remote_port))

    if receive_first:
        remote_buffer = receive_form(remote_socket)
        hexdump(remote_buffer)

    while True:
        local_buffer = receive_from(client_socket)
        if len(local_buffer):
            line = "[==>] Received %d bytes from localhost." % len(local_buffer)
        print(line)
        hexdump(local_buffer)

        local_buffer = request_handler(local_buffer)
        remote_socket.send(local_buffer)
        print("[==>] sent to remote")

        remote_buffer = receive_from(remote_socket)
        if len(remote_buffer):
            print("[==>] Received %d bytes to localhost. " % len(local_buffer))
            print(line)
            hexdump(local_buffer)

            local_buffer = request_handler(local_buffer)
            remote_socket.send(local_buffer)
            print("[==>] sent to remote.")

            remote_buffer = receive_from(remote_socket)
            if len(remote_buffer):
                print("[<==] Received %d bytes from remote." % len(remote_buffer))
                hexdump(local_buffer)

                remote_buffer = response_handler(remote_buffer)
                client_socket.send(remote_buffer)
                print("[<==] sent to localhost")

            if not len(local_buffer) or not len(remote_buffer):
                client_socket.close()
                remote_socket.close()
                print("[*] No more data. Closing connections")
                break

