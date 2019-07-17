package top.interview.questions.medium.collection.array.and.strings;

import java.util.*;

/**
 * Question:
 *      3 Sum
 * See:
 *      https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/776/
 */

public class ThreeSum {

    public List<List<Integer>> threeSum(int[] nums) {

        List<List<Integer>> result = new LinkedList<>();

        Arrays.sort(nums);
        int zeroPos = Arrays.binarySearch(nums, 0);
        int lastNegativePos = zeroPos;
        int firstPositivePos = zeroPos;
        if (zeroPos < 0) {
            lastNegativePos = - zeroPos - 2;
            firstPositivePos = - zeroPos - 1;
        } else {
            while (--lastNegativePos >= 0 && nums[lastNegativePos] == 0);
            while (++firstPositivePos < nums.length && nums[firstPositivePos] == 0);
        }

        if (firstPositivePos - lastNegativePos > 3) {
            result.add(Arrays.asList(0, 0, 0));
        }

        int nPos = 0;
        while (nPos <= lastNegativePos) {

            int l = nPos + 1;
            int r = nums.length - 1;
            while (l < r) {
                if (nums[l] + nums[r] + nums[nPos] == 0) {
                    result.add(Arrays.asList(nums[nPos], nums[l], nums[r]));
                    while (++l + 1 < r && nums[l - 1] == nums[l]);
                    while (l < --r && nums[r + 1] == nums[r]);
                } else if (nums[l] + nums[r] + nums[nPos] > 0) {
                    while (l < --r && nums[r + 1] == nums[r]);
                } else {
                    while (++l + 1 < r && nums[l - 1] == nums[l]);
                }
            }

            while (++nPos < nums.length && nums[nPos - 1] == nums[nPos]);
        }

        return result;

    }

    public List<List<Integer>> threeSum2(int[] nums) {

        List<List<Integer>> result = new LinkedList<>();

        Map<Integer, Integer> numberToCount = new HashMap<>();
        for (int n : nums) {
            numberToCount.put(n, numberToCount.getOrDefault(n, 0) + 1);
        }

        List<Integer> positives = new LinkedList<>();
        List<Integer> negatives = new LinkedList<>();
        for (int n : numberToCount.keySet()) {
            if (n > 0) {
                positives.add(n);
            } else if (n < 0) {
                negatives.add(n);
            }
        }

        if (numberToCount.getOrDefault(0, 0) > 2) {
            result.add(Arrays.asList(0, 0, 0));
        }

        for (int p : positives) {
            for (int n : negatives) {
                int need = -(p + n);
                if (need == p && numberToCount.get(p) > 1) {
                    result.add(Arrays.asList(n, p, p));
                } else if (need == n && numberToCount.get(n) > 1) {
                    result.add(Arrays.asList(n, n, p));
                } else if (numberToCount.containsKey(need) && need > n && need < p) {
                    result.add(Arrays.asList(n, need, p));
                }
            }
        }

        return result;

    }

    boolean judge(int[][] result, List<List<Integer>> output) {

        // 判断结果是否正确
        Set<Map<Integer, Integer>> setResult = new HashSet<>();
        for (int[] r : result) {
            Map<Integer, Integer> map = new HashMap<>();
            for (int n : r) {
                map.put(n, map.getOrDefault(n, 0));
            }
            setResult.add(map);
        }
        Set<Map<Integer, Integer>> setOutput = new HashSet<>();
        for (List<Integer> o : output) {
            Map<Integer, Integer> map = new HashMap<>();
            for (int n : o) {
                map.put(n, map.getOrDefault(n, 0));
            }
            setOutput.add(map);
        }
        return setResult.equals(setOutput);
    }

    public static void main(String[] args) {
        int[][] demos = {
                {-1, 0, 1, 2, -1, -4},
                {0, 0, 0},
                {-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6},
                {-4,-2,-1}
        };

        int[][][] results = {
                {
                        {-1, -1, 2},
                        {-1, 0, 1}
                },
                {
                        {0, 0, 0}
                },
                {
                        {-4, -2, 6},
                        {-4, 0, 4},
                        {-4, 1, 3},
                        {-4, 2, 2},
                        {-2, -2, 4},
                        {-2, 0, 2}
                },
                {}

        };

        ThreeSum solution = new ThreeSum();
        for (int i = 0; i < Math.min(demos.length, results.length); i++) {

            int[] demo = demos[i];
            List<List<Integer>> output = solution.threeSum(demos[i]);

            System.out.format("INPUT: %s\n", Arrays.toString(demo));
            if (solution.judge(results[i], output)) {
                System.out.format("\033[0;32mOUTPUT: %s\033[0m\n\n", output);
            } else {
                System.out.format("\033[0;31mOUTPUT: %s\033[0m\n", output);
                System.out.format("\033[0;36mEXPECT: %s\033[0m\n\n", Arrays.toString(results[i]));
            }

        }
    }
}