#include <bits/stdc++.h>

using namespace std;

int main()
{
    int t, h, n, en, ha;
    cin >> t>> h;
    ha = t / 2;
    vector<int> ar1, ar2;
    for(int i=0; i<t; i++){
        cin >> n;
        if(i%2==0){
            ar1.push_back(n);
        }
        else{
            ar2.push_back(n);
        }
    }
    sort(ar1.begin(), ar1.end());
    sort(ar2.rbegin(), ar2.rend());
    int mn=t, cn=1, x1=0, x2=0;
    for(int i=1; i<=h; i++){
        while(x1 < ha){
            if(ar1[x1]>=i){
                break;
            }
            x1 ++;
        }
        //cout<<" " <<x2<<" " <<-ha<<endl;
        while(x2<ha){
            //cout<<" " <<x2<<" " <<h<<" "<< ar2[x2]<<" "<<i <<endl;
            if(h-ar2[x2] >= i){
                break;
            }
            x2++;
        }
        //cout<<x1<<" "<<x2<<end;
        int s = ha-x1 + x2;
        //cout<<"-----" <<s<<"----"<<endl;
        if(mn == s){
            cn++;
        }
        else if(s<mn){
            mn = s;
            cn = 1;
        }
        //cout<<mn<<"-----" <<s<<"----"<<endl;
    }
    cout<<mn<<" " <<cn<<"\n";
}
