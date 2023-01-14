#include <bits/stdc++.h>

using namespace std;

int main()
{
    int n,ch;

    while(true){
        cin>>n;
        if(n==-1)
            break;
        bool m[n][n];
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                cin>>m[i][j];
            }
        }
        for(int i=0;i<n;i++){
            ch = 0;
            for(int j=0;j<n;j++){
                if(m[i][j] == true){
                    for(int k=j+1;k<n;k++){
                        if(m[i][k] == true && m[j][k] == true){
                            ch = 1;
                            break;
                        }
                    }
                }
                if(ch == 1){
                    break;
                }
            }
            if(ch == 0){
                cout<<i<<" ";
            }
        }
        cout<<endl;
    }
}
