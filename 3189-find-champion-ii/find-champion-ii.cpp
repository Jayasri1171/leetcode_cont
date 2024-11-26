class Solution {
public:
    int findChampion(int n, vector<vector<int>>& edges) {
        vector<int>v;
        vector<int>m;
        if(n==1) return 0;
        for(int i=0;i<edges.size();i++){
            v.push_back(edges[i][0]);
            v.push_back(edges[i][1]);
            m.push_back(edges[i][1]);
        }
        set<int> s(v.begin(),v.end());
        set<int> s1(m.begin(),m.end());

        vector<int> vi(s.begin(),s.end());
        vector<int> mi(s1.begin(),s1.end());
        if(vi.size()<n) return -1;
        if(vi.size()-mi.size()!=1){
            return -1;
        }
        else{
            sort(vi.begin(),vi.end());
            sort(mi.begin(),mi.end());
            for(int j=0;j<mi.size();j++){
                if(vi[j]!=mi[j]){
                    return vi[j];
                }
            }
            return vi[vi.size()-1];
        }

    }
};