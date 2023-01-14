#include <iostream>
#include <iomanip>
using namespace std;
int main()
{
	double a,b,s=0.0;
	cin>>a>>b;
	for(int i=0;i<b;i++)
	{
		double c,d;
		cin>>c>>d;
		s+=a*c*d;
	}
	cout<<fixed<<setprecision(8)<<s;
}
