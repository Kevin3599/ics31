def fibonacci(n):
    if n < 0:
        return -1
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
        
    a, b = 1, 1
    for i in range(2, n):
        a, b = b, a + b
    return b

def main():
    start_num = int(input())
    print(f'fibonacci({start_num}) is {fibonacci(start_num)}')

if __name__ == '__main__':
    main()