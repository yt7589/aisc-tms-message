#

class MessageService(object):
    def __init__(self):
        self.name = 'api.MessageService'

    def startup(self):
        print('启动Thrift消息服务器')

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