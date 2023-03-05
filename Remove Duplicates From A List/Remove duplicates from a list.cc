class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int i=1,k=1;
        
        if(nums.size()==1)
            return nums.size();
        while(k<nums.size()) {
            if(nums[k]==nums[k-1])
            k++;
        else
            nums[i++]=nums[k++];}
        return i;
}
};