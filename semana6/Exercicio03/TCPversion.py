import socket
import sys

TCP_IP = "127.0.0.1"
FILE_PORT = 5005
DATA_PORT = 5006
buf = 1024
file_name = sys.argv[1]

f = None  # Defina a variável f aqui para evitar o erro NameError

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((TCP_IP, FILE_PORT))
    sock.send(file_name.encode())  # Codifique o nome do arquivo antes de enviar
    sock.close()

    print("Sending %s ..." % file_name)

    f = open(file_name, "rb")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((TCP_IP, DATA_PORT))
    data = f.read()
    sock.send(data)

finally:
    if f:
        f.close()
    sock.close()
