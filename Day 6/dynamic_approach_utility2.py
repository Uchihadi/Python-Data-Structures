def LCS(X,Y, i,j,dp={}):
    if (i==0 or j==0):
        return 0
    
    key=(i,j)
    
    if key not in dp:
        if X[i-1] == Y[i-1]:         
            dp[key]= 1+ LCS(X,Y,i-1,j-1)  
            
        else:
            dp[key]=max(LCS(X,Y,i,j-1),LCS(X,Y,i-1,j))    
            
            
    return dp[key]