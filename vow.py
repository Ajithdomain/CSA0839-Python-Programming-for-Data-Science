def c( n) :

        dp=[[0 for i in range(n)] for j in range(5)]

        for i in range(5):
            dp[i][0]=i+1

        dp[0]=[1 for i in range(n)]

        for j in range(1,n):
            for i in range(1,5):

                    dp[i][j]=dp[i-1][j]+dp[i][j-1]


        return dp[4][n-1]

n=int(input())
print(c(n))
0 comm
