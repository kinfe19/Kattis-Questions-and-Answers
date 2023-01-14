#include <bits/stdc++.h>

using namespace std;

int main()
{
    long long a, b, c, sm=0, k;
    vector<int>v;
    cin >>a>>b;
    for(int i=0; i<a; i++){
        cin >> c;
        v.push_back(c);
    }
    sort(v.begin(), v.end());
    for(int i=0; i<b; i++){
        cin >> c;
        k = *lower_bound(v.begin(), v.end(), c);
        sm += k - c;
    }
    cout<<sm;
}
