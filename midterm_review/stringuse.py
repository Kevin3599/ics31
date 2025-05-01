text = " Hello World "

# 常用方法
print(text.strip())         # 去除两端空格
print(text.lower())         # 转小写
print(text.upper())         # 转大写
print(text.replace('o', 'x'))  # 替换
print(text.split())         # 分割成列表
print(','.join(['a','b']))  # 列表合并为字符串

s = "apple,banana,cherry"
fruits = s.split(",")  # 得列表 ['apple', 'banana', 'cherry']

s2 = " ".join(fruits)  # 得 "apple banana cherry"
print(s2)