def countConstruct(target, wordBank, memo=None):
    ## initialize memo here to avoid mutable dict across different function calls
    if memo is None:
        memo = {}
    if target in memo:
        return memo[target]
    if target == '':
        return 1
    
    count = 0
    for word in wordBank:
        if word in target and target.find(word) == 0:
            remainder = target[len(word):]
            count += countConstruct(remainder, wordBank, memo)
            
    if target not in memo:
        memo[target] = count
    return count

def main():
    print(countConstruct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd'])) ## 1
    print(countConstruct('purple', ['purp', 'p', 'ur', 'le', 'purpl'])) ## 2
    print(countConstruct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'])) ## 0
    print(countConstruct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't'])) ## 4
    print(countConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', 
                       ['e', 
                        'ee', 
                        'eee', 
                        'eeee', 
                        'eeeee', 
                        'eeeeee',
                        ])) ## 0

if __name__ == "__main__":
    main()