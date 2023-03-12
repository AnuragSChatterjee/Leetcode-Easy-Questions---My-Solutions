void moveZeroes(int* nums, int numsSize){
    int j = 0;
    int i;

    for (i==0; i<numsSize; i++) {
        if (nums[i] != 0) {
            nums[i], nums[j] = nums[j], nums[i];
            i++;
            j++;
        }
        else {
            i++;
            j++;
        }
    return nums;
    }

}