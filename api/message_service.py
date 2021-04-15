#
from api import MessageServiceApi
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

class MessageService(object):
    def __init__(self):
        self.name = 'api.MessageService'

    def startup(self):
        print('启动Thrift消息服务器')
        processor = MessageServiceApi.Processor(self)
        transport = TSocket.TServerSocket('localhost', '9900')
        tfactory = TTransport.TFramedTransportFactory()
        pfactory = TBinaryProtocol.TBinaryProtocolFactory()
        server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)
        print('startup...')
        server.serve()
        print('Bye')

    def send_sms(self, mobile_phone, msg):
        """
        发送短信
        Parameters:
         - mobile_phone 手机号
         - msg 消息内容
        """
        print('向{0}发送消息：{1};'.format(mobile_phone, msg))

    def send_email(self, email_addr, msg):
        """
        发送邮件
        Parameters:
         - email_addr 邮箱地址
         - msg 消息内容
        """
        print('向{0}发送邮件：{1};'.format(email_addr, msg))