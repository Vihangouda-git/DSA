class Solution {
public:
    long long minSumSquareDiff(vector<int>& nums1, vector<int>& nums2, int k1, int k2) {
        long long k = (long long)k1 + k2;
        vector<int> l(100001, 0);

        for (int i = 0; i < nums1.size(); i++) {
            int c = abs(nums1[i] - nums2[i]);
            l[c]++;
        }

        for (int i = 100000; i > 0 && k > 0; i--) {
            long long c = min((long long)l[i], k);
            l[i] -= c;
            l[i - 1] += c;
            k -= c;
        }

        long long ans = 0;
        for (int i = 1; i <= 100000; i++) {
            ans += 1LL * i * i * l[i];
        }

        return ans;
    }
};
