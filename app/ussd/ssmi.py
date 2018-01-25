import settings from app.settings
class SSMIRequest:
    def __init__(self,command_id):
        self.command_id = command

class USSDRequest(SSMIRequest):
    def __init__(self,command_id,type,msisdn,message):
        SSMIRequest.__init__(self,command_id)
        self.type = type
        self.msisdn = msisdn
        self.message  = message

    def send():
        return "SSMI,{0},{1},{2},{3}\r"
