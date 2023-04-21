import socket 

host='localhost'
psot=50080

client =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((host.port))

while True:
    data=client.recv(1024)

    if data:
        text=data.decode('utf-8')
        print(text)

client.close()

