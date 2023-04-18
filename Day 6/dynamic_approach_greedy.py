def make_change(coins,amount):
    
    dp = [[None]*(amount + 1) for x in range (len(coins) + 1)]
    for i in range (0,len(coins)+1):
        for j in range (0,amount+1):
            if(j==0):
               dp[i][j]=0
            elif(i==0):
               dp[i][j]=float('INF')
            elif(j<coins[i-1]):    # exclude this coin
                 dp[i][j]=dp[i-1][j]
            else:    # include the current coin 3
                dp[i][j]= min(dp[i-1][j], 1+dp[i][j-coins[i-1]])
    return dp[len(coins)][amount]

amount= 18
coins = [1,3,5]
print(make_change(coins,amount))
