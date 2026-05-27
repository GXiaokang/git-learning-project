
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def power(a, b):
    return a ** b

def divide(a, b):
    if b == 0:
        return "错误：除数不能为零"
    return a / b

if __name__ == "__main__":
    print("计算器已初始化")
    print(f"5 + 3 = {add(5, 3)}")
    print(f"5 - 3 = {subtract(5, 3)}")
    print(f"5 * 3 = {multiply(5, 3)}")
    print(f"2 ^ 5 = {power(2, 5)}")
    print(f"6 / 3 = {divide(6, 3)}")
    print(f"5 / 0 = {divide(5, 0)}")
