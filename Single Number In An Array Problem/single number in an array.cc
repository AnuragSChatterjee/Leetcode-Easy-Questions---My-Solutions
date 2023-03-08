class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int output = 0;
        int i;
        for (i=0; i<nums.size(); i++) {
            output ^= nums[i];
    }
    return output;    
    }
};