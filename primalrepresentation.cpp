#include <bits/stdc++.h>
using namespace std;
bitset< 50000 > arr;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    long long int n = 50000, k, a;
    arr[0] = 1;
    arr[1] = 1;
    k = ceil(sqrt(n));
    for(int i=2; i<=k; i++){
        if (arr[i] == 0){
            for(int j=2*i; j<=n; j+=i){
                arr[j] = 1;
            }
        }
    }
    vector<long> prime;
    for(int i=2;i<=n;i++){
        if(!arr[i]){
            prime.push_back(i);
        }
    }
    while(cin>>a){
        if(a<0){
            cout<<"-1 ";
            a = a*-1;
        }
        map<int, int>vals;
        int f = 1;
        int sz = prime.size();
        while(f){
            for(long long it=0; it<sz; it++){
                if(a==prime[it]){
                    vals[prime[it]]++;
                    f = 0;
                    break;
                }
                if(a % prime[it] == 0){
                    a /= prime[it];
                    vals[prime[it]]++;
                    break;
                }
                if(it==sz-1){
                    vals[a]++;
                    f = 0;
                    break;
                }
            }
        }
        for(auto i:vals){
            if(i.second==1){
                cout<<i.first<<" ";
            }
            else{
                cout<<i.first<<"^"<<i.second<<" ";
            }
        }
        cout<<endl;
    }
}
