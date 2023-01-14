#include <iostream>
#include <iomanip>
using namespace std;
int main()
{
	int n;
	cin>>n;
	for(int i=0;i<n;i++)
	{
		double a,b,min,mid,max;
		cin>>a>>b;
		min=60.0*(a-1)/b;
		mid=60.0*a/b;
		max=60.0*(a+1)/b;
		cout<<fixed<<setprecision(4)<<min<<" "<<mid
		<<" "<<max<<endl;
	}
}
