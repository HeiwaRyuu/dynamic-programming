def dp_fib(n, memo=None):
    ## initialize memo here to avoid mutable dict across different function calls
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if(n<=2):
        return 1
    memo[n] = dp_fib(n-1, memo) + dp_fib(n-2, memo)
    return memo[n]

def main():
    print(dp_fib(1)) # 1
    print(dp_fib(2)) # 1
    print(dp_fib(3)) # 2
    print(dp_fib(4)) # 3
    print(dp_fib(5)) # 5
    print(dp_fib(6)) # 8
    print(dp_fib(7)) # 13
    print(dp_fib(8)) # 21
    print(dp_fib(9)) # 34
    print(dp_fib(50)) # 12586269025


if __name__ == "__main__":
    main()