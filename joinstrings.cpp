#include <bits/stdc++.h>
#define endl "\n"
using namespace std;


int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    int n, a, b;cin>>n;
    string arr[n], brr[n];
    vector<int>v[n];
    for(int i=0; i<n; i++){
        cin>>arr[i];
        brr[i] = to_string(i);
    }
    for(int i=0; i<n-1; i++){
        cin>>a>>b;
        v[a-1].push_back(b-1);
    }
    if(n==1){
        cout<<arr[0]<<endl;
    }
    else{
        stack<int>st;
        st.push(a-1);
        int ss;
        while(!st.empty()){
            ss = st.top();
            st.pop();
            for(int j=v[ss].size()-1; j>=0; j--){
                st.push(v[ss][j]);
            }
            cout<<arr[ss];
        }
        cout<<endl;
    }
}