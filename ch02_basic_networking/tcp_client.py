# import socket

# target_host = "www.google.com"
# target_port = 80

# # Buat objek socket (IPv4, TCP)
# client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# # Hubungkan ke target
# client.connect((target_host, target_port))

# # Kirim permintaan HTTP GET
# client.send(b"GET / HTTP/1.1\r\nHost: www.google.com\r\n\r\n")

# # Terima respons (buffer 4096 bytes)
# response = client.recv(4096)

# print(response.decode())

# # Tutup koneksi
# client.close()

import socket

target_host = "www.google.com"
target_port = 80

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((target_host, target_port))

request = f"GET / HTTP/1.1\r\nHost: {target_host}\r\n\r\n"

client.send(request.encode())


response = client.recv(4096)
print(response.decode())