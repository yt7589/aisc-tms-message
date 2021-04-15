# 主程序入口
from api.message_service import MessageService

def main(args={}):
    print('aisc-tms-message v0.0.1')
    message_service = MessageService()
    message_service.startup()

if '__main__' == __name__:
    main()