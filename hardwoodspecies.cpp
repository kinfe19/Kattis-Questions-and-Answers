#include<bits/stdc++.h>

using namespace std;

int main()
{
    map < string, int> ss;
    int c =0;
    string s;
    while(getline(cin,s)){
        ss[s]++;
        c++;
    }
    //sort(ss.begin(), ss.end());
    for(auto i:ss){
        cout<<i.first<<" " << fixed << setprecision(6)<<i.second*100.0 / c<<"\n";
    }
}