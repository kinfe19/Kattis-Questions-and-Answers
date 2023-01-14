#include <iostream>
using namespace std;
int main()
{
	int n;
	cin>>n;
	for(int i=0;i<n;i++)
	{
		int z,y;
		cin>>z>>y;
		double a=(z+y)/2.0,b=(z-y)/2.0;
		if(b<0 || a!=int(a)||b!=int(b))
		cout<<"impossible"<<endl;
		else
		cout<<a<<" "<<b<<endl;
	}
	
	
}
