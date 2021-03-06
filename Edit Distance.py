'''
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

'''

def editDistance(word1, word2):
    m = len(word1)
    n = len(word2)
    
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)] 

    for i in range(m + 1): 
        for j in range(n + 1): 
            if i == 0: 
                dp[i][j] = j   
            
            elif j == 0: 
                dp[i][j] = i    

            elif word1[i-1] == word2[j-1]: 
                dp[i][j] = dp[i-1][j-1] 

            else: 
                dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])
                
    return dp[-1][-1]
    
print(editDistance("horse", "ros"))
