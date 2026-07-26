class Solution {
    public int minSubArrayLen(int target, int[] arr) {

        int i = 0;
        int j = 0;
        int sum = 0;
        int len = Integer.MAX_VALUE;

        while (j < arr.length) {

            if (sum < target) {
                sum += arr[j];
                j++;
                continue;
            }

            if (sum >= target) {
                len = Math.min(len, j - i);
                sum -= arr[i];
                i++;
                continue;
            }
        }

        while (sum >= target) {
            len = Math.min(len, j - i);
            sum -= arr[i];
            i++;
        }

        return len == Integer.MAX_VALUE ? 0 : len;
    }
}