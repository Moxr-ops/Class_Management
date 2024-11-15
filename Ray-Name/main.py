import functions

if __name__ == '__main__':

    Instance = functions.Ray_name()

    excel = input("\n\n请输入花名册的地址：\n")
    text = input("\n\n请输入要检索的文本：\n")

    Instance.get_names_from_excel(excel)

    missing_name = Instance.filter_text(text)

    print(f"缺失的名字：{missing_name}")