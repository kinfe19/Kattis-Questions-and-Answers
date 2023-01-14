#include <iostream>
#include <iomanip>
using namespace std;
int main()
{
	int n;
	cin>>n;
	double sum=0,a,b;
	for(int i=0;i<n;i++)
	{
		cin>>a>>b;
		sum+=a*b;
	}
	cout<<fixed<<setprecision(3)<<sum;
}
