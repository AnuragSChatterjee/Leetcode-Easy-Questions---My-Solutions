int* twoSum(int* nums, int numsSize, int target, int* returnSize){    
    * returnSize = 2;
    int* res = (int*)malloc(sizeof(int) * 2);
    int i,j;

    for(i=0; i<numsSize; i++)
        for(j=i+1; j<numsSize; j++)
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