#include <iostream>
#include <iomanip>
using namespace std;
int main()
{
	int n;
	cin>>n;
	double s=0.0,c;
	for(int i=0;i<n;i++)
	{
		int a;
		cin>>a;
		if(a>=0 && a<=4)
		{
			c++;
			s+=a;
		}
	}
	cout<<fixed<<setprecision(10)<<s/c;
}
