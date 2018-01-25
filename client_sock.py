import socket
SERVER = "10.201.47.102"
PORT = 50017
USERNAME = "4cittest"
PASSWORD = "4c1tt3st"
MSISDN = "258849901374"

connection_string = "SSM1,1,{0},{1}\r".format(USERNAME,PASSWORD)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER,PORT))
client.sendall(bytes(connection_string))
in_data = client.recv(1024)
print("From Server:", in_data.decode())
inp = "1"
while inp == "1":
    TYPE = "1"
    MESSAGE="*105*337#"
    send_push = "SSM1,110,{0},{1},{2}\r".format(MSISDN,TYPE,MESSAGE)
    client.sendall(bytes(send_push))
    in_data = client.recv(1024)
    print("From Server 2:", in_data.decode())
    TYPE="2"
    MESSAGE="Introduza o seu PIN"
    send_push="SSM1,110,{0},{1},{2}\r".format(MSISDN,TYPE,MESSAGE)
    client.sendall(bytes(send_push))
    in_data = client.recv(1024)
    print("From Server 3:", in_data.decode())
    TYPE="3"
    MESSAGE="REQUESTED METHOD IS UNAVAILABLE"
    send_push="SSM1,110,{0},{1},{2}\r".format(MSISDN,TYPE,MESSAGE)
    client.sendall(bytes(send_push))
    inp = raw_input()
client.close()
