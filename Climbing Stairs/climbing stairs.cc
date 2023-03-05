class Solution {
public:
    int climbStairs(int n) {
        
        if (n==1) {
            return n;
        }

        if (n==2) {
            return n;
        }

        int most_previous_value = 1;
        int previous_value = 1;
        int current_value = 0;
        int i;

        for (i=2; i<n+1; i++) {
            current_value = previous_value + most_previous_value;
            most_previous_value = previous_value;
            previous_value = current_value;
    }
    return current_value;
}  
};