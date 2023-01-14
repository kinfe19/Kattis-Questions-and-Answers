#include <bits/stdc++.h>
using namespace std;
int main()
{
    int A[24]={0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23};
    int a,b,h,m;
    cin>>a>>b;
    if(b>=45)
    cout<< a<<" "<<b-45;
    else
    {
        if(a==0)
        h=23;
        else
        h=a-1;
        m=b+15;
        cout<<h<<" "<<m;
    }
}
