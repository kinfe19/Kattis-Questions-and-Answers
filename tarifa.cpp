#include <iostream>
using namespace std;
int main()
{
	int n,m;
	cin>>m>>n;
	int a,sum=0;
	bool v=true;
	for(int i=0;i<n;i++)
	{
		cin>>a;
		if(a>m+sum)
		{
			v=false;
		}
		else
		sum+=m-a;
	}
	if(v)
	cout<<sum+m;
	
}
