class Solution {
    public int maxAreaOfIsland(int[][] grid) {

        int m = grid.length;
        int n = grid[0].length;
        int max_area = 0;
        

        for (int i=0; i<m; i++)
         for (int j = 0; j<n; j++)
        {
            if (grid[i][j] == 1)
            {
                int area = dfs(i, j, m, n, grid);
                max_area = Math.max(max_area, area);
            }
        }
        
        return max_area;
    }

     public int dfs(int i, int j, int m, int n, int [][] grid)
        {
            //boundary conditions
            if (i < 0 || i > m-1 || j < 0 || j > n-1 || grid[i][j] == 0)
            return 0; //wothless

            else {

                //first flood the cell
                grid[i][j] = 0;

                return 1+ dfs(i+1,j, m, n, grid)+ dfs(i, j-1, m, n, grid)+ dfs(i, j+1, m, n, grid)+dfs(i-1, j, m, n, grid);//do dfs on its 4 neighbors
            }

        }
}