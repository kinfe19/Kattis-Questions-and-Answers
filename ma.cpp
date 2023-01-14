#include<bits/stdc++.h>
using namespace std;
int main()
{
    int n;
    cin>>n;
    for(int i=0;i<n;i++)
    {
        int a,b,c;
        cin>>a>>b>>c;
        if(a+b==c||a+c==b||b+c==a||abs(a-b)==abs(c)||abs(a-c)==abs(b)||abs(b-c)==abs(a)||a*b==c||b*c==a||a*c==b)
        cout<<"Possible"<<endl;
        else cout<<"Impossible"<<endl;

    }

}
