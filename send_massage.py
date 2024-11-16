from wxauto import WeChat

class sender:
    
    def __init__(self, contact_list):
        self.contact_list = contact_list
        #self.wx = WeChat()

    
    def send_message_to_contacts(self, message, message_type='text'):
        try:
            wx = WeChat()
            if message_type == 'text':
                # 发送文本消息
                for contact in self.contact_list:
                    wx.SendMsg(message, contact)
            elif message_type == 'file':
                for contact in self.contact_list:
                    message = message.replace("\\", "/").replace("\"", "")
                    wx.SendFiles([message], contact)
            else:
                print("不支持的文件类型。")
        except Exception as e:
            print(f"发送出错：{str(e)}")