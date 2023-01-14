#include<bits/stdc++.h>
using namespace std;
int main()
{
    long long a,b;
    cin>>a>>b;
    while (!(a==0&&b==0))
    {
    long long A[a],n=0,B;
    for(int i=0;i<a;i++)
        cin>>A[i];
    for(int i=0;i<b;i++)
    {
        cin>>B;
        if(binary_search(A,A+a,B))
            n++;
    }
    cout<<n<<endl;
    cin>>a>>b;
    }
    
}


