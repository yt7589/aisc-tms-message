#
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

class MessageServiceClient(object):
    def __init__(self):
        self.name = 'api.MessageServiceClient'

    def send_email(self, email_addr, msg):
        host = 'localhost'
        port = '9900'
        socket = TSocket.TSocket(host, port)
        transport = TTransport.TFramedTransport(socket)
        protocol = TBinaryProtocol(transport)
        client = MessageServiceApi.Client(protocol)
        transport.open()
        client.send_email(email_addr, msg)
        transport.close()