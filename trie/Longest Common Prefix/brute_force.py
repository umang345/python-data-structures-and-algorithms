def longestCommonPrefix(arr, n):
    
    result = []
    for index in range(len(arr[0])):

        ch = arr[0][index]
        for word in arr:
            if len(word) <= index or word[index]!=ch:
                return "".join(result)
        
        result.append(ch)
    
    return "".join(result)
            



