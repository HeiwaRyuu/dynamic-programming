def allConstruct(target, wordBank, memo=None):
    ## initialize memo here to avoid mutable dict across different function calls
    if memo is None:
        memo = {}
    if target in memo:
        return memo[target]
    if target == '':
        return [[]]
    
    result = []
    for word in wordBank:
        if word in target and target.find(word) == 0:
            remainder = target[len(word):]
            suffixWays = allConstruct(remainder, wordBank, memo)
            targetWays = suffixWays[:]
            for index, way in enumerate(targetWays):
                helper = way[:]
                helper.insert(0, word)
                targetWays[index] = helper
            result.extend(targetWays)
    
    memo[target] = result
    return result

def main():
    print(allConstruct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))  # [['abc', 'def']]
    print(allConstruct('purple', ['purp', 'p', 'ur', 'le', 'purpl']))  # [['purp', 'le'], ['p', 'ur', 'p', 'le']]
    print(allConstruct('le', ['purp', 'p', 'ur', 'le', 'purpl']))  # [['le']]
    print(allConstruct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'])) # []
    print(allConstruct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't']))  # [['enter', 'a', 'p', 'ot', 'ent', 'p', 'ot'], ['enter', 'a', 'p', 'ot', 'ent', 'p', 'o', 't'], ['enter', 'a', 'p', 'o', 't', 'ent', 'p', 'ot'], ['enter', 'a', 'p', 'o', 't', 'ent', 'p', 'o', 't']]
    print(allConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', 
                       ['e', 
                        'ee', 
                        'eee', 
                        'eeee', 
                        'eeeee', 
                        'eeeeee',
                        ])) # []

if __name__ == "__main__":
    main()