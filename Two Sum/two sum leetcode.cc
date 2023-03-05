class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int res;
        int i,j;

        for(i=0; i<nums.size(); i++)
            for(j=i+1; j<nums.size(); j++)
                if(nums[i] + nums[j] == target )
            {
                printf("i = %d, j = %d\n", i, j);
                res[0] = i;
                res[1] = j;
                return res;                
            }
    res[0] = -1;
    res[1] = -1;
    return res;
}
        
    }
};