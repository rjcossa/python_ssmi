from app.settings import settings

class SSMIRequest:
    def __init__(self,command_id):
        self.command_id = command_id

class BindRequest(SSMIRequest):
    def __init__(self,username,password):
        SSMIRequest.__init__(self, settings['BIND_REQUEST'])
        self.username = username
        self.password = password

    def send(self):
        return "SSMI,{0},{1},{2}\r".format(self.command_id,self.username,
                                           self.password)

class AckResponse(SSMIRequest):
    def __init__(self,data):
        self.command_id = data[1]
        self.resp_type = data[2]

class USSDRequest(SSMIRequest):
    def __init__(self,type,msisdn,message):
        SSMIRequest.__init__(self,settings['USSD_REQUEST'])
        self.type = type
        self.msisdn = msisdn
        self.message  = message

    def update(self,msisdn,type,message):
        self.msisdn = msisdn
        self.type = type
        self.message = message

    def send(self):
        return "SSMI,{0},{1},{2},{3}\r".format(self.command_id,
                                               self.msisdn, self.type,
                                               self.message)

class USSDResponse(SSMIRequest):
    def __init__(self,data):
        SSMIRequest.__init__(self,data[1])
        self.msisdn = data[2]
        self.type = data[3]
        self.phase = data[4]
        self.genfields = data[5].split(':')
        self.message = data[6]
