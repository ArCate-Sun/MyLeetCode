package top.interview.questions.medium.collection.array.and.strings;

import java.util.*;

/**
 * Question:
 * Set Matrix Zeroes
 * See:
 * https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/776/
 */


public class SetMatrixZeroes {
    public void setZeroes(int[][] matrix) {

        if (matrix.length == 0) {
            return;
        }

        int row = matrix.length;
        int col = matrix[0].length;

        boolean hasZeroInFirstRow = false;
        boolean hasZeroInFirstCol = false;

        // 第一行是否有 0
        for (int i = 0; i < col; i++) {
            if (matrix[0][i] == 0) {
                hasZeroInFirstRow = true;
            }
        }
        // 第一列是否有 0
        for (int i = 0; i < row; i++) {
            if (matrix[i][0] == 0) {
                hasZeroInFirstCol = true;
            }
        }

        // 遍历矩阵中每一个元素,
        // 若有 0,
        // 则将该元素所在行列的第一个元素置为 0
        for (int r = 0; r < row; r++) {
            for (int c = 0; c < col; c++) {
                if (matrix[r][c] == 0) {
                    matrix[r][0] = 0;
                    matrix[0][c] = 0;
                }
            }
        }

        // 根据第一行, 第一列中的 0 的位置,
        // 将对应行列的元素全部置为 0
        for (int r = 1; r < row; r++) {
            for (int c = 1; c < col; c++) {
                if (matrix[r][0] == 0 || matrix[0][c] == 0) {
                    matrix[r][c] = 0;
                }
            }
        }

        // 若初始状态时第一行存在 0,
        // 则将第一行置为 0
        if (hasZeroInFirstRow) {
            for (int i = 0; i < col; i++) {
                matrix[0][i] = 0;
            }
        }
        // 若初始状态时第一列存在 0,
        // 则将第一列置为 0
        if (hasZeroInFirstCol) {
            for (int i = 0; i < row; i++) {
                matrix[i][0] = 0;
            }
        }
    }

    public void setZeroes2(int[][] matrix) {

        if (matrix.length == 0) {
            return;
        }

        int row = matrix.length;
        int col = matrix[0].length;

        Set<Integer> zeroRows = new HashSet<>();
        Set<Integer> zeroCols = new HashSet<>();
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                if (matrix[i][j] == 0) {
                    zeroRows.add(i);
                    zeroCols.add(j);
                }
            }
        }

        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                if (zeroRows.contains(i) || zeroCols.contains(j)) {
                    matrix[i][j] = 0;
                }
            }
        }
    }

}