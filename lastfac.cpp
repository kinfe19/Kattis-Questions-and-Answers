#include <iostream>
using namespace std;
int fac(int n)
{
	if(n==0||n==1)
	return 1;
	else
	return n*fac(n-1);
}
int main()
{
	int b;
	cin>>b;
	for(int i=0;i<b;i++)
	{
		int n,m;
		cin>>n;
		if(n<=10)
		{
	        m=fac(n)%10;
	        cout<<m<<endl;
		}

	}
}
