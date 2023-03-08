int singleNumber(int* nums, int numsSize){
    int output = 0;
    int i;
    for (i=0; i<numsSize; i++) {
        output ^= nums[i];
    }
    return output;
}