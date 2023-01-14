#include <iostream>
#include <cmath>
using namespace std;
int main()
{
	int n,w,h,u;
	cin>>n>>w>>h;
	int d=floor(sqrt(pow(w,2)+pow(h,2)));
	for(int i=0;i<n;i++)
	{
		cin>>u;
		if(u<=d)
		cout<<"DA"<<endl;
		else
		cout<<"NE"<<endl;
	}
}
