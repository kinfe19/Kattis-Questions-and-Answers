#include <iostream>
using namespace std;
int main()
{
	int a[6]={1,1,2,2,2,8};
	int b[6];
	for(int i=0;i<6;i++)
	cin>>b[i];
	for(int j=0;j<6;j++)
	cout<<a[j]-b[j]<<" ";
}
