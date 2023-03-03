int removeDuplicates(int* nums, int numsSize){
     int i=1,k=1;
    if(numsSize==1)
        return numsSize;
    while(k<numsSize)
    {if(nums[k]==nums[k-1])
        k++;
     else
         nums[i++]=nums[k++];}
    return i;
}