from wxauto import *
import sys

import ray_name
import style
import send_massage

if __name__ == '__main__':

    style.welcome()

    Instance = ray_name.Ray_name()

    while True: #直到在用户输入的花名册中找到姓名为止
        excel_path = input("\n\n请输入花名册的地址：\n")
        if Instance.get_names_from_excel(excel_path):
            break
        else:
            pass
    
    try:
        with open('text_being_detected.txt', 'r', encoding='utf-8') as file:
            text = file.read()
    except FileNotFoundError:
        print("未找到名为 'text_being_detected.txt' 的文件，请手动创建。")
        exit()
    except Exception as e:
        print(f"读取文件时发生错误：{e}")
        exit()

    Instance.filter_text(text)
    missing_name = Instance.missing_name_list

    style.dividing_line()

    print("\n缺失的名字：\n\n")
    for name in missing_name:
        print(f"{name}\n")
    print(f"共{len(missing_name)}个\n")

    to_send = int(input("\n是否转到给缺失同学群发消息？（是：1，否：0）\n"))
    if to_send:

        Sender = send_massage.sender(missing_name)

        print("\n请将要发送的消息写入msg.txt文件中\n")
        massage_file = input("\n请输入要发送的文件地址，若不需发送文件，请输入0：\n")

        try:
            Sender.send_message_to_contacts("text")
            if massage_file and massage_file != '0':
                Sender.send_message_to_contacts(massage_file, 'file')
            else:
                print("未发送文件。")

        except Exception as e:
            print(f"发送出错：{str(e)}")

    else:
        sys.exit()
