def canConstruct(target, wordBank, memo=None):
    ## initialize memo here to avoid mutable dict across different function calls
    if memo is None:
        memo = {}
    if target in memo:
        return memo[target]
    if target == '':
        return True
    
    for word in wordBank:
        if word in target and target.find(word) == 0:
            remainder = target[len(word):]
            isPossible = canConstruct(remainder, wordBank, memo)
            if isPossible:
                memo[target] = True
                return True

    memo[target] = False
    return False

def main():
    print(canConstruct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd'])) ## true
    print(canConstruct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'])) ## false
    print(canConstruct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't'])) ## true
    print(canConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', 
                       ['e', 
                        'ee', 
                        'eee', 
                        'eeee', 
                        'eeeee', 
                        'eeeeee',
                        ])) ## false

if __name__ == "__main__":
    main()