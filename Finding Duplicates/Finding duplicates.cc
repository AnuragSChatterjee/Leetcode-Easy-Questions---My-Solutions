class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        int i, j;
        for (i=0;i<nums.size();i++){
        for(j=i+1;j<nums.size();j++){
            if (nums[i] == nums[j] ){
                return true;
                }
                }
                }
    return false;
    }
};