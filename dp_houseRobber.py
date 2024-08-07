def recursive_rob(nums, i, memo=None):
    if memo is None:
        memo = {}
    if i in memo:
        return memo[i]
    if (i < 0):
        return 0
    
    result = max(recursive_rob(nums, i - 2, memo) + nums[i], recursive_rob(nums, i - 1, memo))
    memo[i] = result
    return result

def rob(nums):
    return recursive_rob(nums, len(nums)-1, memo=None)
    

def main():
    print(rob([1, 2, 3, 1])) # 4
    print(rob([2,7,9,3,1])) # 12
    print(rob([1,3,1])) # 3
    print(rob([183,219,57,193,94,233,202,154,65,240,97,234,100,249,186,66,90,238,168,128,177,235,50,81,185,165,217,207,88,80,112,78,135,62,228,247,211])) # 3365

if __name__ == "__main__":
    main()