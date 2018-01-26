import socket
from app.ussd.ssmi import (BindRequest, USSDRequest,
                           USSDResponse, AckResponse)
SERVER = "10.201.47.102"
PORT = 50017
USERNAME = "4cittest"
PASSWORD = "4c1tt3st"
MSISDN = "258849901374"

bind = BindRequest(username=USERNAME, password=PASSWORD)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER,PORT))
client.sendall(bytes(bind.send()))
in_data = client.recv(1024)
bind_resp = AckResponse(data=in_data.decode().split(','))
print bind_resp.resp_type
print("From Server:", in_data.decode())
ussd_req = USSDRequest(msisdn=MSISDN,type='1',message='*105*337#')
inp = "1"
while inp == "1":
    ussd_req = USSDRequest(msisdn=MSISDN,type='1',message='*105*337#')
    print ussd_req.send()
    client.sendall(bytes(ussd_req.send()))
    in_data = client.recv(1024)
    ussd_resp = USSDResponse(data=in_data.decode().split(','))
    print "Session ID %s" % ussd_resp.genfields[3]
    print("From Server 2:", in_data.decode())
    ussd_req.update(msisdn=MSISDN,type='2',message='Introduza o seu PIN')
    client.sendall(bytes(ussd_req.send()))
    in_data = client.recv(1024)
    print("From Server 3:", in_data.decode())
    TYPE="3"
    ussd_req.update(msisdn=MSISDN,type='3',
                                  message='Request has been submitted')
    client.sendall(bytes(ussd_req.send()))
    inp = raw_input()
client.close()
