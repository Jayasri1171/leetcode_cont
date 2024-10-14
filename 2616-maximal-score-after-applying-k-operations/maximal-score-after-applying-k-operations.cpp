class Solution {
public:
    long long maxKelements(vector<int>& nums, int k) {
        priority_queue<int>pq;
        for(int i=0;i<nums.size();i++){
            pq.push(nums[i]);
        }
        long long count=0;
        while(k){
            int z=pq.top();
            count+=z;
            pq.pop();
            if(z%3==0) pq.push(z/3);
            else pq.push(int(z/3)+1);
            k-=1;
        }
        return count;
    }
};