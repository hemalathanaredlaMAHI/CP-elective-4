# longestCommonSubstring(s1, s2)[20 pts]
# Write the function, longestCommonSubstring(s1, s2), that takes two possibly-empty strings and returns the longest 
# string that occurs in both strings (and returns the empty string if either string is empty). For example:
# longestCommonSubstring("abcdef", "abqrcdest") returns "cde"
# longestCommonSubstring("abcdef", "ghi") returns "" (the empty string)
# If there are two or more longest common substrings, return the lexicographically smaller one 
# (ie, just use "<" to compare the strings). So, for example:
# longestCommonSubstring("abcABC", "zzabZZAB") returns "AB" and not "ab"

def longestcommonsubstring(s1, s2):
    # Yourcode goes here
    s=""
    m=0
    for i in range(0,len(s1)):
        if(s1[i] in s2):
            e=s1[i]
            for j in range(i+1,len(s1)):
                e=e+s1[j]
                if(e in s2 and m<len(e)):
                    m=len(s)
                    s=e
                else:
                    break
    return s





