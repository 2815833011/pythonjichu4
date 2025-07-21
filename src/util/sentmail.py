import yagmail
import traceback
import sys,os
sys.path.append(os.getcwd())
from src.util.config import Conf

class Mail:
    def __init__(self):
        self.mailconf=Conf().get_mailconf()
        
    def send_mail(self,subjiect,content,attachmenh=None):
        retval=True
        if self.mailconf["active"]:
            print("开始发送邮件")
            try:
                mail=yagmail.SMTP(**self.mailconf["sender"])
                mail.send(to=self.mailconf["to"],\
                          cc=self.mailconf["cc"],\
                          subject=subjiect,\
                          contents=content,\
                          attachments=attachmenh
                          )
                mail.close()
                print("发送成功")
            except :
                traceback.print_exc()
                retval=False

        return retval

if __name__ =="__main__":
    Mail().send_mail("test3","test")