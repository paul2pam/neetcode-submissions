class Solution {
public:
    int islandPerimeter(vector<vector<int>>& grid) {
        int row = grid.size();
        int col = grid[0].size();

        int perimeter = 0;

        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                if (grid[i][j] == 1) {
                    int local = 0;
                    if (i == 0) {
                        local++;
                    } else if (grid[i-1][j] == 0){
                        local++;
                    }

                    if (i == row - 1) {
                        local++;
                    } else if (grid[i+ 1][j] == 0){
                        local++;
                    }

                    if (j == 0) {
                        local++;
                    } else if (grid[i][j - 1] == 0){
                        local++;
                    }

                    if (j == col - 1) {
                        local++;
                    } else if (grid[i][j + 1] == 0){
                        local++;
                    }

                    perimeter += local;
                }
            }
        }
        return perimeter;
    }
};