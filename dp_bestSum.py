def bestSum(targetSum, numbers, memo=None):
    ## initialize memo here to avoid mutable dict across different function calls
    if memo is None:
        memo = {}
    if targetSum in memo:
        return memo[targetSum]
    if targetSum==0:
        return []
    if targetSum<0:
        return None

    bestResult = None
    for number in numbers:
        remainder = targetSum-number
        remainderResult = bestSum(remainder, numbers, memo)
        if remainderResult is not None:
            combination = remainderResult[:]
            combination.append(number)
            if (bestResult is None) or (len(combination) < len(bestResult)):
                bestResult = combination[:]

    memo[targetSum] = bestResult
    return bestResult

def main():
    print(bestSum(7, [5,3,4])) # [4, 3]
    print(bestSum(7, [5,3,4,7])) # [7]
    print(bestSum(8, [2,3,5])) # [5, 3]
    print(bestSum(8, [1,4,5])) # [4, 4]
    print(bestSum(25, [1,2,5])) # [5, 5, 5, 5, 5]
    print(bestSum(100, [1,2,5,25])) # [25, 25, 25, 25]
    print(bestSum(1000, [2, 5,25, 50, 100, 150])) # [150, 150, 150, 150, 150, 150, 100]

if __name__ == "__main__":
    main()