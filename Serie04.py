def serie4(n, i):
    if i > n:
        return 0
    else:
        return (n - i + 1)/i + serie4(n, i + 1)
    
def main():
    N = int(input("Digite um numero:"))
    
    print(serie4(N, 1))

if __name__ == '__main__':
    main()