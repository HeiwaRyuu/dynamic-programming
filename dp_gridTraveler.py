def dp_gridTraveler(m,n, memo=None):
    ## initialize memo here to avoid mutable dict across different function calls
    if memo is None:
        memo = {}
    memokey = f"{m},{n}"
    if memokey in memo:
        return memo[memokey]
    if (m==1 and n==1):
        return 1
    if (m==0 or n==0):
        return 0
    
    memo[memokey] = dp_gridTraveler(m-1, n, memo) + dp_gridTraveler(m, n-1, memo)
    return memo[memokey]

def main():
    print(dp_gridTraveler(3,2)) # 3
    print(dp_gridTraveler(3,3)) # 6
    print(dp_gridTraveler(2,1)) # 1
    print(dp_gridTraveler(1,1)) # 1
    print(dp_gridTraveler(0,1)) # 0 
    print(dp_gridTraveler(5,10)) # 715
    print(dp_gridTraveler(18,18)) # 2333606220
    print(dp_gridTraveler(50,18)) # 2515943049305400

if __name__ == "__main__":
    main()