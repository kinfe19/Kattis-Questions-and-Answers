#include <bits/stdc++.h>
using namespace std;
int main()
{
    int n,s=0;
    cin>>n;
    for(int i=0;i<n;i++)
    {
        int b;
        cin>>b;
        if(b<0)
            s-=b;
    }
    cout<<s;
}
