#include <bits/stdc++.h>
using namespace std;
int main()
{
	int n;
	cin>>n;
	while(n!=-1)
	{
	int b=0,s=0;
	for(int i=0;i<n;i++)
	{
	   int x,y;
	   cin>>x>>y;
	   s+=x*(y-b);
	   b=y;
	}
	cout<<s<<" miles"<<endl;
	cin>>n;
   }
	
}
