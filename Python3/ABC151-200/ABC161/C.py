def main():
    N, K = list(map(int, input().split()))
    m = N % K
    m = min(m, abs(K-m))
    print(m)
 
if __name__ == '__main__':
    main()