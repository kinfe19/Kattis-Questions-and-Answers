#include <iostream>
#include <iomanip>
using namespace std;
int main()
{
	int n;
	cin>>n;
	for(int i=0;i<n;i++)
	{
		int b,g;
		double sum=0,avg,c=0;
		cin>>b;
		int a[b];
		for(int j=0;j<b;j++)
		{
			cin>>a[j];
			sum+=a[j];
		}
		avg=sum/b;
		for(int t=0;t<b;t++)
			if(a[t]>avg)
		       c++;
		cout<<fixed<<setprecision(3)<<c/b*100.0<<"%"<<endl;
	}
}
