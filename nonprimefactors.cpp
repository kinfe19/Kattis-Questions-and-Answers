
#include <bits/stdc++.h>
#define endl "\n"
using namespace std;

int main()
{
	ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    int n = 2000001;
	int arr[n] = {0};
    arr[0] = arr[1] = 1;
    for(int i=2; i*i<=n; i++){
        if(arr[i] == 0){
            for(int j=i*i; j<n; j+=i){
                arr[j] = 1;
            }
        }
    }
    for(int i=4; i*2<n; i++){
        if(arr[i] != 0){
            for(int j=i*2; j<n; j+=i){
                arr[j] += 1; 
            }
        }
    }

    int t, v;
    cin>>t;
    while(t--){
        cin>>v;
        cout<< arr[v]+1<<"\n";
    }
}