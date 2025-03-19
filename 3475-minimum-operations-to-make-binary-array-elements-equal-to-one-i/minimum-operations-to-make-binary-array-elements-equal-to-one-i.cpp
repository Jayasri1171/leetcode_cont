class Solution {
public:
    int minOperations(vector<int>& nums) {
        int i=0,a=0;
        int n=nums.size();
        while(i<n)
        {
            if(nums[i]==0)
            {
                int j=i+3;
                a+=1;
                for(int k=i;j<=n and k<j;k++)
                {
                    if(nums[k]==1){
                        nums[k]=0;
                    }
                    else{
                        nums[k]=1;
                    }
                }
            }
            i++;
        }
        int m=0;
        for(int p=0;p<n;p++){
            m+=nums[p];
        }
        if(m!=n){
            return -1;
        }
        else{
            return a;
        }
        
    }
};