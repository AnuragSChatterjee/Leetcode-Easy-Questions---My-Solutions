class Solution {
public:
    bool isHappy(int n) {
        int sum=0;
        int remainder;
        while (n<10){
            if(n==1||n==7){
                return 1;
                }
            else{
                return 0;
                }
        }
        while (n>0){
            remainder=n%10;
            sum+=pow(remainder, 2);
            n/=10;
        }
        return isHappy(sum);
    }
};