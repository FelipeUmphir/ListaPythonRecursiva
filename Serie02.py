def serie2(n):
    if n > 1:
        return n + serie2(n-1)
    else:
        return 1
    
def main():
    N = int(input("Digite um numero:"))

    print(serie2(N))

if __name__ == '__main__':
    main()