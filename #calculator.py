#calculator.py
def add(a, b):
    """加法函数"""
    return a + b

def subtract(a, b):
    """减法函数"""
    return a - b

def multiply(a, b):
    """乘法函数"""
    return a * b

# 测试代码
if __name__ == "__main__":
    # 这部分代码只有在直接运行calculator.py时才会执行
    print("正在测试计算器功能...")
    print(f"10 + 5 = {add(10, 5)}")
    print(f"10 - 5 = {subtract(10, 5)}")
    print(f"10 * 5 = {multiply(10, 5)}")