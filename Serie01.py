def serie1(n):
    if n > 1:
        return n + serie1(n-1)
    else:
        return 1
    
def main():
    N: int = 100

    print(serie1(N))

if __name__ == '__main__':
    main()