def howSum(targetSum, numbers):
    complement = {}
    for number in numbers:
        if number==targetSum:
            return (number, 0)
        if targetSum-number in complement:
            return (targetSum-number, complement[targetSum-number])
        else:
            complement[number] = targetSum-number
    return None
            

def main():
    print(howSum(7, [5, 3, 8, 2, 7])) # (5, 2)
    print(howSum(17, [4, 35, 10, 2, 7])) # (10, 7)
    print(howSum(43, [7, 11, 45, 18, 2, 25])) # (18, 25)
    print(howSum(21, [5, 3, 8, 2, 16, 7])) # (5, 16)
    print(howSum(22, [5, 3, 8, 2, 16, 7])) # None
    print(howSum(7, [2, 4])) # None
    print(howSum(300000, [7, 14])) # None

if __name__ == "__main__":
    main()