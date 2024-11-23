def paired_numbers (a,b):
    for i in range(a+1,b):
        if i % 2 == 0:
            print(i)

if __name__ == '__main__':
    _a = int(input())
    _b = int(input())
    paired_numbers(_a,_b)