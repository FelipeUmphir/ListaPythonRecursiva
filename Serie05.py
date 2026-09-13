def fat(num):
    if num > 1:
        return num * fat(num - 1)
    else:
        return 1

def serie5(n):
    if n > 1:
        return fat(n) + serie5(n-1)
    else:
        return 1
    
def main():
    N = int(input("Digite um numero:"))
    
    print(serie5(N))

if __name__ == '__main__':
    main()