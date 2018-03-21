//
// Valid Sudoku
//
// Required:
// Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.
// The Sudoku board could be partially filled, where empty cells are filled with the character '.'.
//
// Note:
// A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.
//

#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    bool isValidSudoku(vector<vector<char>> &board) {

        vector<vector<int>> int_board = this->getIntBoard(board);

        for (int x = 0; x < 9; ++x) {
            for (int y = 0; y < 9; ++y) {
                if (!this->verifyByRows(int_board, x, y)) return false;
                if (!this->verifyByColumns(int_board, x, y)) return false;
                if (!this->verifyByBlocks(int_board, x, y)) return false;
            }
        }

        return true;
    }

private:
    // 获得 int 类型元素的 board
    vector<vector<int>> getIntBoard(vector<vector<char>> &board) {
        vector<vector<int>> result;
        for (int i = 0; i < 9; ++i) {
            result.push_back(vector<int>(9));
        }

        for (int i = 0; i < 9; ++i) {
            for (int j = 0; j < 9; ++j) {
                if (board[i][j] == '.')
                    result[i][j] = 0;
                else
                    result[i][j] = board[i][j] - '0';
            }
        }

        return result;
    }

    // 横向遍历过滤候选组
    bool verifyByRows(vector<vector<int>> &board, int x, int y) {

        if (board[y][x] == 0) return true;

        for (int i = 0; i < 9; ++i) {
            if (i == x) continue;
            if (board[y][x] == board[y][i]) return false;
        }
        return true;
    }

    // 纵向遍历过滤候选组
    bool verifyByColumns(vector<vector<int>> &board, int x, int y) {

        if (board[y][x] == 0) return true;

        for (int i = 0; i < 9; ++i) {
            if (i == y) continue;
            if (board[y][x] == board[i][x]) return false;
        }
        return true;
    }

    // 特定的 3 x 3 方阵中遍历过滤候选组
    bool verifyByBlocks(vector<vector<int>> &board, int x, int y) {

        if (board[y][x] == 0) return true;

        for (int x_abstr = 0; x_abstr < 3; ++x_abstr) {
            for (int y_abstr = 0; y_abstr < 3; ++y_abstr) {
                int x_real = x / 3 * 3 + y_abstr;
                int y_real = y / 3 * 3 + x_abstr;
                if (y_real == y && x_real == x) continue;
                if (board[y][x] == board[y_real][x_real]) return false;
            }
        }
        return true;
    }

};
