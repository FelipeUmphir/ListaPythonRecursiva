def serie3(n):
    if n > 1:
        return 1/n + serie3(n-1)
    else:
        return 1
    
def main():
    N = int(input("Digite um numero:"))

    print(serie3(N))

if __name__ == '__main__':
    main()