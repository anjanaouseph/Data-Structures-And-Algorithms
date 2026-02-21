class Solution {
    public int findMinimumPathSum(int i, int j, int[][]grid, int[][]dp) {      
// Our DP definition depends on future cells (right & down).
// So we must compute those first.
// Therefore we fill from bottom-right → top-left.
// To compute dp[i][j], we must already know:
// dp[i+1][j] (down)
// dp[i][j+1] (right)
// So we must compute those first.
// That means the computation must flow opposite to movement.
// f(i,j) = grid[i][j] + min( f(i+1,j), f(i,j+1) )
// We fill DP from bottom-right → top-left because:
// Every cell depends on the cells to its right and below,
// so those must be computed first.

    //base case
    if (i==0 && j==0)
        return grid[i][j]; //add this value to prev call

    if (i<0 || j<0)
        return Integer.MAX_VALUE-200; //so we can skip ths path. we move only left and up directions

    if (dp[i][j] != -1)
        return dp[i][j]; //take the already computed value, there are repeated subpbms

    int up = grid[i][j] + findMinimumPathSum(i-1, j, grid, dp);
    int left = grid[i][j] + findMinimumPathSum(i, j-1, grid, dp);

    return dp[i][j] = Math.min(up, left);

}

 public int minPathSum(int[][] grid)
    {
        int m = grid.length;
        int n = grid[0].length;

        int dp [][] = new int[m][n];

        for (int i = 0; i<m; i++)
            for (int j = 0; j<n; j++)
                dp[i][j]  = -1;       

        
        return findMinimumPathSum(m-1, n-1, grid, dp);
           
    }
}