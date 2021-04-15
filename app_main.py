# 主程序入口
import sys
from api.message_service import MessageService
from api.message_service_client import MessageServiceClient

def main(args={}):
    print('aisc-tms-message v0.0.1')
    run_mode = '1'
    if len(args) >= 2:
        run_mode = args[1]
    if '2' == run_mode:
        client = MessageServiceClient()
        client.send_email('bill@abc.com', '测试Thrift客户端功能')
        return
    message_service = MessageService()
    message_service.startup()

if '__main__' == __name__:
    main(sys.argv[:])