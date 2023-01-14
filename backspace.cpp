#include <bits/stdc++.h>
using namespace std;

int main(){
    string s, p="";
    cin>>s; 
    int x=0, c=0;
    for(int i=s.length()-1; i>=0; i--){
        if(s[i] != '<'){
            if(c == 0){
                p += s[i];
                x++;
            }
            else{
                c--;
            }
            
        }
        else{
            c++;
        }

    }
    for(int i=x-1; i>=0; i--){
        cout<<p[i];
    }
    cout<<"\n";
}