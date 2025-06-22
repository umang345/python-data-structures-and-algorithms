def countDistinctSubstrings(s):
    distinct = set()
    distinct.add("")

    for index in range(len(s)):
        for nextIndex in range(index, len(s)):
           distinct.add(s[index:nextIndex+1])

    return len(distinct) 