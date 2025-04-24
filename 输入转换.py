string_data = input()
string_data = string_data.strip()

if string_data.startswith("Course:"):
    # 处理 Course: 开头的情况
    print(string_data.lower())
elif string_data[0].isupper():
    # 处理首字母大写的情况
    print(string_data[0] + string_data[1:].lower())
elif string_data.islower():
    # 处理全小写的情况
    print(string_data.capitalize())
else:
    # 其他情况保持原样
    print(string_data)