class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int output;
        int majority_element_counter = 0;
        for (int i=0; i<nums.size(); i++) {
        for (int j = i+1; j<nums.size(); j++) {
            if (nums[i] == nums[j]) {
                majority_element_counter +=1;
                output = nums[i];
            }
        }
        }
        return output;
    }
};