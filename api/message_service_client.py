#
from thrift.transport import TSocket
from thrift.protocol import TBinaryProtocol

class MessageServiceClient(object):
    def __init__(self):
        self.name = 'api.MessageServiceClient'

    def send_email(self, email_addr, msg):
        socket = TSocket.TSocket(host, port)
        protocol = TBinaryProtocol(transport)
        client = MessageServiceApi.Client(protocol)
        transport.open()
        client.send_email(email_addr, msg)
        transport.close()