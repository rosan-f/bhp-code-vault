import socket

target_host = "127.0.0.1"
target_port = 9998

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((target_host, target_port))

request = f"GET / HTTP/1.1\r\nHost: {target_host}\r\n\r\n"

client.send(request.encode())

response = client.recv(4096)
print(response.decode())