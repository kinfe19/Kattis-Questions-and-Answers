#include <bits/stdc++.h>
using namespace std;

bool check(int p[], int n){
    bool flag = true;
    int t, h, k, l;
    for(int i=0; i<n-2; i++){
    	t = p[i];
        for(int j=i+1; j<n; j++){
        	h = p[j];
        	k = 2*j - i;
        	if(k >= n){
            	break;
            }
            l = p[k];
            if((t < h and h < l) || (l < h and h < t)){
            	// cout<<i<<" "<<j<<" "<<k<<"\n";
                flag = false;
                break;
            }
            
        }
        if(!flag){
            break;
        }
    }
    return flag;
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    string s;
    while(1){
        cin>>s;
        if(s == "0"){
            break;
        }
        int n = stoi(s.substr(0, s.length()-1));
        int arr[n], pos[n], kk;
        for(int i=0; i<n; i++){
            cin>>kk;
            arr[i] = kk;
            pos[kk] = i;
        }
        if(check(pos, n)){
            cout<<"yes\n";
        }
        else{
            cout<<"no\n";
        }
    }
}